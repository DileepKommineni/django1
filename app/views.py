# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .form import RegistrationForm
from django.shortcuts import render,get_object_or_404
from .models import Registration
from .form import RegistrationForm
from rest_framework import generics
from serializers import RegSerializer

# Create your views here.
def index(reqest):
    ''''
    if reqest.method == 'POST':
        form = RegistrationForm(reqest.POST)
        if form.is_valid():
          first_name = reqest.POST.get('first_name','')
          last_name = reqest.POST.get('last_name', '')
          cost_obj = Registration(first=first_name,last=last_name)
          cost_obj.save()
    args = {'form':form}
    '''
    queryset = Registration.objects.all()

    return render(reqest,'index.html',{"query":queryset})
def details(request):
    instance = get_object_or_404(Registration,id=7)
    return render(request,"details.html",{"i":instance})
def form(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
   # if request.method == 'POST':
    #    print request.POST.get('first')
    #    print request.POST.get('last')

    context = {
        'form':form,
    }
    return render(request,'form.html',context)

class RegList(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegSerializer