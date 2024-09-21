from django.urls import path
from . import views



urlpatterns = [
    path("",views.home,name="home"),
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    #################PRODUCTOS################
    path("productos/",views.producto_list,name="producto_list"),
    path("productos/create/",views.producto_create,name="producto_create"),
    path("productos/update/<int:pk>",views.producto_update,name="producto_update"),
    path("productos/delete/<int:pk>",views.producto_delete,name="producto_delete"),
    ###############PROVEEDORES##################
    path("proveedores/",views.proveedor_list,name="proveedor_list"),
    path("proveedores/create/",views.proveedor_create,name="proveedor_create"),
    path("proveedores/update/<int:pk>",views.proveedor_update,name="proveedor_update"),
    path("proveedores/delete/<int:pk>",views.proveedor_delete,name="proveedor_delete"),
    #################VENTAS###################
    path("ventas/",views.venta_list,name="venta_list"),
    path("ventas/create/",views.venta_create,name="venta_create"),
    path("ventas/update/<int:pk>",views.venta_update,name="venta_update"),
    path("ventas/delete/<int:pk>",views.venta_delete,name="venta_delete"),
    #################DETALLE_VENTAS###################
    path("detalle_ventas/",views.detalle_venta_list,name="detalle_venta_list"),
    path("detalle_ventas/create/",views.detalle_venta_create,name="detalle_venta_create"),
    path("detalle_ventas/update/<int:pk>",views.detalle_venta_update,name="detalle_venta_update"),
    path("detalle_ventas/delete/<int:pk>",views.detalle_venta_delete,name="detalle_venta_delete"),
    ################# CLIENTE ###################
    path("clientes/",views.cliente_list,name="cliente_list"),
    path("clientes/create/",views.cliente_create,name="cliente_create"),
    path("clientes/update/<int:pk>",views.cliente_update,name="cliente_update"),
    path("clientes/delete/<int:pk>",views.cliente_delete,name="cliente_delete"),
]