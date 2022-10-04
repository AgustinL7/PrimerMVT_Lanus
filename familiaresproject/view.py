from django import http
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
import random
from familiaLanus.models import Persona	

def crear_familiares(request,nombre,apellido):
    persona= Persona(nombre=nombre , apellido=apellido, edad=random.randrange(1,86),fecha_nacimiento=datetime.now())
    persona.save()
    template=loader.get_template('crear_familiares.html')
    template_renderizado=template.render({'personas':persona})
    return HttpResponse(template_renderizado)

def ver_familiares(request):

    personas=Persona.objects.all()
    template=loader.get_template('ver_familiares.html')
    template_renderizado=template.render({'personas':personas})
    return HttpResponse(template_renderizado)
    
