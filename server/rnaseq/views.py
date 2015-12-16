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

def _get_column(colname, alg_name, da):
    return colname if colname in da.get_stat_fields() \
            else colname + "_" + alg_name

def _get_obj_data(da, request_body, alg, add_alg = False):
    query_col1 = _get_column(request_body['x'], request_body[alg], da)
    query_col2 = _get_column(request_body['y'], request_body[alg], da)

    names, xvalues, yvalues = da.get_2col(query_col1, query_col2)

    if add_alg:
        obj_data = [{'name':names[x], request_body['x']:xvalues[x], request_body['y']:yvalues[x], \
                    'alg':request_body[alg]} \
                    for x in xrange(len(names))]
    else:
        obj_data = [{'name':names[x], request_body['x']:xvalues[x], request_body['y']:yvalues[x]} \
                    for x in xrange(len(names))]
    return obj_data

def _get_obj_data_2(da, request_body):
    obj_data1 = _get_obj_data(da, request_body, 'alg1')
    obj_data2 = _get_obj_data(da, request_body, 'alg2')
    return obj_data1 + obj_data2

def _get_obj_data_3(da, request_body):
    query_col1 = _get_column(request_body['attr1'], request_body['alg1'], da)
    query_col2 = _get_column(request_body['attr2'], request_body['alg2'], da)

    names, xvalues, yvalues, p1, p2, error = da.get_2col_wlinear(query_col1, query_col2)
    obj_data = [{'name':names[x], query_col1:xvalues[x], query_col2:yvalues[x]} \
               for x in xrange(len(names))]
    if isinstance(error, list) or isinstance(error, tuple):
        error = error[0]
    return obj_data, p1, p2, error

def get_data(request):
    if request.method == "POST":
        json_obj = {}
        request_body = json.loads(request.body)
        print request_body
        if request_body['type'] == 'algorithm':
            json_obj['data'] = []
            algs = da.get_all_algos()
            try:
                for alg in algs:
                    if request_body['pictype'] == '1':
                        alg_field = list(da.get_algo_fields(alg))
                        alg_field += list(da.get_stat_fields())
                    elif request_body['pictype'] == '2':
                        alg_field = list(da.get_algo_fields_common())
                        alg_field += list(da.get_stat_fields())
                    else:
                        alg_field = list(da.get_algo_fields_common())
                    json_obj['data'] += [{"alg":alg, "attrs":alg_field}]
            except:
                return JsonResponse(json_obj)
        elif request_body['type'] == 'data':
            if request_body['pictype'] == '1':
                try:
                   json_obj['data'] = _get_obj_data(da, request_body, 'alg')
                except:
                    return JsonResponse(json_obj)
            elif request_body['pictype'] == '2':
                try:
                    json_obj['data'] = _get_obj_data_2(da, request_body)
                except:
                    return JsonResponse(json_obj)
        elif request_body['type'] == 'data1':
            try:
                obj_data, p1, p2, error = _get_obj_data_3(da, request_body)
                json_obj['data'] = obj_data
                json_obj['regression'] = {
                    'p1': {'x':p1[0], 'y':p1[1]},
                    'p2': {'x':p2[0], 'y':p2[1]},
                    'error': error}
            except:
                return JsonResponse(json_obj)
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

