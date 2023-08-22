from django.shortcuts import render,redirect
from .models import *
from .form import *
from django.core import serializers
from django.http import JsonResponse
import json
# Create your views here.

def homepage(request):
    salesform=SalesForm()
    salesData = Sales.objects.all()
    sales_json = serializers.serialize('json', salesData)
    sales_json=json.loads(sales_json)

    label = [ 'jan',
        'feb',
        'march' ]
    data = [ 1,100,5000]
    label=json.dumps(label)
    data=json.dumps(data)
    context={ 
        'sales_json':sales_json,
        'salesData':salesData,
        'salesform':salesform,
        'label':label,
        'j_data':data,
    }

    if request.method=='POST':
        salesform=SalesForm(request.POST)
        print("trying saved")

        salesform.is_valid
        salesform.save()
        print("saved")
        return redirect('homepage')

    return render(request,'dashboard.html',context)