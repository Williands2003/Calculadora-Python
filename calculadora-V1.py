def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"
#-------------------------------------------------------------------------------------------

#aqui vou fazer o menu principal, e a implementação das funções
def calculadora():
    while True:
        print("Menu:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Escolha a operação (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de inserir números.")
            continue

        if escolha == '1':
            resultado = adicao(num1, num2)
            print(f"Resultado: {resultado}")
        elif escolha == '2':
            resultado = subtracao(num1, num2)
            print(f"Resultado: {resultado}")
        elif escolha == '3':
            resultado = multiplicacao(num1, num2)
            print(f"Resultado: {resultado}")
        elif escolha == '4':
            resultado = divisao(num1, num2)
            print(f"Resultado: {resultado}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora()