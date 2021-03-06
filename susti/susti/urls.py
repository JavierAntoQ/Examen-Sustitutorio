"""susti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('inicio/', views.index, name = "inicio"),
    
    
    path('listar_empleados', views.listar_empleados, name="listar_empleados"),
    path('eliminar_empleado/<int:id>',views.eliminar_empleado, name="eliminar_empleado"),
    path('save_empleado/',views.save_empleado, name="save_empleado"),
    path('create_empleado/',views.create_empleado, name="create_empleado"),

    path('listar_regiones', views.listar_regiones, name="listar_regiones"),
    path('eliminar_region/<int:id>',views.eliminar_region, name="eliminar_region"),
    path('save_region/',views.save_region, name="save_region"),
    path('create_region/',views.create_region, name="create_region"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
