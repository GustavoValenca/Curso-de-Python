nome = input("Digite seu nome: ")
tamanho = len(nome)

if tamanho < 5:
    print("Seu nome é curto")
elif tamanho < 7:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")