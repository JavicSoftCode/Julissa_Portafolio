from django.contrib import admin

from .models import User, Blog, Portfolio, Curso

admin.site.register(Curso)
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Portfolio)

# Register your models here.
