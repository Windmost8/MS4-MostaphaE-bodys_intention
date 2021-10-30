from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    #path('fav/<int:id>/', views.add_favorite, name='add_favorite'),
    path('add_comment/<int:product_id>/', views.add_comment, name='add_comment'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('contact/', views.contact, name='contact'),
]