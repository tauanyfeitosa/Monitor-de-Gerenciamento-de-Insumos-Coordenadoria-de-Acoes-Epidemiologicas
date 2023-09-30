# Importa as bibliotecas necessárias
import pandas as pd  # Para manipulação de dados em formato tabular
import matplotlib.pyplot as plt  # Para criação de gráficos
import numpy as np  # Para manipulação numérica
import tkinter as tk  # Para criação de interfaces gráficas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Para incorporar gráficos em uma interface gráfica

# Define uma classe chamada GraficoDeBarrasBase
class GraficoDeBarrasBase:
    # O método __init__ é chamado quando um objeto da classe é criado
    def __init__(self, entrada_col, saida_col, titulo, frame, anoSelecionado):
        # Inicializa os atributos da classe com os valores passados como parâmetros
        self.entrada_col = entrada_col  # Nome da coluna de entrada
        self.saida_col = saida_col  # Nome da coluna de saída
        self.titulo = titulo  # Título do gráfico
        self.frame = frame  # O frame onde o gráfico será exibido
        self.anoSelecionado = int(anoSelecionado)  # Ano selecionado para exibir dados
        self.dataset = self.create_dataset()  # Chama o método para criar o conjunto de dados
        self.create_chart()  # Chama o método para criar o gráfico

    # Método para criar o conjunto de dados
    def create_dataset(self):
        try:
            # Lê o arquivo CSV com os dados
            df = pd.read_csv("dados.csv", encoding="utf-8")

            records = df.to_dict(orient="records")
            records.sort(key=lambda x: x["Ano"])

            saldo_por_ano = {}
            saldo_anterior = 0

            #lógica para a construção do saldo total de todos os anos contidos no csv

            for record in records:
                ano = record["Ano"]
                entrada = int(record[self.entrada_col])
                saida = int(record[self.saida_col])
                saldo_anterior = saldo_anterior + entrada - saida
                saldo_por_ano[ano] = saldo_anterior

            contador = 0
            saldo = 0
            dataset = {"Entrada": [], "Saída": [], "Saldo": [], "Mes": []}

            #lógica para a construção do dataset a partir do mês selecionado pelo usuário
            for record in records:
                ano = record["Ano"]
                mes = record["Mes"]

                if int(ano) == self.anoSelecionado:
                    entrada = int(record[self.entrada_col])
                    saida = int(record[self.saida_col])
                    ano_anterior = int(ano) - 1
                    contador += 1

                    """"#lógica para, caso o ano não seja único ou o mais antigo do csv, utilizar o dado do dicionário 
                    construído, cado contrário, seu saldo anterior inicia em 0"""
                    if contador == 1 and ano_anterior in saldo_por_ano:
                        saldo = saldo_por_ano[ano_anterior] + entrada - saida
                    else:
                        saldo = saldo + entrada - saida

                    dataset["Entrada"].append(entrada)
                    dataset["Saída"].append(saida)
                    dataset["Saldo"].append(saldo)
                    dataset["Mes"].append(mes)

            df = pd.DataFrame(dataset)
            df.index = df.index + 1  # Índices começam em 1
            return df

        except Exception as e:
            # Em caso de erro na leitura do arquivo CSV, imprime o erro
            print(e)
            return None

    # Método para criar o gráfico
    def create_chart(self):
        if self.dataset is not None and not self.dataset.empty:
            self.figure = plt.figure(figsize=(12, 8))
            ax = self.figure.add_subplot(111) #define que o gráfico deve ocupar 100% da plotagem

            ax.set_title(self.titulo) #título do gráfico
            ax.set_xlabel(f"Mês (referente ao ano de {self.anoSelecionado})") #legenda do eixo x
            ax.set_ylabel("Quantidade de Insumos") #legenda do eixo y

            bar_width = 0.2 #determina a largura das barras do gráfico
            x = np.arange(len(self.dataset["Mes"]))
            """cria um array x que contém uma sequência de números inteiros de 0 
            até (número de meses - 1), onde cada número inteiro representa a posição horizontal de uma barra no gráfico de 
            barras. Isso garante que as barras sejam espaçadas igualmente ao longo do eixo horizontal do gráfico, com cada
            número inteiro correspondendo a uma posição de mês."""

            #logica para a criação de 3 barras agrupadas para o mesmo mês
            entrada_bars = ax.bar(x - bar_width, self.dataset["Entrada"], label="Entrada", width=bar_width, color='red')
            saida_bars = ax.bar(x, self.dataset["Saída"], label="Saída", width=bar_width, color='blue')
            saldo_bars = ax.bar(x + bar_width, self.dataset["Saldo"], label="Saldo", width=bar_width, color='green')

            ax.legend() #insere a legenda
            ax.set_xticks(x) #define o local dos marcadores do eixo x
            ax.set_xticklabels(self.dataset["Mes"], rotation=45)  # Rotacionar os rótulos dos meses em 45 graus e nomeia

            #adiciona o valor da barra em 90 graus
            for bar in entrada_bars + saida_bars + saldo_bars:
                height = bar.get_height()
                ax.annotate('{}'.format(height),
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom', rotation=90)  # Rotacionar os números em 90°

            # Aumenta o limite do eixo y em +50 para que os valores da barra não coincidam com a margem
            ax.set_ylim(ax.get_ylim()[0], ax.get_ylim()[1] + 50)

            #adiciona a figura a um novo frame
            canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
            canvas.get_tk_widget().pack()

        else:
            print("O dataset está vazio ou não foi carregado corretamente.")