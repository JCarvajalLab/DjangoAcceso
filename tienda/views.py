from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Producto

class InicioView(ListView):
    model = Producto
    template_name = 'inicio.html'
    context_object_name = 'productos'

class CatalogoView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'catalogo.html'
    context_object_name = 'productos'

class PanelAdminView(PermissionRequiredMixin, ListView):
    
    permission_required = 'tienda.view_producto'
    model = Producto
    template_name = 'panel.html'
    context_object_name = 'productos'