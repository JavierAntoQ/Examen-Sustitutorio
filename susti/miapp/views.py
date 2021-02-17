from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Region
from django.contrib import messages
# Create your views here.
layout = """
    <h1>
        <ul>
            <li>
                <a href="/inicio"> INICIO </a> 
            </li>
        </ul>
    </h1>
    """
def index(request):

    return render(request, 'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto web con Django'
    })

def listar_regiones(request):
    regiones = Region.objects.all
    return render(request, 'listar_regiones.html',{
        'regiones' : regiones,
        'titulo' : 'LISTADO DE REGIONES',
    })

def eliminar_region(request, id):
    region = Region.objects.get(pk=id)
    region.delete()
    return redirect('listar_regiones')

def save_region(request):
    if request.method == 'POST':
        date = request.POST['date']
        name = request.POST['name']
        cases =request.POST['cases']
        deaths = request.POST['deaths']
        lathality = request.POST['lathality']

        region = Region(
            date = date,
            name = name, 
            cases = cases,
            deaths = deaths,
            lathality = lathality
    )
        region.save()
        messages.success(request, f'Se agrego correctamente la region {region.id}')
        return redirect('listar_regiones')
        
def create_region(request):

    return render(request, 'create_region.html',{
        'titulo':'Crear una nueva region',
        'mensaje':'Agregar region'
    })

def create_empleado(request):

    return render(request, 'create_empleado.html',{
        'titulo':'Crear un nuevo empleado',
        'mensaje':'Agregar empleado'
    })

def listar_empleados(request):

    return render(request, 'listar_empleados.html',{
        'titulo':'Lista de empleados',
        'mensaje':'Listado de empleados'
    })


