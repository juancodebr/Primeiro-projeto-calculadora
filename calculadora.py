#Importar bibliotecas
import tkinter as tk
#Funções de chamada, limpar e calcular
def click(num):
    entry.insert (tk.END, num)
def clear():
    entry.delete(0, tk.END)
def calculate():
    try:
        result=eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert (tk.END, str(result))
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END, "Erro")


#Cria a janela principal do titulo 
root=tk.Tk()
root.title('Calculadora simples')  
#4 Cria o campo de entrada e o campo dos resultados 
entry=tk.Entry(root, width=20, borderwidth=5, font=("Arial",14))
entry.grid(row=0, column=0, columnspan=4 )

#5 Lista com rotulos de cada botão (números e operadores)
buttons=[
     '7','8','9','+',
     '4','5','6','-',
     '1','2','3','*',
     '0','C','=','/',
]
row,col=1,0
# Loop que cria e posiciona cada botão
for b in buttons:
    if b == 'C':
        action = clear
    elif b == '=':
        action = calculate
    else:
        action = lambda x=b: click(x)

    btn = tk.Button(root, text=b, width=5, height=2, command=action)
    btn.grid(row=row, column=col)

    col += 1

    if col > 3:
        col = 0
        row += 1

root.mainloop()