import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limpar_tela()

    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    operacao = input("somar(+), multiplicar(*), subtrair(-) ou dividir(/)? ")

    if operacao.lower() == "somar" or operacao == "+":
        print(f"o resultado da soma e: {num1 + num2}")
    elif operacao.lower() == "multiplicar" or operacao == "*":
        print(f"o resultado da multiplicacao e: {num1 * num2}")
    elif operacao.lower() == "subtrair" or operacao == "-":
        print(f"o resultado da subtracao e: {num1 - num2}")
    elif operacao.lower() == "dividir" or operacao == "/":
        print(f"o resultado da divisao e: {num1 / num2}")

    continuar = input("\nfazer outro calculo? (s/n): ")
    if continuar.lower() == "n":
        print("Fim! Obrigado! 👋")
        break