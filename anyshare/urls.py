from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_redirect, name='base_redirect'),
    path('<uuid:unique_id>/', views.unique_view, name='unique_view'),
]
