from django.contrib import admin
from .models import TeamMember, Gender, Usuario, Post, Calificacion

# Register your models here.
admin.site.register(TeamMember)
admin.site.register(Gender)
admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Calificacion)