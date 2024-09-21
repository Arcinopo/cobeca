from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Producto, Proveedor, Venta, Detalle_venta, Cliente
from .forms import ProductoForm, ProveedorForm, VentaForm, DetalleVentaForm,ClienteForm

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username = username,password=password)
            login(request,user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request,"core/signup.html",{"form":form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request,"core/signin.html",{"form":form})


################### PRODUCTO ############################

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'core/producto_list.html', {'productos':productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'core/producto_form.html',{'form':form})

def producto_update(request,pk):
    producto = get_object_or_404(Producto,pk=pk)    
    if request.method =='POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'core/producto_form.html', {'form':form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto,pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request,'core/producto_confirm_delete.html',{'producto': producto})

################### PROVEEDOR ############################

def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'core/proveedor_list.html', {'proveedores':proveedores})

def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm()
    return render(request, 'core/proveedor_form.html',{'form':form})

def proveedor_update(request,pk):
    proveedor = get_object_or_404(Proveedor,pk=pk)    
    if request.method =='POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedor_list')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'core/proveedor_form.html', {'form':form})

def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor,pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedor_list')
    return render(request,'core/proveedor_confirm_delete.html',{'proveedor': proveedor})

################### VENTAS ############################

def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'core/venta_list.html', {'ventas':ventas})

def venta_create(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'core/venta_form.html',{'form':form})

def venta_update(request,pk):
    venta = get_object_or_404(Venta,pk=pk)    
    if request.method =='POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'core/venta_form.html', {'form':form})

def venta_delete(request, pk):
    venta = get_object_or_404(Venta,pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('venta_list')
    return render(request,'core/venta_confirm_delete.html',{'venta': venta})


################### DETALLE_VENTA ############################

def detalle_venta_list(request):
    detalle_ventas = Detalle_venta.objects.all()
    return render(request, 'core/detalle_venta_list.html', {'detalle_ventas':detalle_ventas})

def detalle_venta_create(request):
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalle_venta_list')
    else:
        form = DetalleVentaForm()
    return render(request, 'core/detalle_venta_form.html',{'form':form})

def detalle_venta_update(request,pk):
    detalle_venta = get_object_or_404(Detalle_venta,pk=pk)    
    if request.method =='POST':
        form = DetalleVentaForm(request.POST, instance=detalle_venta)
        if form.is_valid():
            form.save()
            return redirect('detalle_venta_list')
    else:
        form = DetalleVentaForm(instance=detalle_venta)
    return render(request, 'core/detalle_venta_form.html', {'form':form})

def detalle_venta_delete(request, pk):
    detalle_venta = get_object_or_404(Detalle_venta,pk=pk)
    if request.method == 'POST':
        detalle_venta.delete()
        return redirect('detalle_venta_list')
    return render(request,'core/detalle_venta_confirm_delete.html',{'detalle_venta': detalle_venta})

################### Clientes ############################

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/cliente_list.html', {'clientes':clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'core/cliente_form.html',{'form':form})

def cliente_update(request,pk):
    cliente = get_object_or_404(Cliente,pk=pk)    
    if request.method =='POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/cliente_form.html', {'form':form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente,pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request,'core/cliente_confirm_delete.html',{'cliente':cliente})