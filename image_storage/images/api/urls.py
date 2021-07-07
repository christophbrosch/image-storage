from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('<int:pk>/images/', views.ImageListAPIView.as_view(), name='dataset-images'),
]

urlpatterns = format_suffix_patterns(urlpatterns)