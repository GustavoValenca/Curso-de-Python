"""
Camel case -> primeiroNomePessoa
Pascal case -> PrimeiroNomePessoa
Snake case -> primeiro_nome_pessoa
Screaming snake case -> PRIMEIRO_NOME_PESSOA

Convenções Python:
- snake_case para variáveis, funções e métodos;
- PascalCase para classes;
- SCREAMING_SNAKE_CASE para constantes.
"""

nome_completo = 'Luiz Otávio Miranda'
int_um = int('1')
print(int_um, type(int_um))

nome = 'Luiz'
idade = 30
maior_de_idade = idade >= 18
print(nome, idade, maior_de_idade)