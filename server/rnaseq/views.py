from django.shortcuts import render
from django.http import HttpResponse
from utils.file2db import file2db
from django.http import JsonResponse
from models import *
import json

data_path = "/Users/waigx/Downloads/cse509/"
data_file_dict = {"kallisto": "kallisto.data",
                  "rsem": "rsem.data",
                  "sailfish": "sailfish.data"}


def import_data(request):
    file2db(data_path+data_file_dict["kallisto"], KallistoEntryIDs, KallistoAttributes, KallistoData)
    file2db(data_path+data_file_dict["rsem"], RsemEntryIDs, RsemAttributes, RsemData)
    file2db(data_path+data_file_dict["sailfish"], SailfishEntryIDs, SailfishAttributes, SailfishData)
    return HttpResponse("<h1>Import Success</h1>")
