from django.urls import path
from . import views
from django.shortcuts import render
from .views import send_invite
from .views import invite_user, base_redirect, unique_view, send_invite, InviteView, invite_view

urlpatterns = [
    path('', views.base_redirect, name='base_redirect'),
    path('<uuid:unique_id>/', views.unique_view, name='unique_view'),
    path('invite/', views.invite_user, name='invite_user'),
    path('expired/', lambda request: render(request, 'expired.html'), name='expired'),
    path('invite/', send_invite, name='send_invite'),
    # path('invite/', invite_view, name='invite'),
    path('invite/', views.invite_view, name='invite'),
    
    
    
    path('invite/', invite_user, name='invite_user'),
    path('base_redirect/', base_redirect, name='base_redirect'),
    path('unique/<str:unique_id>/', unique_view, name='unique_view'),
    path('send_invite/', send_invite, name='send_invite'),
    
    # DRF API Endpoints
    path('api/invite/', InviteView.as_view(), name='api_invite_view'),
    path('api/invite_view/', invite_view, name='api_invite_view_function'),
]
