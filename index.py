
while True:
        nome = input("Digite o seu nome: ").strip()
        if all(parte.isalpha() for parte in nome.split()):
            break
        else:
            print("Digite um nome válido!")

while True:
    try:
        altura = float(input("Digite a sua altura: "))
        if altura <= 0:
            print("O valor deve ser positivo!")
        else:
            break
    except ValueError:
        print("Digite um valor válido para a altura!")

while True:
    try:
        peso = float(input("Digite o seu peso: "))
        if peso <= 0:
            print("O valor deve ser positivo!")
        else:
            break
    except ValueError:
        print("Digite um valor válido para o peso!")

def calculaImc(peso, altura):
            return peso / (altura * altura)

print(f"{nome} o seu IMC é: {calculaImc(peso, altura):.2f} ")

