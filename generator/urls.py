from django.urls import path
from .views import *

urlpatterns = [
    path('', gen_pass),
    path('nums',gen_nums),
    path('name', gen_name)
]