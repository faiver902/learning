from dataclasses import dataclass

from django.http import HttpResponse
from django.shortcuts import render


@dataclass
class PersonDTO:
    id: int
    name: str
    type: str


def index(request):
    header = "Данные пользователя"  # обычная переменная
    langs = ["Python", "Java", "C#"]  # список
    user = {"name": "Tom", "age": 23}  # словарь
    address = ("Абрикосовая", 23, 45)  # кортеж
    extra = PersonDTO(2, "Vova", "rus")
    data = {
        "header": header,
        "langs": langs,
        "user": user,
        "address": address,
        "extra": extra,
    }
    return render(request, "index.html", context=data)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def about_1(request):
    return HttpResponse(f"{request.headers}", status=200)


def contact_1(request, name="Def", age="18"):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


def user_1(request, name="Def", age="18"):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


def set(request):
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Hello {username}")
    di = {"username": username, "name": "username", "id": "4"}
    for key, value in di.items():
        response.set_cookie(key, value)

    return response


def get(request):
    # username = request.COOKIES["username"]
    return HttpResponse(f"Hello {request.COOKIES}")
