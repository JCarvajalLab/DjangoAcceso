from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tienda.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]