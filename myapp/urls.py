"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_product_subcategory/<int:product_id>/', views.add_product_subcategory, name='add_product_subcategory'),
    path('view_products/', views.view_products, name='view_products'),
    path('view_products_subcategory/<int:product_id>/', views.view_product_subcategory, name='view_product_subcategory'),
    path('update_product_subcategory/<int:subcategory_id>/', views.update_product_subcategory, name='update_product_subcategory'),
    path('delete_product_subcategory/<int:subcategory_id>/', views.delete_product_subcategory, name='delete_product_subcategory'),
    path('dashboard/', views.product_manager_dashboard, name='product_manager_dashboard'),
    path('search_product/', views.search_product, name='search_product'),
]