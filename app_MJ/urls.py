from django.urls import path
from app_MJ.views import base

urlpatterns = [
    path('', base, name='base'),

]
