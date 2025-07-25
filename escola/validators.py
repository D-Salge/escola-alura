import re
from rest_framework import serializers

def cpf_invalido(cpf):
    cpf = ''.join(re.findall(r'\d', str(cpf)))
    if len(cpf) != 11:
        raise serializers.ValidationError({"cpf": "O CPF deve conter exatamente 11 dígitos."})

    if len(set(cpf)) == 1:
        raise serializers.ValidationError({"cpf": "CPF inválido (dígitos repetidos)."})

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito_verificador_1 = 0 if resto < 2 else 11 - resto

    if int(cpf[9]) != digito_verificador_1:
        raise serializers.ValidationError({"cpf": "CPF inválido."})

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito_verificador_2 = 0 if resto < 2 else 11 - resto

    if int(cpf[10]) != digito_verificador_2:
        raise serializers.ValidationError({"cpf": "CPF inválido."})

def nome_invalido(nome):
    if not nome.isalpha():
        raise serializers.ValidationError({"nome": "O nome só pode conter letras."})

def celular_invalido(celular):
    if len(celular) != 13:
        raise serializers.ValidationError({"celular": "O celular precisa conter 13 dígitos."})