from django.http import HttpResponse
from django.shortcuts import render

from .models import Item

def index(request):
    return HttpResponse("Welcome to the simple store!")


##this method is a generic method that will show all the records 
##for a given database model 
# def all_records(request):


def all_items(request):
    itemList = Item.objects.all()
    context = {"itemList": itemList}
    return render(request, "simplestore/all_items.html", context)
