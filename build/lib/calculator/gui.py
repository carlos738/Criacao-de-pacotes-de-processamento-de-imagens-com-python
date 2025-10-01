import tkinter as tk
from calculator import somar, subtrair, multiplicar, dividir


def calcular():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operacao = operacao_var.get()
        if operacao == '+':
            resultado = somar(a, b)
        elif operacao == '-':
            resultado = subtrair(a, b)
        elif operacao == '*':
            resultado = multiplicar(a, b)
        elif operacao == '/':
            resultado = dividir(a, b)
        resultado_label.config(text=f"Resultado: {resultado}")
    except Exception as e:
        resultado_label.config(text=f"Erro: {e}")


root = tk.Tk()
root.title("Calculadora")

tk.Label(root, text="Número 1").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Número 2").pack()
entry2 = tk.Entry(root)
entry2.pack()

operacao_var = tk.StringVar(value='+')
tk.OptionMenu(root, operacao_var, '+', '-', '*', '/').pack()

tk.Button(root, text="Calcular", command=calcular).pack()
resultado_label = tk.Label(root, text="Resultado:")
resultado_label.pack()

root.mainloop()
