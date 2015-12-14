from django.shortcuts import render
from django.http import HttpResponse
from utils.file2db import file2db
import utils.dboperate as dbop
from django.http import JsonResponse
from models import *
import json

data_path = "/Users/waigx/Downloads/cse509/"
data_file_dict = {"kallisto": "kallisto.data",
                  "rsem": "r.data",
                  "sailfish": "sailfish.data"}


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
