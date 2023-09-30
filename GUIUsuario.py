import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import shutil

from ArquivoCSV import ArquivoCSV
from BotoesManager import BotoesManager
from GraficoDeBarrasInsumos import (
    GraficoDeBarrasRemedios, GraficoDeBarrasIAB, GraficoDeBarrasVacinasCriancas,
    GraficoDeBarrasVacinas, GraficoDeBarrasTR, GraficoDeBarrasDG
)

# Classe principal que define a interface gráfica do usuário
class GUIUsuario(tk.Tk):
    def __init__(self):
        super().__init__()

        # Inicializa variáveis de classe para armazenar informações do arquivo selecionado e do ano selecionado
        self.selectedCSVFile = None
        self.anoSelecionado = ""

        # Configura a janela principal
        self.title('Monitor de Gerenciamento de Insumos - Coordenadoria de Ações Epidemiológicas')
        self.geometry('800x600')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Cria um painel de botões
        self.painel_de_botoes = ttk.LabelFrame(self, text='Gerenciador', padding=10)
        self.painel_de_botoes.pack(fill='both', expand=True)

        # Cria um frame vazio
        self.frame_vazio = ttk.Frame(self)
        self.frame_vazio.pack(fill='both', expand=True)

        # Cria um container para os botões
        self.container_de_botoes = ttk.Frame(self.painel_de_botoes)
        self.container_de_botoes.pack(fill='both', expand=True)

        # Cria um botão para selecionar um arquivo CSV
        self.botao_arquivo = ttk.Button(self.painel_de_botoes, text='Selecionar Arquivo CSV',
                                        command=self.executar_mostrar_arquivo)
        self.botao_arquivo.pack(fill='both', expand=True)

        # Cria uma caixa de combinação para selecionar o ano
        self.comboBoxAno = ttk.Combobox(self.container_de_botoes)
        self.comboBoxAno.pack(fill='both', expand=True)

        # Cria um painel de botões para os gráficos
        self.graphButtonPanel = ttk.Frame(self.container_de_botoes)
        self.graphButtonPanel.pack(fill='both', expand=True)

        # Crie uma instância da classe ArquivoCSV após criar a combobox
        self.arquivo_csv = ArquivoCSV(self.comboBoxAno)

        # Chama o método para criar a interface gráfica
        self.create_ui()

    # Método para criar a interface gráfica
    def create_ui(self):
        # Crie uma instância de BotoesManager e passe o painel e o callback para mostrar gráfico
        self.botoes_manager = BotoesManager(self.graphButtonPanel, self.mostrar_grafico)

        # Use o BotoesManager para criar os botões de gráficos
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
        # Verifica se já existe um arquivo "dados.csv" no diretório atual
        if os.path.exists("dados.csv"):
            arquivo_selecionado = "dados.csv"
        else:
            # Se não existir, permite ao usuário selecionar um arquivo
            arquivo_selecionado = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
            if not arquivo_selecionado:
                # Se o usuário não selecionar um arquivo, saia do método
                return

            # Copia o arquivo selecionado para "dados.csv"
            shutil.copy(arquivo_selecionado, "dados.csv")
            messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso!")

        # Atualiza as opções da caixa de combinação de anos
        self.arquivo_csv = ArquivoCSV(self.comboBoxAno)
        self.lista_anos = self.arquivo_csv.atualizar_arquivo_csv()

