from django.urls import path
from app_MJ.views import home, sobre, contato

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name="sobre"),
    path('contato/', contato, name="contato")

]
