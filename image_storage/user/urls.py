from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]