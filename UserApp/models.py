from django.db import models

class Category_Db(models.Model):
    Category_Name = models.CharField(max_length=100,blank=True,null=True)
    Description  = models.CharField(max_length=100,blank=True,null=True)
    Category_Image = models.ImageField(upload_to="Category",blank=True,null=True)

class Product_Db(models.Model):
    Product_Category = models.CharField(max_length=100,blank=True,null=True)
    Product_Name = models.CharField(max_length=100,blank=True,null=True)
    Quantity = models.IntegerField(blank=True,null=True)
    MRP = models.IntegerField(blank=True,null=True)
    Description = models.CharField(max_length=100,blank=True,null=True)
    Country_Orgin = models.CharField(max_length=100,blank=True,null=True)
    Manufactured_By = models.CharField(max_length=100,blank=True,null=True)
    P_Image1 = models.ImageField(upload_to="Product",blank=True,null=True)
    P_Image2 = models.ImageField(upload_to="Product",blank=True,null=True)
    P_Image3 = models.ImageField(upload_to="Product",blank=True,null=True)

# Create your models here.
