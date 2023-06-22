from distutils.command.upload import upload
from django.db import models



class  Register(models.Model):
    ism=models.CharField(max_length=200,null=True)
    Familiya=models.CharField(max_length=200,null=True)   
    Email=models.EmailField(max_length=200,null=True)
    telefon=models.CharField(max_length=200,null=True)
    taklif=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.telefon)

class Mt(models.Model):
    tel=models.CharField(max_length=200)