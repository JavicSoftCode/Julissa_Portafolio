from django.contrib import admin

from .models import SuperUser, User, Blog, Portfolio, Curso

admin.site.register(Curso)
admin.site.register(SuperUser)
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Portfolio)

# Register your models here.
