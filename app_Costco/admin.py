from django.contrib import admin
from .models import Usuario, Producto, Pedido

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_usuario','email','nombre','apellido','fecha_registro')
    search_fields = ('nombre_usuario','email','nombre','apellido')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','precio','stock','categoria','fecha_creacion')
    search_fields = ('nombre','codigo_barras')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id','usuario','fecha_pedido','estado_pedido','total_pedido')
    filter_horizontal = ('productos',)