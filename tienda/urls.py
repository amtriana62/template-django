from django.urls import path
from . import views
#propiedades para poder mostrar las imagenes
from django.conf import settings
from django.contrib.staticfiles.urls import static #los archivos estaticos


urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('hojas',views.hojas, name='hojas'), #coincidir con la funcion que hay en views
    #name es el que va a acceder directamente a la url
    path('hojas/crearhoja',views.crear_hoja, name='crearhoja'),
    #poner un url diferente de hojas hojas/crear_hoja
    path('hojas/editarhoja',views.editar_hoja, name='editarhoja'),
    path('borrarhoja/<int:id>',views.borrar_hoja, name='borrarhoja'),
    #el id que se pasa debe ser igual al que tiene la funcion borrar en las views
    path('hojas/editarhoja/<int:id>',views.editar_hoja, name='editarhoja')

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)