from django.urls import path , re_path
from . import views

urlpatterns = [
    path('', views.home),
    path('users/' , views.users),
    path('transfer/', views.transfer),
    path('choose_sender/' , views.choose_sender),
    path('choose_receiver/' , views.choose_receiver),
    path('enter_amount/', views.enter_amount),
    path('set_amount/', views.set_amount),
    path('finalize/', views.finalize),
]