from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('index/', views.index, name='index'),
    path('index/cliente/', views.Client_view.client, name="cliente"),
    path('index/cliente/nuevo-cliente/', views.Client_view.new_client, name="new_client"),
    path('index/trazabilidad/', views.trazability, name="trazability"),
    path('index/maquinaria/', views.Machine_view.machine, name="maquinaria"),
    path('index/maquinaria/nueva_maquinaria/', views.Machine_view.new_machine, name="nueva_maquinaria"),
    path('index/configuracion/', views.Config_view.config, name="configuracion"),
    path('index/configuracion/new_user', views.Config_view.new_user, name="new_user"),
    path('index/manuales/', views.Manual_view.manual, name="Manuales"),
    path('index/manuales/nuevo_manual/', views.Manual_view.new_manual, name="nuevo_manual"),
    ]