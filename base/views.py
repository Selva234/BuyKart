import json
from . models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from base.forms import CustomUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def home(request):
  products = Product.objects.filter(trending=1)
  return render(request, 'base/index.html', {'products': products})

def cart(request):
  if request.user.is_authenticated:
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'base/cart.html', {'cart': cart})
  else:
    return redirect('/')

def add_to_cart(request):
  if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data = json.load(request)
      product_qty = data['product_qty']
      product_id = data['pid']
      # print(request.user.id)
      product_status = Product.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user.id, product_id=product_id):
          return JsonResponse({'status': 'Product Already in Cart'}, status = 200)
        else:
          if product_status.quantity >= product_qty:
            Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
            return JsonResponse({'status': 'Product Added to the Cart'}, status = 200)
          else:
            return JsonResponse({'status': 'Product Stock Not Available'}, status = 200)
    else:
      return JsonResponse({'status': 'Login to Add Cart'}, status = 200)
  else:
    return JsonResponse({'status': 'Invalid Access'}, status = 200)


def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request, 'Logged out Successfully')
  return redirect('/')
    
def login_page(request):
  if request.user.is_authenticated:
    return redirect("/")
  else:
    if request.method == 'POST':
      name = request.POST.get('username')
      pwd = request.POST.get('password')
      user = authenticate(request, username = name, password = pwd)
      if user is not None:
        login(request, user)
        messages.success(request, 'Logged in Successfully')
        return redirect('/')
      else:
        messages.error(request, 'Invalid User Name and Password')
        return redirect('/login')
    return render(request, 'base/login.html')


def register(request):
  form = CustomUserForm()
  if request.method == 'POST':
    form = CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Registration Success You can login now..!')
      return redirect('login')
  return render(request, 'base/register.html', {'form': form})


def collections(request):
  category = Category.objects.filter(status = 0)
  return render(request, 'base/collections.html', {'category': category})

def collectionsView(request, name):
  if(Category.objects.filter(name=name, status=0)):
    products = Product.objects.filter(category__name = name)
    return render(request, 'base/products/index.html', {'products':products, 'category_name': name})
  else:
    messages.warning(request, "No such category found!")
    return redirect('collections')
  
  
def product_details(request, cname, pname):
  if(Category.objects.filter(name=cname, status=0)):
    if(Product.objects.filter(name=pname, status=0)):
      products = Product.objects.filter(name=pname, status=0).first()
      return render(request, 'base/products/product_details.html', {'products': products})
    else:
      messages.error(request, "No Such Product Found")
      return redirect('collections')
  else:
    messages.error(request, 'No Such Category Found')
    return redirect('collections')
  
def remove_cart(request, cid):
    delete_cart = Cart.objects.get(id=cid)
    delete_cart.delete()
    return redirect('cart')

def orders(request):
    if request.user.is_authenticated:
        orders = Cart.objects.filter(user=request.user)
        return render(request, 'base/orders.html', {'orders': orders})
    else:
        return redirect('/')
    
def place_order(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id=data['pid']
            product = Product.objects.get(id=product_id)
            product_qty = data['product_qty']
            total_items = Orders.objects.get(total_items=product_qty)
            total = data['total']
            total_amt = Billing.objects.get(total_amount=total)
            tax = data['tax']
            tax_amt = Billing.objects.get(tax=tax)
            delivery_charge = data['delivery_charge']
            shipping_charge = Billing.objects.get(delivery_charge=delivery_charge)
            Billing.objects.create(
                user=request.user,
                product=product,
                cart=total_items,
                delivery_charge=shipping_charge,
                tax=tax_amt,
                order_total=total_amt
            )
            return JsonResponse({'status': 'Order Placed Successfully'}, status=200)
        else:
            return JsonResponse({'status': 'Login to Place Order'}, status=200)
    else:
        return JsonResponse({'status': 'Invalid Access'}, status=200)               
                

def tracking(request):
    if request.user.is_authenticated:
        track = Cart.objects.filter(user=request.user)
        return render(request, 'base/tracking.html', {'track': track})
    else:
        return redirect('/')

def billing(request):
    if request.user.is_authenticated:
        billing = Cart.objects.filter(user=request.user)
        return render(request, 'base/billing.html', {'billing': billing})
    else:
        return redirect('cart')




