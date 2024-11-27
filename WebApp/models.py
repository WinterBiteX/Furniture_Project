from django.db import models

class Contact_Db(models.Model):
    First_Name = models.CharField(max_length=100,null=True,blank=True)
    Last_Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Message = models.CharField(max_length=100,null=True,blank=True)

class Login_Db(models.Model):
    Login_Name = models.CharField(max_length=100,null=True,blank=True)
    Login_Email = models.EmailField(null=True,blank=True)
    Login_Mobile = models.IntegerField(null=True,blank=True)
    Login_Password = models.CharField(max_length=100,null=True,blank=True)
    Login_Repassword = models.CharField(max_length=100,null=True,blank=True)


# Create your models here.
class Cart_Db(models.Model):
    Quantity = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Holder = models.CharField(max_length=100,null=True,blank=True)
    P_Name = models.CharField(max_length=200,null=True,blank=True)
    P_Image = models.CharField(max_length=255, blank=True, null=True)
class Order_Db(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Address = models.CharField(max_length=200,null=True,blank=True)
    Total = models.IntegerField(null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    Postal = models.IntegerField(null=True,blank=True)
    Order = models.TextField(null=True,blank=True)
