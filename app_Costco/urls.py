from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_costco, name='inicio_costco'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/', views.ver_usuario, name='ver_usuario'),
    path('usuarios/actualizar/<int:usuario_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/realizar_actualizacion/<int:usuario_id>/', views.realizar_actualizacion_usuario, name='realizar_actualizacion_usuario'),
    path('usuarios/borrar/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario'),
    # --- PRODUCTO ---
path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
path('productos/', views.ver_producto, name='ver_producto'),
path('productos/actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
path('productos/realizar_actualizacion/<int:producto_id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
path('productos/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),

]