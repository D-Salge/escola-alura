from django.db import models

class Estudante(models.Model):
  nome = models.CharField(max_length=30)
  email = models.EmailField(max_length=254, blank=False)
  cpf = models.CharField(max_length=11)
  data_nascimento = models.DateField()
  celular = models.CharField(max_length=14)
  
  def __str__(self):
    return self.nome
  
class Curso(models.Model):
  NIVEL_CHOICES = (
    ('B', 'Básico'),
    ('I', 'Intermediário'),
    ('A', 'Avançado'),
  )
  
  codigo = models.CharField(max_length=10)
  descricao = models.CharField(max_length=100, blank=False)
  nivel = models.CharField(max_length=1, choices=NIVEL_CHOICES, blank=False, null=False, default='B')
  
  def __str__(self):
    return self.codigo
  
class Matricula(models.Model):
  PERIODO_CHOICES = (
    ('M', 'Matutino'),
    ('V', 'Vespertino'),
    ('N', 'Noturno'),
  )
  
  estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  periodo = models.CharField(max_length=1, choices=PERIODO_CHOICES, blank=False, null=False, default='M')