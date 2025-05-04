from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('collections', views.collections, name='collections'),
    path('collections/<str:name>', views.collectionsView, name='collections'),
    path('collections/<str:cname>/<str:pname>', views.product_details, name='product_details'),
    path('addtocart', views.add_to_cart, name='addtocart'),
    path('cart', views.cart, name="cart"),
    path('remove_cart/<str:cid>', views.remove_cart, name="remove_cart"),
    path('orders', views.orders, name="orders"),
    path('track', views.tracking, name="track"),
    path('place_order', views.place_order, name="place_order"),
    path('billing', views.billing, name="billing"),
]
