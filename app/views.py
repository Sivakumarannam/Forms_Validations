from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def create_studentform(request):
    STFO=Student_Form()
    d={'STFO':STFO}
    if request.method=='POST':
          STDO=Student_Form(request.POST)
          if STDO.is_valid():
                Sn=STDO.cleaned_data['Sname']
                P=STDO.cleaned_data['Password']
                RP=STDO.cleaned_data['Reenterpassword']
                E=STDO.cleaned_data['Email']
                RE=STDO.cleaned_data['ReenterEmail']
                Sd=STDO.cleaned_data['Sdateofbirth']
                Sq10=STDO.cleaned_data['Squalification_10']
                Sa10=STDO.cleaned_data['Saggregrate_10']
                Sq12=STDO.cleaned_data['Squalification_12']
                Sa12=STDO.cleaned_data['Saggregrate_12']
                Sqd=STDO.cleaned_data['Squalification_Degree']
                Sad=STDO.cleaned_data['Saggregrate_Degree']
                STF=Student_model.objects.get_or_create(Sname=Sn,Password=P,Reenterpassword=RP,Email=E,ReenterEmail=RE,Sdateofbirth=Sd,Squalification_10=Sq10,Saggregrate_10=Sa10,Squalification_12=Sq12,Saggregrate_12=Sa12,Squalification_Degree=Sqd,Saggregrate_Degree=Sad)[0]
                STF.save()
                return HttpResponse('Data can be created')
          else:
               return HttpResponse('Invalid Data')


            
    return render(request,'create_studentform.html',d)






