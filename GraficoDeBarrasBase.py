from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class GraficoDeBarrasBase:
    def __init__(self, entrada_col, saida_col, titulo, frame):
        self.entrada_col = entrada_col
        self.saida_col = saida_col
        self.titulo = titulo
        self.frame = frame
        self.dataset = self.create_dataset()

    def create_dataset(self):
        try:
            # Lê o arquivo CSV com os dados
            df = pd.read_csv("dados.csv", encoding="utf-8")

            saldo = 0
            dataset = {"Entrada": [], "Saída": [], "Saldo": [], "Mes": []}

            # Itera pelas linhas do arquivo CSV
            for _, row in df.iterrows():
                mes = row["Mes"]
                entrada = int(row[self.entrada_col])
                saida = int(row[self.saida_col])
                saldo += entrada - saida
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

    def create_chart(self):
        if self.dataset is not None and not self.dataset.empty:  # Verifica se o dataset não é vazio
            self.figure = Figure(figsize=(12, 8))
            ax = self.figure.add_subplot(111)

            ax.set_title(self.titulo)
            ax.set_xlabel("Mês (de jun de 2022 a mai de 2023)")
            ax.set_ylabel("Quantidade de Insumos")

            ax.bar(self.dataset.index, self.dataset["Entrada"], label="Entrada")
            ax.bar(self.dataset.index, self.dataset["Saída"], label="Saída", bottom=self.dataset["Entrada"])
            ax.bar(self.dataset.index, self.dataset["Saldo"], label="Saldo",
                   bottom=self.dataset["Entrada"] + self.dataset["Saída"])

            ax.legend()
            ax.set_xticks(self.dataset.index)
            ax.set_xticklabels(self.dataset["Mes"], rotation=45)

            self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
            self.canvas_widget = self.canvas.get_tk_widget()
            self.canvas_widget.pack()
        else:
            print("O dataset está vazio ou não foi carregado corretamente.")


