from django.shortcuts import render
from django.http import HttpResponse
from person1.models import Person

def index(request):
    return HttpResponse("<h1> Welcome to Django </h1>")

def identity(request, te):
    try:
        a = Person.objects.get(id=te)
        return HttpResponse(f"{a.name} {a.sec}")
    except Person.DoesNotExist:
        return HttpResponse(f"Person with id {te} not found")
