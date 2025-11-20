from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.home, name="home"),
    path('add_category/',views.add_category, name="add_category"),
    path('category_list/',views.category_list, name="category_list"),
    path('product_loop/',views.product_loop, name="product_loop"),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
