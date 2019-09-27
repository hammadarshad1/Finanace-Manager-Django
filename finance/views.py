from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DeleteView
from . import models
from django.contrib import messages



# Create your views here.
def home(request):
    cash = models.Cash.objects.all()
    check = models.Check.objects.all()
    if request.method == "POST":
        cash = serializers.serialize('json',cash)
        check = serializers.serialize('json',check)
        return JsonResponse({"cash":cash, "check":check})
    return render(request, 'finance/home.html')

def about(request):
    return render(request, 'finance/about.html',{'title':'About'})

def delca(request):
    cash = models.Cash.objects.all()
    return render(request, 'finance/delca.html',{'cash':cash})

def delch(request):
    check = models.Check.objects.all()
    return render(request, 'finance/delch.html',{'check':check})

class Cash(CreateView):
    model = models.Cash
    template_name = 'finance/cash.html'
    fields = ['title', 'Cash']

class Check(CreateView):
    model = models.Check
    template_name = 'finance/check.html'
    fields = ['title', 'Check', 'Account_number']

class CashDelete(DeleteView):
    model=models.Cash
    template_name='finance/cash_delete.html'
    success_url = '/cash/del'

class CheckDelete(DeleteView):
    model=models.Check
    template_name='finance/check_delete.html'
    success_url = '/check/del'
