from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudantesSerializer, ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class EstudantesViewSet(viewsets.ModelViewSet):
  queryset = Estudante.objects.all()
  serializer_class = EstudanteSerializer
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
  search_fields = ['cpf']
  ordering_fields = ['nome', 'id']
  
class CursosViewSet(viewsets.ModelViewSet):
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  
class MatriculasViewSet(viewsets.ModelViewSet):
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer
  
class ListaMatriculasEstudante(generics.ListAPIView):
  def get_queryset(self):
    queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasEstudantesSerializer
  
class ListaMatriculasCurso(generics.ListAPIView):
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasCursoSerializer