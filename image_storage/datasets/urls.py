from typing import List
from django.urls import path

from . import views

app_name='datasets'

urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),

    path('<int:pk>/transactions/<int:page>/', views.transactions_table, name='transactions-page'),
]
