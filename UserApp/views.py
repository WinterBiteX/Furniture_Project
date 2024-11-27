from django.shortcuts import render,redirect
from UserApp.models import Category_Db,Product_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import Contact_Db
from django.contrib import messages



def index_page(req):
    return render(req,"index.html")

def add_category(req):
    return render(req,"Add_Category.html")
def save_category(request):
    if request.method == 'POST':
        a = request.POST.get("cname")
        b = request.POST.get("description")
        c = request.FILES['c_img']

        obj = Category_Db(Category_Name = a,Description = b,Category_Image = c)
        obj.save()
        messages.success(request,"Category Saved.....!")
        return redirect(add_category)
def display_category(req):
    data = Category_Db.objects.all()
    return render(req,"Display_Category.html",{"data":data})
def edit_category(req,cat_id):
    data = Category_Db.objects.get(id = cat_id)
    return render(req,"Edit_Category.html",{"data":data})
def update_category(request,cat_id):
    if request.method == 'POST':
        cn = request.POST.get("cname")
        desc = request.POST.get("description")

        try:
            img = request.FILES['c_img']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Category_Db.objects.get(id = cat_id).Category_Image
        Category_Db.objects.filter(id = cat_id).update(Category_Name = cn,Description = desc,Category_Image = file)
        messages.success(request,"Category Successfully Edited.....!")
        return redirect(display_category)
def delete_category(request,cat_id):
    data = Category_Db.objects.filter(id = cat_id)
    data.delete()
    messages.warning(request,"Category Successfully Deleted.....!")
    return redirect(display_category)

def add_product(req):
    data = Category_Db.objects.all()
    return render(req,"Add_Product.html",{"data":data})
def save_product(request):
    if request.method == 'POST':
        a = request.POST.get("pcategory")
        b = request.POST.get("pname")
        c = request.POST.get("quantity")
        d = request.POST.get("mrp")
        e = request.POST.get("description")
        f = request.POST.get("orgin")
        g = request.POST.get("manufacture")
        h = request.FILES['img1']
        i = request.FILES['img2']
        j = request.FILES['img3']

        obj = Product_Db(Product_Category = a,Product_Name = b,Quantity = c,MRP = d,Description = e,Country_Orgin = f,
                         Manufactured_By = g,P_Image1 = h,P_Image2 = i,P_Image3 = j)
        obj.save()
        messages.success(request,"Product Saved.....!")
        return redirect(add_product)

def display_product(req):
    data = Product_Db.objects.all()
    return render(req,"Display_Product.html",{"data":data})
def delete_product(request,pro_id):
    data = Product_Db.objects.filter(id = pro_id)
    data.delete()
    messages.warning(request,"Product Successfully Deleted.....!")
    return redirect(display_product)
def edit_product(req,pro_id):
    cat = Category_Db.objects.all()
    data = Product_Db.objects.get(id = pro_id)
    return render(req,"Edit_Product.html",{"data":data,"cat":cat})
def update_product(request,pro_id):
    if request.method == 'POST':
        a = request.POST.get("pcategory")
        b = request.POST.get("pname")
        c = request.POST.get("quantity")
        d = request.POST.get("mrp")
        e = request.POST.get("description")
        f = request.POST.get("orgin")
        g = request.POST.get("manufacture")

        try:
            img1 = request.FILES['img1']
            fs1 = FileSystemStorage()
            file1 = fs1.save(img1.name,img1)
        except MultiValueDictKeyError:
            file1 = Product_Db.objects.get(id = pro_id).P_Image1
        try:
            img2 = request.FILES['img2']
            fs2 = FileSystemStorage()
            file2 = fs2.save(img2.name,img2)
        except MultiValueDictKeyError:
            file2 = Product_Db.objects.get(id = pro_id).P_Image2

        try:
            img3 = request.FILES['img3']
            fs3 = FileSystemStorage()
            file3 = fs3.save(img3.name,img3)
        except MultiValueDictKeyError:
            file3 = Product_Db.objects.get(id = pro_id).P_Image3

        Product_Db.objects.filter(id = pro_id).update(Product_Category = a,Product_Name = b,Quantity = c,MRP = d,Description = e,Country_Orgin = f,
                         Manufactured_By = g,P_Image1 = file1,P_Image2 = file2,P_Image3 = file3)
        messages.success(request,"Product Successfully Edited.....!")
        return redirect(display_product)

def admin_login(req):
    return render(req,"Admin_Login.html")
def admin(request):
    if request.method == "POST":
        us = request.POST.get("email-username")
        ps = request.POST.get("password")

        if User.objects.filter(username__contains = us).exists():
            user = authenticate(username = us,password = ps)

            if user is not None:
                login(request,user)
                request.session['username'] = us
                request.session['password'] = ps
                messages.success(request,"Welcome!")
                return redirect(index_page)
            else:
                messages.error(request,"Incorrect Password!")
                return redirect(admin_login)
        else:
            messages.warning(request,"Username Incorrect!")
            return redirect(admin_login)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.warning(request,"You are logging out!")
    return redirect(admin_login)

def display_contact(req):
    data = Contact_Db.objects.all()
    return render(req,"Display_Contact.html",{"data":data})
def delete_contact(req,con_id):
    data = Contact_Db.objects.filter(id = con_id)
    data.delete()
    return redirect(display_contact)









# Create your views here.
