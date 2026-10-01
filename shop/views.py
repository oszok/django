from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello World!")

from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Strona główna")


def about(request):
    return HttpResponse("Jesteśmy klasą 4TP. Robimy sklep.")


def status(request):
    return JsonResponse({"ok": True, "version": "0.1"})


def forbidden(request):
    return HttpResponse("Brak dostępu", status=403)

def index(request):
    return render(request, "shop/index.html", {"project_name": "Sklep 4TP", "user_name": "Ania"})
