from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


from .models import *

def index(request):
    return render(request, "simplestore/index.html")


##this method is a generic method that will show all the records 
##for a given database model 
# def all_records(request):


def all_items(request):
    itemList = Item.objects.all()
    context = {"itemList": itemList}
    return render(request, "simplestore/all_items.html", context)

def all_customers(request):
    customerList = Customer.objects.all()
    context = {'customerList': customerList}
    return render(request, "simplestore/all_customers.html", context)

def all_orders(request):
    orderList = Order.objects.all()
    context = {'orderList': orderList}
    return render(request, "simplestore/all_orders.html", context)

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    orderItemList = order.getOrderItems()
    context = {'order': order, "orderItemList":orderItemList}
    return render(request, "simplestore/order_detail.html", context)

def addNewCustomer(request):
    if request.method == 'POST':
        customerName = request.POST.get('customerName')
        newCustomer = Customer(name=customerName)
        newCustomer.save()
    return render(request, 'simplestore/add_customer.html')
