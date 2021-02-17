from django.shortcuts import render, HttpResponse, redirect

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

def create_region(request):

    return render(request, 'create_region.html',{
        'titulo':'Crear una nueva region',
        'mensaje':'Agregar region'
    })

def listar_regiones(request):

    return render(request, 'listar_regiones.html',{
        'titulo':'Lista de regiones',
        'mensaje':'Listado de Regiones'
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


