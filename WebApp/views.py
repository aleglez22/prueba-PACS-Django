from django.shortcuts import render

from django.http import HttpResponse
from WebApp.models import Person
from django.shortcuts import render
from django.template import loader, RequestContext, Context



# Create your views here.
def index(request):
   posts = Person.objects.all()
   mitemplate = loader.get_template("index.html")
   micontexto = Context({'posts':posts})
   contexto = RequestContext(request, {
        'posts': posts,
    })
   return HttpResponse(mitemplate.render(contexto))

def personas(request):
    persons= Person.objects.all()
    plantilla= "personas_template.html"
    datos= {'person_list':persons}
    return  render(request, plantilla, datos)

