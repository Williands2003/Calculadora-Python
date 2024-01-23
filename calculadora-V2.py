

import tkinter as tk  # Importa o módulo tkinter e o renomeia como tk
from tkinter import messagebox  # Importa a classe messagebox do módulo tkinter

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
        messagebox.showerror("Erro", "Divisão por zero não permitida.")
        return None

def calcular():
    try:#Código que pode gerar uma exceção-
        #O bloco try em Python é utilizado para envolver um trecho de código onde podem ocorrer exceções, permitindo que o programa lide com possíveis erros de forma controlada e evite interrupções inesperadas. 
         #Em caso de exceção 
        num1 = float(entry_num1.get())  # recebe e converte o valor do primeiro Entry para float
        num2 = float(entry_num2.get())  # recebe e converte o valor do segundo Entry para float
    except ValueError:#o bloco except correspondente é executado, proporcionando a oportunidade de tratar ou registrar o erro.
        messagebox.showerror("Erro", "Certifique-se de inserir números válidos.")
        return

    escolha = operacoes.get()  # Obtém a escolha da operação a partir do widget Combobox

    if escolha == 'Adição':
        resultado = adicao(num1, num2)
    elif escolha == 'Subtração':
        resultado = subtracao(num1, num2)
    elif escolha == 'Multiplicação':
        resultado = multiplicacao(num1, num2)
    elif escolha == 'Divisão':
        resultado = divisao(num1, num2)
    else:
        messagebox.showerror("Erro", "Selecione uma operação válida.")
        return

    if resultado is not None:
        messagebox.showinfo("Resultado", f"Resultado: {resultado}")

# Cria uma instância da classe Tk, que é a janela principal
root = tk.Tk()

# Definindo o título da janela
root.title("Calculadora Simples")

# Cria dois widgets Entry para a inserção dos números
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

# Cria um widget Combobox para selecionar a operação
operacoes = tk.StringVar()
operacoes.set("Adição")  # Define a operação padrão como Adição
opcoes_operacoes = tk.OptionMenu(root, operacoes, "Adição", "Subtração", "Multiplicação", "Divisão")

# Cria um botão para executar o cálculo
botao_calcular = tk.Button(root, text="Calcular", command=calcular)

# Define a disposição dos widgets na janela
entry_num1.pack()
entry_num2.pack()
opcoes_operacoes.pack()
botao_calcular.pack()

# Inicia o loop principal da aplicação tkinter
root.mainloop()

# daqui pra baixo o chatgpt me ajudou bastante ainda não sei usar o tkinter sem ajuda, usei um comando mais ou menos assim: "me ajude a transformar o codigo em interativo com uma tela propria, mas não escreva, apenas vá me guiando nas etapas"
# Configuração da interface gráfica
app = tk.Tk()
app.title("Calculadora pika")


# aqui vai ser as cores
cor_fundo = "#110101"  # Cor do fundo, peguei as paletas com uma estensão do google
cor_botao = "#010511"  # Cor dos botões
cor_texto = "#333333"  # Cor do texto
#ficou feio mas o importante é que foi feito com amor, eu amo meu filho da forma que ele veio ao mundo

#cores de fundo
app.configure(bg=cor_fundo)#o chat tentou me explicar isso mas entendi nada com nada


#essa parte se eu falar que fui eu é mentira pura
# Entradas
entry_num1 = tk.Entry(app, width=10)
entry_num1.grid(row=0, column=0, padx=6, pady=6)

entry_num2 = tk.Entry(app, width=12)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

# Menu de operações
operacoes = tk.StringVar(app)
operacoes.set('Adição')  # Valor padrão
menu_operacoes = tk.OptionMenu(app, operacoes, 'Adição', 'Subtração', 'Multiplicação', 'Divisão')
menu_operacoes.grid(row=0, column=3, padx=5, pady=5)

# Botão de cálculo
botao_calcular = tk.Button(app, text="Calcular", command=calcular)
botao_calcular.grid(row=1, column=2, columnspan=4, pady=10)

# Rodar a interface
app.mainloop()
