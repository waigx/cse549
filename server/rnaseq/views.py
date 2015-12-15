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
    return HttpResponse("<h1>Data Loaded.</h1>")


def get_data(request):
    if request.method == "POST":
        json_obj = {}
        request_body = json.loads(request.body)
        if request_body['type'] == 'algorithm':
            json_obj['data'] = []
            algs = da.get_all_algos()
            for alg in algs:
                alg_field = da.get_algo_fields(alg)
                json_obj['data'] += [{"alg":alg, "attrs":alg_field}]
        elif request_body['type'] == 'data':
            try:
                raw_data = da.get_2col(request_body['x'] + "_" + request_body['alg'], request_body['y'] + "_" + request_body['alg'])
            except:
                return JsonResponse(json_obj)
            obj_data_len = len(raw_data[0])
            obj_data = [None] * obj_data_len
            for i in xrange(obj_data_len):
                obj_data[i] = {
                    'name': raw_data[0][i],
                    request_body['x'] + "_" + request_body['alg']: raw_data[1][i],
                    request_body['y'] + "_" + request_body['alg']: raw_data[2][i]
                }
            json_obj['data'] = obj_data
        elif request_body['type'] == 'data1':
            try:
                raw_data = da.get_2col(request_body['attr1'] + "_" + request_body['alg1'], request_body['attr2'] + "_" + request_body['alg2'])
            except:
                return JsonResponse(json_obj)
            obj_data_len = len(raw_data[0])
            obj_data = [None] * obj_data_len
            for i in xrange(obj_data_len):
                obj_data[i] = {
                    'name': raw_data[0][i],
                    request_body['attr1'] + "_" + request_body['alg1']: raw_data[1][i],
                    request_body['attr2'] + "_" + request_body['alg2']: raw_data[2][i]
                }
            json_obj['data'] = obj_data
        return JsonResponse(json_obj)
    else:
        return HttpResponse("Access method must be POST.")
