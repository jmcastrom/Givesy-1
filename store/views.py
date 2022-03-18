from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Categoria, Producto, Imagen, Orden
from .forms import UsuarioForm

def index(req):
    categorias = Categoria.objects.filter()
    productos = Producto.objects.filter(estado="activo")
    context = {"productos":productos, "categorias":categorias}
    return HttpResponse(context)
    #return render(req, context)

def UserView(req):
    form_class = UsuarioForm
    
    def get_success_url(self):
        return reverse("contact")

def filtrar_productos(req, slug):
    print(type(slug), slug)
    if Categoria.objects.filter(slug=slug).exists():
        categorias = Categoria.objects.get(slug=slug)
    else:
        categorias = None
    
    if categorias and Producto.objects.filter(slug=slug).exists():
        productos_filt = Producto.objects.filter(activo=True, categoria=categorias)
    else:
        productos_filt = None
    
    context = {"productos":productos_filt, " categorias":categorias, " slug":slug}
    return HttpResponse(context)
    #return render(req, context)

def buscar(req):
    name = req.GET()
    productos = Producto.objects.filter(activo=True, nombre__icontains=name)
    categorias = Categoria.objects.filter(activo=True)
    context = {"productos":productos, "categorias":categorias}
    return render(req, context)

def detail(req, slug):
    if Producto.objects.filter(activo=True, slug=slug).exists():
        producto = Producto.objects.get(activo=True, slug=slug)
        categorias = Categoria.objects.filter(activo=True)
        context = {"productos":producto, "categorias":categorias}
        return render(req, context)
