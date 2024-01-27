import tkinter as tk

#Janela
janela=tk.Tk()
janela["bg"]="red"
janela.title("Calculadora")
janela.geometry("185x100+550+300")

#Labels
lb1=tk.Label(janela, text="1º valor", bg="red", fg="white")
lb1.grid(row=0,column=0)

lb2=tk.Label(janela, text="2º valor", bg="red", fg="white")
lb2.grid(row=1,column=0)

lb3=tk.Label(janela, text="", bg="red", fg="white")
lb3.grid(row=3,column=0)

#Caixas de textos
v1=tk.Entry(janela, width=22)
v1.grid(row=0,column=1, columnspan=3)

v2=tk.Entry(janela, width=22)
v2.grid(row=1,column=1, columnspan=3)

#Botões
def bt_1():
    lb3['text']=float(v1.get())+float(v2.get())
    
def bt_2():
    lb3['text']=float(v1.get())-float(v2.get())
    
def bt_3():
    lb3['text']=float(v1.get())*float(v2.get())
    
def bt_4():
    lb3['text']=float(v1.get())/float(v2.get())

bt1=tk.Button(janela, width=3, text="+", command=bt_1)
bt1.grid(row=2, column=0, pady=5)

bt2=tk.Button(janela, width=3, text="-", command=bt_2)
bt2.grid(row=2, column=1, pady=5)

bt3=tk.Button(janela, width=3, text="*", command=bt_3)
bt3.grid(row=2, column=2,  pady=5)

bt4=tk.Button(janela, width=3, text="/", command=bt_4)
bt4.grid(row=2, column=3,  pady=5)

janela.mainloop()