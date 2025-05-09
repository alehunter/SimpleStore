from django.urls import path

from . import views


app_name = "simplestore"
urlpatterns = [
    path("", views.index, name="index"),
    path("items/", views.all_items, name="all_items"),
    path("items/add", views.addNewItem, name="addNewItem"),
    path("customers/", views.all_customers, name="all_customers"),
    path("customers/add", views.addNewCustomer, name="addNewCustomer"),
    path("orders/", views.all_orders, name="all_orders"),
    path("orders/<int:order_id>/", views.order_detail, name="order_detail"),

]
