from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('about', TemplateView.as_view(template_name='dashboard/about.html'), name='about')
]
