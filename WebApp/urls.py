from django.urls import path
from WebApp import views

urlpatterns = [
    path("home/",views.home,name = "home"),
    path("product_page/",views.product_page,name = "product_page"),
    path("about_us/",views.about_us,name = "about_us"),
    path("contact_us/",views.contact,name = "contact_us"),
    path("save_contact/",views.save_contact,name = "save_contact"),
    path("product_filter/<cat_name>/",views.product_filter,name="product_filter"),
    path("single_product/<int:pro_id>/",views.single_product,name="single_product"),
    path("user_signup/",views.user_signup,name="user_signup"),
    path("",views.user_signin,name="user_signin"),
    path("save_user/",views.save_user,name="save_user"),
    path("user_login/",views.user_login,name="user_login"),
    path("user_logout/",views.user_logout,name="user_logout"),
    path("save_cart/",views.save_cart,name="save_cart"),
    path("cart/",views.cart,name="cart"),
    path("delete_cart/<int:ca_id>/",views.delete_cart,name="delete_cart"),
    path("checkout/",views.check_out,name="checkout"),
    path("order/",views.save_order,name="order"),
    path("payment/",views.payment,name="payment")
]
