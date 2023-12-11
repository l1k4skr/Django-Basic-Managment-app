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
    path('index/cliente/', views.client, name="cliente"),
    path('index/cliente/nuevo-cliente/', views.new_client, name="new_client"),
    path('index/cliente/editar/<int:id>/', views.edit_cliente, name='editar_cliente'),
    path('index/cliente/eliminar/<int:id>/', views.delete_cliente, name='eliminar_cliente'),
    
    # Trazabilidad
    path('index/trazabilidad/', views.trazability, name="trazability"),
    path('index/trazabilidad/boleta/<int:id>', views.boleta, name="boleta"),
    # Maquinaria
    path('index/maquinaria/', views.machine, name="maquinaria"),
    path('index/maquinaria/nueva_maquinaria/', views.new_machine, name="nueva_maquinaria"),
    path('index/maquinaria/editar/<int:id>/', views.edit_maquinaria, name='editar_maquinaria'),
    path('index/maquinaria/eliminar/<int:id>/', views.delete_maquinaria, name='eliminar_maquinaria'),
    
    # Configuracion
    path('index/configuracion/', views.config, name="configuracion"),
    path('index/configuracion/nuevo_usuario', views.new_user, name="nuevo_usuario"),
    path('index/configuracion/editar/<int:id>/', views.edit_user, name='editar_usuario'),
    path('index/configuracion/eliminar/<int:id>/', views.delete_user, name='eliminar_usuario'),

    # Manuales
    path('index/manuales/', views.manual, name="manuales"),
    path('index/manuales/nuevo_manual/', views.new_manual, name="nuevo_manual"),
    path('index/descargar_manual/<int:id>', views.download_manual, name="descargar_manual"),
    path('index/manuales/editar/<int:id>/', views.edit_manual, name='editar_manual'),
    path('index/manuales/eliminar/<int:id>/', views.delete_manual, name='eliminar_manual'),

    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)