from django.shortcuts import render

from urllib import request

from django.http import HttpResponse
import random

from django.template import Context, Template, loader

def inicio(request):
    return HttpResponse("hola soy una pagina")

def otra_vista(request):
    return HttpResponse("""
                        <h1>Este es un titulo en h1</h1
                        """)

def numero_random(request):
    numero=random.randrange(1,100,4)
    texto=f"<h1>tu numero random es: {numero}</h1>"
    return HttpResponse(texto)

def numero_usuario(request,numero): 
    texto= f"<h1>Este es tu numero: {numero}</h1>"
    return HttpResponse(texto)

def anio_edad(request,numero):
    anio=2022-int(numero)
    return HttpResponse(anio)

def mi_plantilla(request):
    #plantilla= open(r"C:\Users\Facundo Nieves\Desktop\Coder\proyecto2\repasodjango\plantilla\mi_plantilla.html")
    #template=Template(plantilla.read())
    #plantilla.close
    #context= Context(diccionario_de_datos)
    #plantilla_preparada= template.render(context)
    
    
    nombre= "jorge"
    apellido="Atahualpa"
    
    lista=[23,21,345,54658,3642,2341,17564,8636]

    diccionario_de_datos={
        "nombre":nombre,
        "apellido": apellido,
        "len_nombre": len(nombre),
        "lista":lista
    }
    #version con open
    #Plantilla = open(r("C:\Users\Facundo Nieves\Desktop\Coder\proyecto2\indice\plantilla\mi_plantilla.html"))
    #template = Template(plantilla.read())
    #plantilla.close()
    #context= Context(diccionario_de_datos)
    #plantilla_preparada= template.remder(diccionario_de_datos)

    #version con loader
    #template=loader.get_template("mi_plantilla.html") 
    #plantilla_preparada= template.render(diccionario_de_datos)
    #return HttpResponse(plantilla_preparada)

    #vercion con render(from django.shortcuts import render)
    return render(request,"mi_plantilla.html", diccionario_de_datos)


