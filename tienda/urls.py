from django.urls import path
from .views import (InicioView, CatalogoView, PanelAdminView)

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('catalogo/', CatalogoView.as_view(), name='catalogo'),
    path('panel/', PanelAdminView.as_view(), name='panel'),
]