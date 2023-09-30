from ArquivoCSV import ArquivoCSV
from BotoesManager import BotoesManager
from GraficoDeBarrasInsumos import (
    GraficoDeBarrasRemedios, GraficoDeBarrasIAB, GraficoDeBarrasVacinasCriancas,
    GraficoDeBarrasVacinas, GraficoDeBarrasTR, GraficoDeBarrasDG
)


import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from PIL import Image, ImageTk

class GUIUsuario(tk.Tk):
    def __init__(self):
        super().__init__()

        self.selectedCSVFile = None
        self.anoSelecionado = ""

        self.title('Monitor de Gerenciamento de Insumos - Coordenadoria de Ações Epidemiológicas')
        self.geometry('800x600')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#c6e5b1')

        # Crie um canvas com a cor de fundo igual à cor do frame
        self.canvas = tk.Canvas(self, bg='#c6e5b1')
        self.canvas.pack(side='top', fill='both', expand=True)  # Empacote o canvas aqui

        # Adicione a imagem ao canvas e centralize-a
        self.adicionar_imagem_centralizada()

        self.painel_de_botoes = ttk.LabelFrame(self, padding=10, style='TFrame', relief='groove')
        self.painel_de_botoes.pack(fill='both', expand=True)

        self.frame_vazio = ttk.Frame(self)
        self.frame_vazio.pack(fill='both', expand=True)

        self.container_de_botoes = ttk.Frame(self.painel_de_botoes)
        self.container_de_botoes.pack(fill='both', expand=True)

        # Crie um botão para selecionar um arquivo CSV
        self.botao_arquivo = ttk.Button(self.container_de_botoes, text='Selecionar Arquivo CSV', command=self.executar_mostrar_arquivo, style='TButton')
        self.botao_arquivo.pack(fill='both', expand=True)

        self.comboBoxAno = ttk.Combobox(self.container_de_botoes)
        self.comboBoxAno.pack(fill='both', expand=True)

        self.graphButtonPanel = ttk.Frame(self.container_de_botoes)
        self.graphButtonPanel.pack(fill='both', expand=True)

        self.arquivo_csv = ArquivoCSV(self.comboBoxAno)

        self.create_ui()


    def adicionar_imagem_centralizada(self):
        # Carregue a imagem usando o Pillow (PIL)
        imagem = Image.open("logo.png")  # Substitua "logo.png" pelo caminho da sua imagem
        imagem_redimensionada = imagem.resize((150, 150))
        self.imagem = ImageTk.PhotoImage(imagem_redimensionada)

        # Adicione a imagem ao canvas na posição inicial (será ajustada posteriormente)
        self.imagem_no_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.imagem)

        # Vincule o evento de redimensionamento do Canvas a uma função de ajuste
        self.canvas.bind("<Configure>", self.ajustar_imagem)

    def ajustar_imagem(self, event):
        # Obtenha as novas dimensões do canvas
        canvas_width = event.width
        canvas_height = event.height

        # Calcule a nova posição central para a imagem
        x = (canvas_width - self.imagem.width()) / 2
        y = (canvas_height - self.imagem.height()) / 2

        # Ajuste a posição da imagem no canvas
        self.canvas.coords(self.imagem_no_canvas, x, y)


    def create_ui(self):
        self.botoes_manager = BotoesManager(self.graphButtonPanel, self.mostrar_grafico)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - Remedios', GraficoDeBarrasRemedios)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - IAB', GraficoDeBarrasIAB)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - Vacinas1', GraficoDeBarrasVacinasCriancas)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - Vacinas2', GraficoDeBarrasVacinas)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - TR', GraficoDeBarrasTR)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - DG', GraficoDeBarrasDG)

    def mostrar_grafico(self, grafo_class):
        ano_selecionado = self.comboBoxAno.get()

        if not ano_selecionado:
            messagebox.showerror("Erro", "Selecione um ano antes de criar o gráfico.")
            return

        nova_janela = tk.Toplevel(self)
        nova_janela.title(f'Gráfico de {grafo_class.__name__}')
        nova_janela.geometry('1400x700')

        grafico = grafo_class(nova_janela, ano_selecionado)
        grafico.create_chart()

    def executar_mostrar_arquivo(self):
        if os.path.exists("dados.csv"):
            arquivo_selecionado = "dados.csv"
        else:
            arquivo_selecionado = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
            if not arquivo_selecionado:
                return

            shutil.copy(arquivo_selecionado, "dados.csv")
            messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso!")

        self.arquivo_csv = ArquivoCSV(self.comboBoxAno)
        self.lista_anos = self.arquivo_csv.atualizar_arquivo_csv()



