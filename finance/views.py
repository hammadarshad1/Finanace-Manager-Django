from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
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

class Cash(CreateView):
    model = models.Cash
    template_name = 'finance/cash.html'
    fields = ['title', 'Cash']

class Check(CreateView):
    model = models.Check
    template_name = 'finance/check.html'
    fields = ['title', 'Check', 'Account_number']
