from typing import List
from django.urls import path

from . import views

app_name='dataset'

urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('create/', views.CreateView.as_view(), name='create'),
]
