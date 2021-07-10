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

    # images
    path('<int:pk>/images/<int:image_id>/', views.images.DetailView.as_view(), name='images-detail'),

    #htmx
    path('<int:pk>/expand/', views.images.htmx.expand, name='images-expand'),
    path('<int:pk>/collapse/', views.images.htmx.collapse, name='images-collapse'),

    # transactions
    path('<int:pk>/transactions/<int:transaction_id>/delete/', views.transactions.DeleteView.as_view(), name='transactions-delete'),

    # htmx
    path('<int:pk>/transactions/<int:page>/', views.transactions.htmx.table_pagination, name='transactions-pagination'),

]
