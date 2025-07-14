from django.contrib import admin
from escola.models import Estudante, Curso

class EstudanteAdmin(admin.ModelAdmin):
  list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
  list_display_links = ('id', 'nome')
  search_fields = ('nome',)
  list_per_page = 20

class CursoAdmin(admin.ModelAdmin):
  list_display = ('id', 'codigo', 'descricao', 'nivel')
  list_display_links = ('id', 'codigo')
  search_fields = ('codigo',)
  list_per_page = 20

admin.site.register(Estudante, EstudanteAdmin)
admin.site.register(Curso, CursoAdmin)