from django.urls import path
from . import views


urlpatterns = [
 path('item_list/', views.item_list, name='item_list'),   
 #path('<slug:slug>/',views.item_detail, name='item_detail'),
]
