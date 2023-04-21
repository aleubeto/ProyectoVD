from django.urls import path
from rest_framework import routers
from .views import *

# Router que renderiza PostViewSet en la ruta "/api/posts"
router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('genders', GenderViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('team', TeamViewSet)
router.register('calificaciones', CalificacionViewSet)
urlpatterns = router.urls