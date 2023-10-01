import tkinter as tk
from tkinter import ttk

class BotoesManager(tk.Frame):
    def __init__(self, painel, mostrar_grafico_callback, master=None):
        super().__init__(master)
        self.painel = painel  # O painel onde os botões serão colocados
        self.mostrar_grafico_callback = mostrar_grafico_callback  # Função de callback para mostrar o gráfico

    def criar_botao_grafico(self, titulo, grafo_class):
        # Cria um botão com o título especificado e configura o comando para chamar a função de callback
        botao_grafico = ttk.Button(self.painel, text=titulo, command=lambda: self.mostrar_grafico_callback(grafo_class))
        botao_grafico.pack(fill='both', expand=True)  # Adiciona o botão ao painel e configura o preenchimento e expansão
