from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_form),
    path('list/', views.emp_list)
]