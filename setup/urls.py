from django.contrib import admin
from django.urls import path, include
from escola.views import EstudantesViewSet, CursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudantesViewSet, basename='Estudantes')
router.register('cursos', CursosViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
