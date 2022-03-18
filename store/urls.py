from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cuenta/', views.UserView, name='usuario'),
    path('<slug:slug>/filtro', views.filtrar_productos, name='filtro'),
    path('<slug:slug>/buscar', views.buscar, name='buscar'),
    path('<slug:slug>/detail', views.detail, name='detallar'),
]