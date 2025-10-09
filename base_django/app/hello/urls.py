from django.urls import path, re_path

from hello import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("about/contact/<name>/<age>", views.contact_1),
    path("about/", views.about_1),
    re_path(r"^user(?:/(?P<name>\D+))?(?:/(?P<age>\d+))?/?$", views.user_1),
    path("set", views.set),
    path("get", views.get),
]
