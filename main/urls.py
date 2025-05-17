# main/urls.py
from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # 'home' görünüşünü bağlayırıq
    path('contactmessage/', views.contact_message, name='contactmessage'),
    path('services/', views.services_view, name='services'),
    path('questions/', views.questions_view, name='questions'),  # Sualar səhifəsi
    path('contact/', views.contact_view, name='contact'),  # Sualar səhifəsi
    path('404/', views.test_404_view, name='test404'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



