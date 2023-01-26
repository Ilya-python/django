from django.urls import path
from .views import *


urlpatterns=[
    path('', user_register, name='registr'),
    path('success',user_success_register,name='success_register'),
    path('login', user_login, name='login'),
    path('logout', user_success_out, name='logout'),
    path('comment/<int:pk>', add_comment, name="add_comment")
]