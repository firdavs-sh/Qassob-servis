from distutils.command.upload import upload
from django.db import models

class  Qoy (models.Model):
    rasm=models.FileField(upload_to='media/',null=True)
    goshtn= models.CharField(max_length=200)
    gosht=models.CharField(max_length=200)
    narxi=models.CharField(max_length=200)
    telefon=models.CharField(max_length=200)
    def __str__(self) :
        return str(self.goshtn)

class  Mol (models.Model):
    rasm=models.FileField(upload_to='media/',null=True)
    goshtn= models.CharField(max_length=200)
    gosht=models.CharField(max_length=200)
    narxi=models.CharField(max_length=200)
    telefon=models.CharField(max_length=200)
    def __str__(self) :
        return str(self.goshtn)

class  Tuya (models.Model):
    rasm=models.FileField(upload_to='media/',null=True)
    goshtn= models.CharField(max_length=200)
    gosht=models.CharField(max_length=200)
    narxi=models.CharField(max_length=200)
    telefon=models.CharField(max_length=200)
    def __str__(self) :
        return str(self.goshtn)

class  Quyon (models.Model):
    rasm=models.FileField(upload_to='media/',null=True)
    goshtn= models.CharField(max_length=200)
    gosht=models.CharField(max_length=200)
    narxi=models.CharField(max_length=200)
    telefon=models.CharField(max_length=200)
    def __str__(self) :
        return str(self.goshtn)

class  Tovuq (models.Model):
    rasm=models.FileField(upload_to='media/',null=True)
    goshtn= models.CharField(max_length=200)
    gosht=models.CharField(max_length=200)
    narxi=models.CharField(max_length=200)
    telefon=models.CharField(max_length=200)
    def __str__(self) :
        return str(self.goshtn)

class  Ot (models.Model):
    rasm=models.FileField(upload_to='media/',null=True)
    goshtn= models.CharField(max_length=200)
    gosht=models.CharField(max_length=200)
    narxi=models.CharField(max_length=200)
    telefon=models.CharField(max_length=200)
    def __str__(self) :
        return str(self.goshtn)

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