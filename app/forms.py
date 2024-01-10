from django import forms
from django.core import validators

def validate_for_name(data):
    if data.lower().startswith('s'):
        raise forms.ValidationError("Name cannot start with a 's'")

def validate_for_password(data):
    if len(data)<=5:
        raise forms.ValidationError("Password must be more than 5 characters long.")

class Student_Form(forms.Form):
    Sname=forms.CharField(validators=[validate_for_name,validators.MinLengthValidator(5)])
    Password=forms.CharField(widget=forms.PasswordInput,validators=[validate_for_password])
    Reenterpassword=forms.CharField(widget=forms.PasswordInput,validators=[validate_for_password])
    Email=forms.EmailField()
    ReenterEmail=forms.EmailField()
    Sdateofbirth=forms.DateTimeField()
    Squalification_10=forms.CharField()
    Saggregrate_10=forms.IntegerField()
    Squalification_12=forms.CharField()
    Saggregrate_12=forms.IntegerField()
    Squalification_Degree=forms.CharField()
    Saggregrate_Degree=forms.IntegerField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        Pa=self.cleaned_data['Password']
        RPa=self.cleaned_data['Reenterpassword']
        if Pa!=RPa:
            raise forms.ValidationError('Both are not match')
        E=self.cleaned_data['Email']
        RE=self.cleaned_data['ReenterEmail']
        if E!=RE:
            raise forms.ValidationError('Email doesnot match')
        
    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('Bot')