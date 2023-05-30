from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.mynotes, name='mynotes'),
    path('notes/<slug:slug>', views.mynotedetails, name='mynotedetails')
  
]
