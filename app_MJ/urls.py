from django.urls import path
from app_MJ.views import base, sobre, contato

urlpatterns = [
    path('', base, name='base'),
    path('sobre/', sobre, name="sobre"),
    path('contato/', contato, name="contato")

]
