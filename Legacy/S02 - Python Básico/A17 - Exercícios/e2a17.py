num1 = input("Digite a hora: ")

try:
    num1 = int(num1)

    if num1 < 12:
        print("Bom dia")
    elif num1 < 18:
        print("Boa tarde")
    else:
        print("Boa noite")
except:
    print("Erro")
