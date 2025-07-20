nome = input("Digite o seu nome: ")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

def calculaImc(peso, altura):
    return peso / (altura * altura)

print(f"{nome} o seu IMC é: {calculaImc(peso, altura):.2f} ")
