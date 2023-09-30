import tkinter as tk
from tkinter import ttk

class BotoesManager(tk.Frame):
    def __init__(self, painel, mostrar_grafico_callback, master=None):
        super().__init__(master)
        self.painel = painel
        self.mostrar_grafico_callback = mostrar_grafico_callback

    def criar_botao_grafico(self, titulo, grafo_class):
        botao_grafico = ttk.Button(self.painel, text=titulo, command=lambda: self.mostrar_grafico_callback(grafo_class))
        botao_grafico.pack(fill='both', expand=True)

