from django.contrib import admin
from django.urls import path, re_path
from app01 import views

urlpatterns=[
    path('login/',views.login,name='login'),
    path('registry/',views.registry,name='registry'),
    path('control/',views.control,name='control'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),


    path('account/list/',views.account_list,name='account_list'),
    path('account/add/',views.account_add,name='account_add'),
    path('account/delete/', views.account_delete, name='account_delete'),
    path('account/<int:nid>/edit/', views.account_edit),

    path('staff/list/', views.staff_list, name='staff_list'),
    # path('staff/add/', views.staff_add, name='staff_add'),
    # path('staff/delete/', views.staff_delete, name='staff_delete'),
    # path('staff/<int:nid>/edit/', views.staff_edit),
    path('data/', views.data, name='data'),
    path('info/', views.info, name='info'),
    path('center/', views.center, name='center'),
    path('water/', views.water, name='water'),

]