from django.urls import path,include
from . import views
from accounts import views as AccountViews

urlpatterns = [
    
    path('',AccountViews.vendorDashboard,name='vendor'),
    path('profile/',views.vprofile,name="vprofile"),
    path('menu-builder/',views.menu_builder,name='menu_builder'),
    path('menu-bulider/category/<int:pk>/',views.fooditems_by_category,name="fooditems_by_category"),

    # category crud
    path('menu-bulider/category/add/',views.add_category,name="add_category"),
    path('menu-bulider/category/edit/<int:pk>',views.edit_category,name="edit_category"),
    path('menu-bulider/category/delete/<int:pk>',views.delete_category,name="delete_category"),

    # food item crud
    path('menu-bulider/food/add/',views.add_food,name="add_food"),
    path('menu-bulider/food/edit/<int:pk>/',views.edit_food,name="edit_food"),
    path('menu-bulider/food/delete/<int:pk>',views.delete_food,name="delete_food"),



]