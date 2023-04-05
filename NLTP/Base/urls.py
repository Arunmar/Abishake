from django.urls import path
from Base import views as views
urlpatterns=[
    path("",views.welcome),
    path("InputFormater",views.InputFormatter),
    path("process",views.process,name="process"),
]