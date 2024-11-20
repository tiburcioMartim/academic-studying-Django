from django.db.models.expressions import result
from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    idade = int(idade)
    return HttpResponse("<h1>Hello {} de {} anos.</h1>".format(nome, idade))

def soma(request, n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    result = n1 + n2
    return HttpResponse(f"A soma de {n1} + {n2} é = {result}")

def subtraction(request, n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    result = n1 - n2
    return HttpResponse(f"A diferença de {n1} - {n2} é = {result}")

def multiply(request, n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    result = n1 * n2
    return HttpResponse(f"O produto entre {n1} * {n2} é = {result}")

def divisor(request, n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    if n2 == 0:
        return HttpResponse(f"A divisão por {n2} não é válida, tente outro número.")
    result = n1 / n2
    return HttpResponse(f"O quociente de {n1} / {n2} é = {result}")