from django.contrib import admin

# Register your models here.


from .models import Alumno
#registar el modelo Alumno en el admin
admin.site.register(Alumno)
