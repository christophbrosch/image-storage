from typing import List
from django.urls import path

from . import views

app_name='datasets'

urlpatterns = [
    # datasets
    path('list/', views.datasets.ListView.as_view(), name='list'),
    path('<int:pk>/', views.datasets.DetailView.as_view(), name='detail'),
    path('create/', views.datasets.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.datasets.DeleteView.as_view(), name='delete'),
    
    # transactions
    path('<int:pk>/delete', views.transactions.DeleteView.as_view(), name='transactions-delete'),
    path('<int:pk>/transactions/<int:page>/', views.transactions.table_pagination, name='transactions-pagination'),
]
