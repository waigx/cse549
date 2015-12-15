from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datautils.query import DataAnalyzor
import json


'''
def import_data(request):
    file2db(data_path+data_file_dict["kallisto"], KallistoEntryIDs, KallistoAttributes, KallistoData)
#    file2db(data_path+data_file_dict["rsem"], RsemEntryIDs, RsemAttributes, RsemData)
#   file2db(data_path+data_file_dict["sailfish"], SailfishEntryIDs, SailfishAttributes, SailfishData)
    return HttpResponse("<h1>Import Success</h1>")




def test(request):
    tpm_lst = dbop.get_col_in_db("TPM", SailfishEntryIDs, SailfishAttributes, SailfishData).values()
    nr_lst = dbop.get_col_in_db("NumReads", SailfishEntryIDs, SailfishAttributes, SailfishData).values()
    id_lst = list(SailfishEntryIDs.objects.all().values())
    entries = zip(id_lst, tpm_lst, nr_lst)
    result = [(e[0]['entry_id'], e[1]['value'], e[2]['value']) for e in entries]
    print len(result)
    return HttpResponse("<h1>test page</h1>")
'''

da = DataAnalyzor()


def main_view(request):
    da.load_data()
    return HttpResponse("<head><script language=\"javascript\"> "
                        "window.location.href = \"/static/index.html\""
                        "</script></head>"
                        "<body>Data Loaded</body>")


def get_data(request):
    if request.method == "POST":
        json_obj = {}
        request_body = json.loads(request.body)
        if request_body['type'] == 'algorithm':
            json_obj['data'] = []
            algs = da.get_all_algos()
            try:
                for alg in algs:
                    if request_body['pictype'] == '1':
                        alg_field = list(da.get_algo_fields(alg))
                    else:
                        alg_field = list(da.get_algo_fields_common())
                        alg_field += list(da.get_stat_fields()) + list(da.get_truth_fields())
                    json_obj['data'] += [{"alg":alg, "attrs":alg_field}]
            except:
                return JsonResponse(json_obj)

        elif request_body['type'] == 'data':
            except_lst = list(da.get_stat_fields()) + list(da.get_truth_fields())
            try:
                query_col1 = request_body['x'] if request_body['x'] in except_lst else request_body['x'] + "_" + request_body['alg']
                query_col2 = request_body['y'] if request_body['y'] in except_lst else request_body['y'] + "_" + request_body['alg']
                raw_data = da.get_2col(query_col1, query_col2)
            except:
                return JsonResponse(json_obj)
            obj_data_len = len(raw_data[0])
            obj_data = [None] * obj_data_len
            for i in xrange(obj_data_len):
                obj_data[i] = {
                    'name': raw_data[0][i],
                    query_col1: raw_data[1][i],
                    query_col2: raw_data[2][i]
                }
            json_obj['data'] = obj_data

        elif request_body['type'] == 'data1':
            except_lst = list(da.get_stat_fields()) + list(da.get_truth_fields())
            try:
                query_col1 = request_body['attr1'] if request_body['attr1'] in except_lst else request_body['attr1'] + "_" + request_body['alg1']
                query_col2 = request_body['attr2'] if request_body['attr2'] in except_lst else request_body['attr2'] + "_" + request_body['alg2']
                raw_data = da.get_2col_wlinear(query_col1, query_col2)
            except:
                return JsonResponse(json_obj)
            obj_data_len = len(raw_data[0])
            obj_data = [None] * obj_data_len
            for i in xrange(obj_data_len):
                obj_data[i] = {
                    'name': raw_data[0][i],
                    query_col1: raw_data[1][i],
                    query_col2: raw_data[2][i]
                }
            json_obj['data'] = obj_data
            json_obj['regression'] = {
                'p1': {'x':raw_data[3][0], 'y':raw_data[3][1]},
                'p2': {'x':raw_data[4][0], 'y':raw_data[4][1]},
                'error': list(raw_data[5])[0]}
        return JsonResponse(json_obj)
    else:
        return HttpResponse("Access method must be POST.")


def get_matrix(request):
    json_obj = {'data': da.get_matrix()}
    return JsonResponse(json_obj)


def get_common_attr(request):
    json_obj = {'data': da.get_algo_fields_common()}
    return JsonResponse(json_obj)


def test(request):
    print da.get_2col_wlinear('TPM_sailfish', 'TPM_rsem')
    return HttpResponse("Access method must be POST.")

