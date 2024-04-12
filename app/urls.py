from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_email/', views.add_email, name='add_email'),
    path('getPrize', views.get_prize, name='get_prize'),
]