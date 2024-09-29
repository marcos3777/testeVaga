import os

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def pertence_fibonacci(num):
    a, b = 0, 1
    if num == 0 or num == 1:
        return True
    while b < num:
        a, b = b, a + b
    return b == num

while True:
    numero_str = input("Digite um número (ou 'sair' para finalizar): ").strip()

    # Verifica se o usuário deseja sair
    if numero_str.lower() == 'sair':
        print("Encerrando o programa.")
        break

    # Verifica se a entrada é um número válido
    if not numero_str.isdigit():
        limpar_console()
        print(f"Entrada inválida: '{numero_str}' não é um número positivo.")
        continue

    # Converte a entrada para um número inteiro
    numero = int(numero_str)

    # Verifica se o número é negativo
    if numero < 0:
        limpar_console()
        print(f"Entrada inválida: '{numero}' é um número negativo.")
        continue

    # Verifica se o número pertence à sequência de Fibonacci
    limpar_console()
    if pertence_fibonacci(numero):
        print(f"Número digitado: {numero}")
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"Número digitado: {numero}")
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
