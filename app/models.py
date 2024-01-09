from django.db import models

# Create your models here.


class Student_model(models.Model):

    Sname=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Reenterpassword=models.CharField(max_length=100)
    Email=models.EmailField()
    ReenterEmail=models.EmailField()
    Sdateofbirth=models.DateTimeField()
    Squalification_10=models.CharField(max_length=100)
    Saggregrate_10=models.IntegerField()
    Squalification_12=models.CharField(max_length=100)
    Saggregrate_12=models.IntegerField()
    Squalification_Degree=models.CharField(max_length=100)
    Saggregrate_Degree=models.IntegerField()

    def __str__(self):
        return self.Sname




    
