__author__ = 'Jian Yang'
__date__ = '11/30/15'

from ParsingUtils import *

import pandas
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import scipy.stats
import random

import reg

def median(lst):
    return np.median(np.array(lst))

def sqr(x):
    return x * x

def distance(x0, y0, x1, y1):
    return sqr(x0-x1) + sqr(y0-y1)

class DataAnalyzor:
    def __init__(self):
        self.all_res = None
        self.stat_res = os.path.dirname(os.path.realpath(__file__)) + '/stat.res'

        self.algos = ['sailfish', 'kallisto', 'rsem', 'truth']
        self.algo_res = {'sailfish':os.path.dirname(os.path.realpath(__file__)) + '/quant.sf',
                         'kallisto':os.path.dirname(os.path.realpath(__file__)) + '/kall.tsv',
                         'rsem':os.path.dirname(os.path.realpath(__file__)) + '/rsem.result',
                         'truth':os.path.dirname(os.path.realpath(__file__)) + '/config.pro'}
        self.algo_method = {'sailfish':readSailfish,
                            'kallisto':readKallisto,
                            'rsem':readRSEMTruth,
                            'truth':readProFile}
        self.algo_fields = {'sailfish':[],
                            'kallisto':[],
                            'rsem':[],
                            'truth':[]}
        self.truth_field = []
        self.stat_field = []
        self.bar = {}

    def load_data(self):
        self.all_res = readTranscriptRes(self.stat_res)
        self.stat_field = self.all_res.columns

        for algo_name, algo_resfile in self.algo_res.items():
            algo_res = self.algo_method[algo_name](algo_resfile, '_' + algo_name)
            del algo_res['Length_' + algo_name]
            self.all_res = self.all_res.join(algo_res)
            self.algo_fields[algo_name] = [x[:x.find('_')] for x in algo_res.columns]

        self.build_bar_chart()

    def build_bar_chart(self):
        for field in self.get_algo_fields_common():
            self.bar[field] = os.path.dirname(os.path.realpath(__file__ + "/../../")) + '/static/img/%s_bar.png' % (field)

            all_algo = self.get_all_algos()

            values = []
            for algo in all_algo:
                fname = self._convert_col('%s_%s' % (field, algo))
                if algo == 'truth' and field == 'TPM':
                    values.append(self.all_res.ix[:, fname].sum() * 1000000)
                else:
                    values.append(self.all_res.ix[:, fname].sum())

            index = np.arange(len(all_algo))
            bar_width = 0.35
            plt.bar(index, values, bar_width,
                 alpha=0.4,
                 color='b',
                 label=field)
            plt.xticks(index + bar_width / 2.0, all_algo)
            plt.xlabel('Algorithms')
            plt.ylabel(field)
            plt.savefig(self.bar[field])
            plt.clf()

    def get_bar_chart(self, field):
        return self.bar[field]

    def get_stat_fields(self):
        return self.stat_field

    def get_all_algos(self):
        return self.algos

    def get_algo_fields(self, algo):
        return self.algo_fields[algo]

    def get_algo_fields_common(self):
        return [x for x in self.algo_fields['sailfish'] if x != 'Length' and x in self.algo_fields['kallisto'] and x in self.algo_fields['rsem']]

    def update_truth(self, truth_file):
        self.algo_res['truth'] = truth_file
        self.load_data()

    def get_fields(self):
        assert self.all_res is not None
        return self.all_res.columns

    def _convert_col(self, col):
        if col.endswith('_truth'):
            if col.startswith('NumReads'):
                return 'SeqNum_truth'
            elif col.startswith('TPM'):
                return 'LibFrac_truth'
        return col

    def _sample(self, names, x, y):
        lenth = len(names)
        x_avg = sum(x) * 1.0 / lenth
        y_avg = sum(y) * 1.0 / lenth
        dist = [distance(x_avg, y_avg, x[i], y[i]) for i in xrange(lenth)]
        dist.sort()
        p = dist[-500]
        res_name = []
        res_x = []
        res_y = []
        for i in xrange(lenth):
            if distance(x_avg, y_avg, x[i], y[i]) > p:
                res_name.append(names[i])
                res_x.append(x[i])
                res_y.append(y[i])
            else:
                if random.randint(0, 100) < 5:
                    res_name.append(names[i])
                    res_x.append(x[i])
                    res_y.append(y[i])

        return res_name, res_x, res_y
        # return names[:1000], x[:1000], y[:1000]

    def get_2col(self, colx, coly): # TODO: add name
        colx = self._convert_col(colx)
        coly = self._convert_col(coly)

        print 'debug to print col:', colx, coly
        assert colx in self.all_res.columns
        assert coly in self.all_res.columns
        names = np.array(self.all_res.index, dtype=str) # self.all_res.ix[:, 'Name'], dtype=str)
        x = np.array(self.all_res.ix[:, colx], dtype=float)
        y = np.array(self.all_res.ix[:, coly], dtype=float)

        if colx.startswith('TPM') or coly.startswith('TPM'):
            if colx == 'LibFrac_truth':
                x = x * 1000000
            elif coly == 'LibFrac_truth':
                y = y * 1000000

        names, x, y = self._sample(names, x, y)
        print 'final length is:', len(names)
        return names, x, y

    def get_2col_wlinear(self, colx, coly):
        names, x, y = self.get_2col(colx, coly)
        p1, p2, err = reg.get_regression(x, y)
        return names, x, y, p1, p2, err

    def get_matrix(self):
        matrix = []
        for algo_name in self.algos:
            if algo_name == 'truth':
                continue
            corr, tpef, tpme, mard, wmard = self._calculate_submatrix('SeqNum_truth', 'NumReads_%s' % (algo_name))
            matrix.append({'':algo_name, 'spearman':corr, 'TPEF':round(tpef, 2), 'TPME':round(tpme, 2), 'MARD':round(mard, 2), 'wMARD':round(wmard, 2)})
        return matrix

    def plot_scatter(self, colx, coly, figname, reg = False):
        self.all_res.plot(kind='scatter', x=colx, y=coly)
        if reg:
            names, x, y, p1, p2, err = self.get_2col_wlinear(colx, coly)
            print p1, p2
            plt.plot([p1[0], p2[0]], [p1[1], p2[1]])
        plt.savefig(figname)
        plt.clf()

    def _calculate_submatrix(self, nmx, nmy):
        # st[nmx].corr(st[nmy], method = "spearman")

        x = np.array(self.all_res.ix[:, nmx], dtype=float)
        y = np.array(self.all_res.ix[:, nmy], dtype=float)
        x = x / 2

        corr = scipy.stats.spearmanr(x, y)[0]

        num_xplus = 0
        sum_eii = 0
        reis = []
        sum_ardi = 0
        sum_wmard = 0

        for xi, yi in zip(x, y):
            ardi = 0 if xi + yi == 0 else abs(xi - yi) / (0.5 * (xi + yi))
            sum_ardi += ardi
            wmard = 0 if ardi == 0 else ardi * math.log(max(xi, yi), 2)
            sum_wmard += wmard

            if xi == 0:
                continue

            num_xplus += 1
            rei = (xi - yi) * 1.0 / xi
            # print xi, yi, rei
            eii = 1 if abs(rei) > 0.1 else 0

            sum_eii += eii
            reis.append(rei)

        tpef = sum_eii * 1.0 / num_xplus
        tpme = median(reis)
        mard = sum_ardi * 1.0 / len(x)
        wmard = sum_wmard * 1.0 / len(x)
        return corr, tpef, tpme, mard, wmard


if __name__ == '__main__':
    datas = DataAnalyzor()
    datas.load_data()

    matrix = datas.get_matrix()
    print matrix

    names, x, y = datas.get_2col('GC_Content', 'ExpFrac_truth')
    print names, x, y

    print 'sailfish algo fields:', datas.get_algo_fields('sailfish')
    print 'common fields:', datas.get_algo_fields_common()
    print 'stat fields:', datas.get_stat_fields()
    print 'bar_chart:', datas.get_bar_chart('NumReads')

    names, x, y = datas.get_2col('TPM_truth', 'TPM_sailfish')
    names, x, y = datas.get_2col('ExpFrac_truth', 'TPM_sailfish')

    datas.plot_scatter('TPM_kallisto', 'TPM_sailfish', 'a.png', True)