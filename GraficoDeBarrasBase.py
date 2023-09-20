import pandas as pd
import matplotlib.pyplot as plt

class GraficoDeBarrasBase:
    def __init__(self, entrada_col, saida_col, titulo):
        self.entrada_col = entrada_col
        self.saida_col = saida_col
        self.titulo = titulo
        self.dataset = self.create_dataset()

    def create_dataset(self):
        try:
            # Lê o arquivo CSV com os dados
            df = pd.read_csv("dados.csv", encoding="utf-8")

            saldo = 0
            dataset = {"Entrada": [], "Saída": [], "Saldo": []}

            # Itera pelas linhas do arquivo CSV
            for _, row in df.iterrows():
                mes = row["Mes"]
                entrada = int(row[self.entrada_col])
                saida = int(row[self.saida_col])
                saldo += entrada - saida
                dataset["Entrada"].append(entrada)
                dataset["Saída"].append(saida)
                dataset["Saldo"].append(saldo)

            df = pd.DataFrame(dataset)
            df.index = df.index + 1  # Índices começam em 1
            return df

        except Exception as e:
            # Em caso de erro na leitura do arquivo CSV, imprime o erro
            print(e)

    def create_chart(self):
        plt.figure(figsize=(14, 7))
        plt.title(self.get_titulo())
        plt.xlabel("Mês (de jun de 2022 a mai de 2023)")
        plt.ylabel("Quantidade de Insumos")
        plt.bar(self.dataset.index, self.dataset["Entrada"], label="Entrada")
        plt.bar(self.dataset.index, self.dataset["Saída"], label="Saída", bottom=self.dataset["Entrada"])
        plt.bar(self.dataset.index, self.dataset["Saldo"], label="Saldo", bottom=self.dataset["Entrada"] + self.dataset["Saída"])
        plt.legend()
        plt.xticks(self.dataset.index, self.dataset.index, rotation=45)
        plt.tight_layout()
        plt.show()

    def get_titulo(self):
        return self.titulo
