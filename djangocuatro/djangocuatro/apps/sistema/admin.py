from django.contrib import admin

from djangocuatro.apps.sistema.models import Empresa, PlanEmpresa, Categoria, Proveedor, Producto, Cliente

# Register your models here.
admin.site.register(Empresa)
admin.site.register(PlanEmpresa)


# admin modelos giro
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Cliente)
