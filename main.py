# Importa as bibliotecas necessárias para criar a interface gráfica
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from GraficoDeBarrasInsumos import *  # Importa classes para a criação de gráficos


# Classe principal que define a interface gráfica do usuário
class GUIUsuario:
    def __init__(self):
        # Inicializa variáveis de classe para armazenar informações do arquivo selecionado e do ano selecionado
        self.selectedCSVFile = None
        self.anoSelecionado = ""

        # Cria uma janela principal
        self.window = tk.Tk()
        self.window.title('Monitor de Gerenciamento de Insumos - Coordenadoria de Ações Epidemiológicas')
        self.window.geometry('800x600')
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)

        # Chama o método para criar a interface gráfica
        self.create_ui()

    # Método para criar a interface gráfica
    def create_ui(self):
        # Cria um painel de botões
        self.painel_de_botoes = ttk.LabelFrame(self.window, text='Gerenciador', padding=10)
        self.painel_de_botoes.pack(fill='both', expand=True)

        # Cria um frame vazio
        self.frame_vazio = ttk.Frame(self.window)
        self.frame_vazio.pack(fill='both', expand=True)

        # Cria um container para os botões
        self.container_de_botoes = ttk.Frame(self.painel_de_botoes)
        self.container_de_botoes.pack(fill='both', expand=True)

        # Cria um botão para selecionar um arquivo CSV
        self.botao_arquivo = ttk.Button(self.painel_de_botoes, text='Selecionar Arquivo CSV',
                                        command=self.receber_arquivo)
        self.botao_arquivo.pack(fill='both', expand=True)

        # Cria uma caixa de combinação para selecionar o ano
        self.comboBoxAno = ttk.Combobox(self.container_de_botoes)
        self.comboBoxAno.pack(fill='both', expand=True)

        # Cria um painel de botões para os gráficos
        self.graphButtonPanel = ttk.Frame(self.container_de_botoes)
        self.graphButtonPanel.pack(fill='both', expand=True)

        # Cria botões para gerar diferentes tipos de gráficos
        # Botão para Gráfico de Barras - Remedios
        self.botao_grafico_remedios = ttk.Button(self.graphButtonPanel, text='Gráfico de Barras - Remedios',
                                                 command=lambda: self.mostrar_grafico(GraficoDeBarrasRemedios))
        self.botao_grafico_remedios.pack(fill='both', expand=True)

        # Botão para Gráfico de Barras - IAB
        self.botao_grafico_iab = ttk.Button(self.graphButtonPanel, text='Gráfico de Barras - IAB',
                                            command=lambda: self.mostrar_grafico(GraficoDeBarrasIAB))
        self.botao_grafico_iab.pack(fill='both', expand=True)

        # Botão para Gráfico de Barras - Vacinas1
        self.botao_grafico_vacinas1 = ttk.Button(self.graphButtonPanel, text='Gráfico de Barras - Vacinas1',
                                                 command=lambda: self.mostrar_grafico(GraficoDeBarrasVacinasCriancas))
        self.botao_grafico_vacinas1.pack(fill='both', expand=True)

        # Botão para Gráfico de Barras - Vacinas2
        self.botao_grafico_vacinas2 = ttk.Button(self.graphButtonPanel, text='Gráfico de Barras - Vacinas2',
                                                 command=lambda: self.mostrar_grafico(GraficoDeBarrasVacinas))
        self.botao_grafico_vacinas2.pack(fill='both', expand=True)

        # Botão para Gráfico de Barras - TR
        self.botao_grafico_tr = ttk.Button(self.graphButtonPanel, text='Gráfico de Barras - TR',
                                           command=lambda: self.mostrar_grafico(GraficoDeBarrasTR))
        self.botao_grafico_tr.pack(fill='both', expand=True)

        # Botão para Gráfico de Barras - DG
        self.botao_grafico_dg = ttk.Button(self.graphButtonPanel, text='Gráfico de Barras - DG',
                                           command=lambda: self.mostrar_grafico(GraficoDeBarrasDG))
        self.botao_grafico_dg.pack(fill='both', expand=True)

        # Chama o método para atualizar as opções da caixa de combinação com os anos disponíveis
        self.atualizar_combobox_ano()

        # Inicia o loop principal da janela
        self.window.mainloop()

    # Método para receber e copiar o arquivo CSV selecionado
    def receber_arquivo(self):
        try:
            arquivo_selecionado = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
            if arquivo_selecionado:
                # Copia o arquivo selecionado para "dados.csv"
                shutil.copy(arquivo_selecionado, "dados.csv")
                messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso!")
                # Atualiza as opções da caixa de combinação de anos
                self.atualizar_combobox_ano()
        except Exception as e:
            # Exibe uma mensagem de erro em caso de falha
            messagebox.showerror("Erro", f"Ocorreu um erro ao copiar o arquivo: {str(e)}")

    # Método para atualizar as opções da caixa de combinação com os anos disponíveis no arquivo CSV
    def atualizar_combobox_ano(self):
        anos_set = set()
        try:
            with open("dados.csv", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines[1:]:
                    columns = line.strip().split(",")
                    if len(columns) > 0 and columns[0].isdigit():
                        anos_set.add(columns[0])
        except Exception as e:
            print(e)

        anos_list = sorted(list(anos_set), reverse=True)
        self.comboBoxAno["values"] = anos_list
        if anos_list:
            self.comboBoxAno.set(anos_list[0])

    # Método para mostrar um gráfico em uma nova janela
    def mostrar_grafico(self, grafo_class):
        nova_janela = tk.Toplevel(self.window)
        nova_janela.title(f'Gráfico de {grafo_class.__name__}')
        nova_janela.geometry('1400x700')

        ano_selecionado = self.comboBoxAno.get()
        grafico = grafo_class(nova_janela, ano_selecionado)
        grafico.create_chart()


# Função principal para iniciar o aplicativo
if __name__ == "__main__":
    import shutil

    app = GUIUsuario()
