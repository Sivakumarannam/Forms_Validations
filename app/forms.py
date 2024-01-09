from django import forms

def validate_for_name(data):
    if data.lower().startswith('s'):
        raise forms.ValidationError("Name cannot start with a 's'")

def validate_for_password(data):
    if len(data)<=5:
        raise forms.ValidationError("Password must be more than 5 characters long.")

class Student_Form(forms.Form):
    Sname=forms.CharField(validators=[validate_for_name])
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

    def clean(self):
        Pa=self.cleaned_data['Password']
        RPa=self.cleaned_data['Reenterpassword']
        if Pa!=RPa:
            raise forms.ValidationError('Both are not match')
        E=self.cleaned_data['Email']
        RE=self.cleaned_data['ReenterEmail']
        if E!=RE:
            raise forms.ValidationError('Email doesnot match')