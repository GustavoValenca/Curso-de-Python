num1 = input("Digite um número inteiro: ")

try:
    num1 = int(num1)

    if num1 % 2 == 0:
        print("Par")
    else:
        print("Impar")
except:
    print("Você não digitou um número inteiro")

