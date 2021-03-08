from django.shortcuts import render
from task.models import SortedData as modelSort
from task.sort import *
from django.core.files.storage import FileSystemStorage
import os
from sort.settings import MEDIA_ROOT
import datetime as dt


def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        kind = request.POST['sorting']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        file = os.path.join(MEDIA_ROOT,uploaded_file.name)
        model = modelSort()
        if kind == 'buble':
            a = BubleSort()
            model.kind = kind
            model.beforesort = a.getdata(file)
            model.aftersort = a.sort(a.getdata(file))
            model.exectime = deltas['BubleSort']
            model.timestart = starts['BubleSort']
            model.save()




    return render(request, 'task/index.html')

