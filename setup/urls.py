from django.contrib import admin
from django.urls import path, include
from escola.views import EstudantesViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasEstudante, ListaMatriculasCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudantesViewSet, basename='Estudantes')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudante/<int:pk>/matriculas/', ListaMatriculasEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculasCurso.as_view()),
]
