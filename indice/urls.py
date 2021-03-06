from django.urls import path
from .views import inicio,otra_vista,numero_random,numero_usuario,anio_edad,mi_plantilla

urlpatterns = [
    
    path("",inicio,name="inicio"),
    path("otra_vista/",otra_vista,name="otra vista"),
    path("edad/<numero>",anio_edad),
    path("mi_plantilla/",mi_plantilla,name="mi_plantilla"),
    path("dame-numero/<int:numero>",numero_usuario),
    path("numero_random/",numero_random,name="numero_random"),
]