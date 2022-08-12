from tkinter import Y
from django.contrib import admin
from .models import Memories, Student, Year, Branch, Comments, Student
# Register your models here.

admin.site.register(Student)
admin.site.register(Comments)
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Memories)