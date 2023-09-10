from django.urls import path
from . import views

urlpatterns = [
    path('addfram/', views.addfarmers,name="add"),
]
