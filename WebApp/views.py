
from django.shortcuts import render,redirect
from UserApp.models import Product_Db,Category_Db
from WebApp.models import Contact_Db,Login_Db,Cart_Db,Order_Db
from django.contrib import messages
import razorpay

def home(request):
    cat = Category_Db.objects.all()
    name = request.session.get("Login_Name")
    count = Cart_Db.objects.filter(Holder = name).count()
    return render(request,"Home.html",{"cat":cat,"count":count})
def product_page(request):
    product = Product_Db.objects.all()
    name = request.session.get("Login_Name")
    count = Cart_Db.objects.filter(Holder = name).count()
    return render(request,"Product.html",{"product":product,"count":count})
def about_us(request):
    name = request.session.get("Login_Name")
    count = Cart_Db.objects.filter(Holder = name).count()
    return render(request,"About_Us.html",{"count":count})
def contact(request):
    name = request.session.get("Login_Name")
    count = Cart_Db.objects.filter(Holder = name).count()
    return render(request,"Contact.html",{"count":count})
def save_contact(request):
    if request.method == 'POST':
        a = request.POST.get("fname")
        b = request.POST.get("lname")
        c = request.POST.get("email")
        d = request.POST.get("message")

        obj = Contact_Db(First_Name = a,Last_Name = b,Email = c,Message = d)
        obj.save()
        return redirect(contact)
def product_filter(request,cat_name):
    name = request.session.get("Login_Name")
    count = Cart_Db.objects.filter(Holder = name).count()
    data = Product_Db.objects.filter(Product_Category = cat_name)
    name = cat_name
    return render(request,"Product_Filter.html",{"data":data,"name":name,"count":count})
def single_product(request,pro_id):
    data = Product_Db.objects.get(id = pro_id)
    name = Product_Db.objects.get(id = pro_id).Product_Name
    name = request.session.get("Login_Name")
    count = Cart_Db.objects.filter(Holder = name).count()
    return render(request,"Single_Product.html",{"data":data,"name":name,"count":count})
def user_signup(req):
    return render(req,"User_SignUp.html")
def user_signin(req):
    return render(req,"User_SignIn.html")
def save_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        pass_word = request.POST.get("pass")
        re_pass = request.POST.get("re_pass")

        obj = Login_Db(Login_Name = name,Login_Email = email,Login_Mobile = mobile,
                       Login_Password = pass_word,Login_Repassword = re_pass)
        if Login_Db.objects.filter(Login_Name = name).exists():
            messages.warning(request,"Username already exists..!")
            return redirect(user_signup)
        elif Login_Db.objects.filter(Login_Email = email).exists():
            messages.warning(request,"Email Address already exists..!")
            return redirect(user_signup)
        obj.save()
        return redirect(user_signin)
def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get("your_name")
        user_password = request.POST.get("your_pass")

        if Login_Db.objects.filter(Login_Name = user_name,Login_Password = user_password).exists():
            request.session["Login_Name"] = user_name
            request.session["Login_Password"] = user_password
            messages.success(request,"Welcome!")
            return redirect(home)
        else:
            messages.error(request,"Incorrect Password!")
            return redirect(user_signin)

    else:
        return redirect(user_signin)
def user_logout(request):
    del request.session["Login_Name"]
    del request.session["Login_Password"]
    messages.warning(request,"You are Logged Out!")
    return redirect(user_signin)


# Create your views here.
def save_cart(request):
    if request.method == 'POST':
        quantity = request.POST.get("quantity")
        total = request.POST.get("total")
        price = request.POST.get("price")
        user = request.POST.get("user_name")
        pname = request.POST.get("pro_name")
        pimage = request.POST.get("p_img")

        # Proceed with saving
        obj = Cart_Db(Quantity=quantity, Total_Price=total, Price=price, Holder=user, P_Name=pname,P_Image = pimage)
        obj.save()
        return redirect(home)

def cart(request):
    name = request.session.get("Login_Name")
    count = Cart_Db.objects.filter(Holder = name).count()
    name = request.session.get("Login_Name")
    data = Cart_Db.objects.filter(Holder = name)
    sum = 0
    for x in data:
        sum = sum+x.Total_Price
    if sum>50000:
        Shipping = 100
    else:
        Shipping = 250
    total_amount = Shipping + sum
    return render(request,"Cart.html",{"data":data,"sum":sum,"Shipping":Shipping,"total_amount":total_amount,"count":count})
def delete_cart(request,ca_id):
    data = Cart_Db.objects.filter(id = ca_id)
    data.delete()
    return redirect(cart)
def check_out(request):
    name = request.session.get("Login_Name")
    count = Cart_Db.objects.filter(Holder = name).count()
    name = request.session.get("Login_Name")
    cart = Cart_Db.objects.filter(Holder = name)
    sum = 0
    for x in cart:
        sum = sum+x.Total_Price
    if sum>50000:
        Shipping = 100
    else:
        Shipping = 250
    total_amount = Shipping + sum
    return render(request,"Checkout.html",{"cart":cart,"sum":sum,"Shipping":Shipping,"total_amount":total_amount,
                                           "name":name,"count":count})
def save_order(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        place = request.POST.get("place")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        total = request.POST.get("total")
        state = request.POST.get("state")
        code = request.POST.get("code")
        order = request.POST.get("order")

        obj = Order_Db(Name = name,Email = email,Place = place,Mobile = mobile,Address = address,Total = total,
                       State = state,Postal = code,Order = order)
        obj.save()
        return redirect(payment)

def payment(request):
    customer = Order_Db.objects.order_by("-id").first()

    payy = customer.Total

    amount = int(payy*100)

    pay_str = str(amount)
    for i in pay_str:
        print(i)
    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_C7ztg4x7jmjoLs', 'z7WOqqTsGgHiRHYE1NSptK3m'))
        payment = client.order.create({"amount":amount,"currency":order_currency})
    return render(request,"payment.html",{"customer":customer,"pay_str":pay_str})

