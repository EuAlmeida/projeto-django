from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, UsuarioViewSet, EditoraViewSet, LivroViewSet, AutorViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'usuario', UsuarioViewSet)
router.register(r'editora', EditoraViewSet)
router.register(r'livro', LivroViewSet)
router.register(r'autor', AutorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]