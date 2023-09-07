from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hoja #necesito importar lo del modelo-la tabla Hoja
#utilizar el fomrulario de form.py
from .forms import HojaForm 
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

#la funcion para poder acceder a lo que se vera-templates
def hojas(request):
    #hojas recibe la información
    hojas=Hoja.objects.all() #hay que pasarle el modelo a la vista
   #print(hojas)
   #la variable hojas-verde- es la que estará en el for de las filas del index
    return render(request,'hojas/index.html',{'hojas':hojas}) 

def crear_hoja(request):
    formulario=HojaForm(request.POST or None, request.FILES or None) #identificar los elementos que nos envian en el formulario
    #request.files para recepcionar los archivos, luego en el if se guardan
    if formulario.is_valid():
        formulario.save()
        return redirect('hojas')
    return render(request,'hojas/crear.html', {'formulario':formulario}) #se envia la info al fomrulario a través de la variable formulario-verde

def editar_hoja(request,id):
    hoja=Hoja.objects.get(id=id) #consulta de la hoja
    #recuperar informacion:
    formulario=HojaForm(request.POST or None, request.FILES or None, instance=hoja)
    #si hay cambios
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('hojas')
    return render(request,'hojas/editar.html',{'formulario':formulario})

def borrar_hoja(request,id):
    hoja=Hoja.objects.get(id=id)
    hoja.delete()
    return redirect('hojas') #en hoja esta el boton borrar