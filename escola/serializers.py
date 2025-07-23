from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
import re

class EstudanteSerializer(serializers.ModelSerializer):
  class Meta:
      model = Estudante
      fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']
      
  def validate_cpf(self, cpf):
      cpf = ''.join(re.findall(r'\d', str(cpf)))
      
      if len(cpf) != 11:
        raise serializers.ValidationError("O CPF deve conter exatamente 11 dígitos.")
      
      if len(set(cpf)) == 1:
        raise serializers.ValidationError("CPF inválido (dígitos repetidos).")
      
      soma = 0
      
      for i in range(9):
        soma += int(cpf[i]) * (10 - i)
        
      resto = soma % 11
      digito_verificador_1 = 0 if resto < 2 else 11 - resto
      
      if int(cpf[9]) != digito_verificador_1:
        raise serializers.ValidationError("CPF inválido.")
      
      soma = 0
      
      for i in range(10):
        soma += int(cpf[i]) * (11 - i)
        
      resto = soma % 11
      digito_verificador_2 = 0 if resto < 2 else 11 - resto
      
      if int(cpf[10]) != digito_verificador_2:
        raise serializers.ValidationError("CPF inválido.")
      
      return cpf

class CursoSerializer(serializers.ModelSerializer):
  class Meta:
      model = Curso
      fields = '__all__'
      
class MatriculaSerializer(serializers.ModelSerializer):
  class Meta:
      model = Matricula
      exclude = []
      
class ListaMatriculasEstudantesSerializer(serializers.ModelSerializer):
  curso = serializers.ReadOnlyField(source='curso.descricao')
  periodo = serializers.SerializerMethodField()
  class Meta:
      model = Matricula
      fields = ['curso', 'periodo']
      
  def get_periodo(self, obj):
    return obj.get_periodo_display()
  
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
  estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
  class Meta:
      model = Matricula
      fields = ['estudante_nome']