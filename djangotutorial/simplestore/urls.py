from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_items/", views.all_items, name="all_items"),
]
