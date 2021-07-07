from django.urls import path

from . import views

app_name = 'transactions'

urlpatterns = [
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
]