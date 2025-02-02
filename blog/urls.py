from django.urls import path 
from .views import alist , feedblog,deta_blog,edit_blog,delete_blog

urlpatterns = [
    path('', alist, name='home'),
    path('form', feedblog, name='form'),
    path('detail/<int:pk>/', deta_blog, name= 'detail'),
    path('edit/<int:pk>', edit_blog, name = 'edit_blog'),
    path('delete/<int:pk>', delete_blog, name = 'delete_blog')
]
