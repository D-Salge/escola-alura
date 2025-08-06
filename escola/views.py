from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudantesSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from escola.throttles import MatriculaAnonRateThrottle

class EstudantesViewSet(viewsets.ModelViewSet):
  queryset = Estudante.objects.all().order_by('id')
  # serializer_class = EstudanteSerializer
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
  search_fields = ['cpf']
  ordering_fields = ['nome', 'id']
  
  def get_serializer_class(self):
    if self.request.version == 'v2':
      return EstudanteSerializerV2
    return EstudanteSerializer
  
class CursosViewSet(viewsets.ModelViewSet):
  queryset = Curso.objects.all().order_by('id')
  serializer_class = CursoSerializer
  
class MatriculasViewSet(viewsets.ModelViewSet):
  queryset = Matricula.objects.all().order_by('id')
  serializer_class = MatriculaSerializer
  throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]

class ListaMatriculasEstudante(generics.ListAPIView):
  def get_queryset(self):
    queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
    return queryset
  serializer_class = ListaMatriculasEstudantesSerializer
  
class ListaMatriculasCurso(generics.ListAPIView):
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
    return queryset
  serializer_class = ListaMatriculasCursoSerializer