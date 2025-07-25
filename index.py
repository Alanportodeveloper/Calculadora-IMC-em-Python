import tkinter as tk
from tkinter import messagebox

def calcula_imc(peso, altura):
    return peso / (altura * altura)

def calcular_imc():
    try:
        nome = nome_entry.get().strip()
        altura = altura_entry.get().strip()
        peso = peso_entry.get().strip()

        if not nome:
            raise ValueError("O nome deve ser preenchido!")

        if not all(parte.isalpha() for parte in nome.split()):
            raise ValueError("Digite um nome válido!")

        if not altura:
            raise ValueError("A altura deve ser informada!")
        if not peso:
            raise ValueError("O peso deve ser informado!")

        try:
             altura = float(altura)
             if altura <= 0:
                raise ValueError("A altura deve ser um valor positivo (Exemplo: 1.75)!")
        except ValueError:
             raise ValueError("Digite um valor válido para a altura (Exemplo: 1.75)!")

        try:
            peso = float(peso)
            if peso <=0:
                raise ValueError("O peso deve ser um valor positivo (Exemplo: 70.5)!")
        except ValueError:
            raise ValueError("Digite um valor válido para o peso (Exemplo: 70.5)!")

        imc = calcula_imc(peso, altura)

        resultado_label.config(text=f"{nome}, o seu IMC é: {imc:.2f}")

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

janelaPrincipal = tk.Tk()
janelaPrincipal.title("Calculadora do IMC")

tk.Label(janelaPrincipal, text="Digite seu nome: ").grid(row=0, column=0, padx=10, pady=5, sticky="w")
nome_entry = tk.Entry(janelaPrincipal)
nome_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(janelaPrincipal, text="Digite a sua altura: ").grid(row=1, column=0, padx=10, pady=5, sticky="w")
altura_entry = tk.Entry(janelaPrincipal)
altura_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(janelaPrincipal, text="Digite o seu peso: ").grid(row=2, column=0, padx=10, pady=5, sticky="w")
peso_entry = tk.Entry(janelaPrincipal)
peso_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

calcular_btn = tk.Button(janelaPrincipal, text="Calcular IMC", command=calcular_imc)
calcular_btn.grid(row=3, column=0, columnspan=2, pady=10)

resultado_label = tk.Label(janelaPrincipal, text="")
resultado_label.grid(row=4, column=0, columnspan=2, pady=5)

janelaPrincipal.grid_columnconfigure(1, weight=1)

janelaPrincipal.mainloop()



