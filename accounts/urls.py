from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register', views.register, name='register'),
    path('sign_up', views.sign_up, name='sign_up'),
    # path('register', views.register, name='register'),
]