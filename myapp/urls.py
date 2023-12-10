from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Login
    path('', views.home, name="home"),
    path('login/', views.login_view, name="login"),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('index/', views.index, name='index'),

    # Clientes
    path('index/cliente/', views.Client_view.client, name="cliente"),
    path('index/cliente/nuevo-cliente/', views.Client_view.new_client, name="new_client"),
    path('index/cliente/editar/<int:id>/', views.Client_view.edit_cliente, name='editar_cliente'),
    path('index/cliente/eliminar/<int:id>/', views.Client_view.delete_cliente, name='eliminar_cliente'),
    
    # Trazabilidad
    path('index/trazabilidad/', views.trazability, name="trazability"),
    path('index/descargar_manual/<int:id>', views.Manual_view.download_manual, name="descargar_manual"),
    path('index/manuales/editar/<int:id>/', views.Manual_view.edit_manual, name='editar_manual'),
    path('index/manuales/eliminar/<int:id>/', views.Manual_view.delete_manual, name='eliminar_manual'),
    path('index/descargar_manual/<int:id>', views.Manual_view.download_manual, name="descargar_manual"),
    path('index/manuales/editar/<int:id>/', views.Manual_view.edit_manual, name='editar_manual'),
    path('index/manuales/eliminar/<int:id>/', views.Manual_view.delete_manual, name='eliminar_manual'),

    # Maquinaria
    path('index/maquinaria/', views.Machine_view.machine, name="maquinaria"),
    path('index/maquinaria/nueva_maquinaria/', views.Machine_view.new_machine, name="nueva_maquinaria"),
    path('index/maquinaria/editar/<int:id>/', views.Machine_view.edit_maquinaria, name='editar_maquinaria'),
    path('index/maquinaria/eliminar/<int:id>/', views.Machine_view.delete_maquinaria, name='eliminar_maquinaria'),
    
    # Configuracion
    path('index/configuracion/', views.Config_view.config, name="configuracion"),
    path('index/configuracion/nuevo_usuario', views.Config_view.new_user, name="nuevo_usuario"),
    path('index/configuracion/editar/<int:id>/', views.Config_view.edit_user, name='editar_usuario'),
    path('index/configuracion/eliminar/<int:id>/', views.Config_view.delete_user, name='eliminar_usuario'),

    # Manuales
    path('index/manuales/', views.Manual_view.manual, name="manuales"),
    path('index/manuales/nuevo_manual/', views.Manual_view.new_manual, name="nuevo_manual"),
    path('index/descargar_manual/<int:id>', views.Manual_view.download_manual, name="descargar_manual"),
    path('index/manuales/editar/<int:id>/', views.Manual_view.edit_manual, name='editar_manual'),
    path('index/manuales/eliminar/<int:id>/', views.Manual_view.delete_manual, name='eliminar_manual'),

    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)