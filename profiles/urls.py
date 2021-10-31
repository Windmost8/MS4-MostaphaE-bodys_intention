from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('my_comments', views.my_comments, name='my_comments'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('my_contacts', views.my_contacts, name='my_contacts'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
]
