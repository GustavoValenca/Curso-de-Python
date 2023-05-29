import datetime

today = datetime.date.today()
year = today.strftime("%Y")

idade = 20
altura = 1.80
peso = 80
imc = peso / altura ** 2

nascimento = int(year) - idade
print(nascimento)