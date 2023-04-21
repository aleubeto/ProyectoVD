from django.urls import path
from rest_framework import routers
from .views import PostViewSet

# Router que renderiza PostViewSet en la ruta "/api/posts"
router = routers.DefaultRouter()
router.register('posts', PostViewSet)
urlpatterns = router.urls