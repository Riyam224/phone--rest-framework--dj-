import imp
from tkinter.messagebox import NO
from django.contrib import admin

# Register your models here.


from .models import Note


admin.site.register(Note)