# Importe o módulo 'os' que fornece funcionalidades relacionadas ao sistema operacional, como leitura de arquivos e diretórios.
import os
# Importe o módulo 'shutil' que oferece operações de alto nível para trabalhar com arquivos e diretórios.
import shutil
# Importe a biblioteca 'tkinter' que é usada para criar interfaces gráficas (GUI) simples.
import tkinter as tk
# Do módulo 'tkinter', importe o submódulo 'ttk' que fornece widgets de estilo temático adicionais.
from tkinter import ttk
# Importe a função 'filedialog' do módulo 'tkinter' para abrir caixas de diálogo para seleção de arquivos.
from tkinter import filedialog
# Importe a função 'messagebox' do módulo 'tkinter' para exibir caixas de diálogo de mensagem.
from tkinter import messagebox
# Importe a classe 'Image' e 'ImageTk' da biblioteca 'PIL' (Pillow) para trabalhar com imagens.
from PIL import Image, ImageTk
# Importe a classe 'ArquivoCSV' do arquivo 'ArquivoCSV.py' para lidar com operações relacionadas a arquivos CSV.
from ArquivoCSV import ArquivoCSV
# Importe a classe 'BotoesManager' do arquivo 'BotoesManager.py' para gerenciar os botões na interface.
from BotoesManager import BotoesManager
# Importe várias classes de gráficos de barras do arquivo 'GraficoDeBarrasInsumos.py'.
from GraficoDeBarrasInsumos import (
    GraficoDeBarrasRemedios, GraficoDeBarrasIAB, GraficoDeBarrasVacinasCriancas,
    GraficoDeBarrasVacinas, GraficoDeBarrasTR, GraficoDeBarrasDG
)
# A partir daqui, o código define a classe 'GUIUsuario' que herda de 'tk.Tk'.
class GUIUsuario(tk.Tk):
    # O método '__init__' é o construtor da classe 'GUIUsuario'.
    def __init__(self):
        # Chame o construtor da classe pai (tk.Tk) para inicializar a GUI.
        super().__init__()

        # Inicialize variáveis de instância.
        self.selectedCSVFile = None
        self.anoSelecionado = ""

        # Configura o título e tamanho inicial da janela.
        self.title('Monitor de Gerenciamento de Insumos - Coordenadoria de Ações Epidemiológicas')
        self.geometry('800x600')

        # Configure um estilo para os widgets.
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#c6e5b1')

        # Crie um canvas com a cor de fundo igual à cor do frame.
        self.canvas = tk.Canvas(self, bg='#c6e5b1')
        self.canvas.pack(side='top', fill='both', expand=True)

        # Adicione a imagem ao canvas e centralize-a.
        self.adicionar_imagem_centralizada()

        # Crie um painel de botões.
        self.painel_de_botoes = ttk.LabelFrame(self, padding=10, style='TFrame', relief='groove')
        self.painel_de_botoes.pack(fill='both', expand=True)

        # Crie frames vazios para organização.
        self.frame_vazio = ttk.Frame(self)
        self.frame_vazio.pack(fill='both', expand=True)

        # Crie um container para os botões.
        self.container_de_botoes = ttk.Frame(self.painel_de_botoes)
        self.container_de_botoes.pack(fill='both', expand=True)

        # Crie um botão para selecionar um arquivo CSV.
        self.botao_arquivo = ttk.Button(self.container_de_botoes, text='Selecionar Arquivo CSV', command=self.executar_mostrar_arquivo, style='TButton')
        self.botao_arquivo.pack(fill='both', expand=True)

        # Crie uma ComboBox para selecionar o ano.
        self.comboBoxAno = ttk.Combobox(self.container_de_botoes)
        self.comboBoxAno.pack(fill='both', expand=True)

        # Crie um painel para os botões de gráfico.
        self.graphButtonPanel = ttk.Frame(self.container_de_botoes)
        self.graphButtonPanel.pack(fill='both', expand=True)

        # Crie uma instância da classe ArquivoCSV para manipulação de arquivos CSV.
        self.arquivo_csv = ArquivoCSV(self.comboBoxAno)

        # Crie a interface do usuário.
        self.create_ui()

    # O método 'adicionar_imagem_centralizada' adiciona uma imagem centralizada no canvas.
    def adicionar_imagem_centralizada(self):
        # Carregue a imagem usando o Pillow (PIL).
        imagem = Image.open("logo.png")
        # Redimensione a imagem.
        imagem_redimensionada = imagem.resize((150, 150))
        # Crie uma instância da classe ImageTk.PhotoImage para exibir a imagem no tkinter.
        self.imagem = ImageTk.PhotoImage(imagem_redimensionada)

        # Adicione a imagem ao canvas na posição inicial (será ajustada posteriormente).
        self.imagem_no_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.imagem)

        # Vincule o evento de redimensionamento do Canvas a uma função de ajuste.
        self.canvas.bind("<Configure>", self.ajustar_imagem)

    # O método 'ajustar_imagem' ajusta a posição da imagem quando o tamanho do canvas é alterado.
    def ajustar_imagem(self, event):
        # Obtenha as novas dimensões do canvas.
        canvas_width = event.width
        canvas_height = event.height

        # Calcule a nova posição central para a imagem.
        x = (canvas_width - self.imagem.width()) / 2
        y = (canvas_height - self.imagem.height()) / 2

        # Ajuste a posição da imagem no canvas.
        self.canvas.coords(self.imagem_no_canvas, x, y)

    # O método 'create_ui' cria os botões de gráfico e os associa a suas respectivas funções de exibição.
    def create_ui(self):
        self.botoes_manager = BotoesManager(self.graphButtonPanel, self.mostrar_grafico)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - Remedios', GraficoDeBarrasRemedios)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - IAB', GraficoDeBarrasIAB)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - Vacinas1', GraficoDeBarrasVacinasCriancas)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - Vacinas2', GraficoDeBarrasVacinas)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - TR', GraficoDeBarrasTR)
        self.botoes_manager.criar_botao_grafico('Gráfico de Barras - DG', GraficoDeBarrasDG)

    # O método 'mostrar_grafico' exibe uma nova janela com um gráfico selecionado.
    def mostrar_grafico(self, grafo_class):
        ano_selecionado = self.comboBoxAno.get()

        if not ano_selecionado:
            # Exibe uma mensagem de erro se nenhum ano foi selecionado.
            messagebox.showerror("Erro", "Selecione um ano antes de criar o gráfico.")
            return

        # Cria uma nova janela para exibir o gráfico.
        nova_janela = tk.Toplevel(self)
        nova_janela.title(f'Gráfico de {grafo_class.__name__}')
        nova_janela.geometry('1400x700')

        # Cria uma instância da classe de gráfico selecionada e exibe o gráfico.
        grafico = grafo_class(nova_janela, ano_selecionado)
        grafico.create_chart()

    # O método 'executar_mostrar_arquivo' abre uma caixa de diálogo para selecionar um arquivo CSV.
    def executar_mostrar_arquivo(self):
        if os.path.exists("dados.csv"):
            arquivo_selecionado = "dados.csv"
        else:
            arquivo_selecionado = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
            if not arquivo_selecionado:
                return

            # Copie o arquivo selecionado para "dados.csv" e exiba uma mensagem de sucesso.
            shutil.copy(arquivo_selecionado, "dados.csv")
            messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso!")

        # Atualize a instância da classe ArquivoCSV com o novo arquivo selecionado.
        self.arquivo_csv = ArquivoCSV(self.comboBoxAno)
        self.lista_anos = self.arquivo_csv.atualizar_arquivo_csv()

