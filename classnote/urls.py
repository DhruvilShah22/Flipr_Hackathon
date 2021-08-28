from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='click'),
    path('join/', views.join, name="join"),
    path('processing/', views.processing, name="processing"),
    path('profile/', views.profile),
    path('update-profile/', views.UserUpdatation),
    path('register/', views.register, name="register"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
]