from GraficoDeBarrasBase import GraficoDeBarrasBase


class GraficoDeBarrasRemedios(GraficoDeBarrasBase):
    def __init__(self):
        super().__init__("Entrada - Remedios", "Saida - Remedios",
                         "Gráfico de Barras - Entrada e Saída de Medicamentos por Mês")


class GraficoDeBarrasIAB(GraficoDeBarrasBase):
    def __init__(self):
        super().__init__("Entrada - IAB", "Saida - IAB",
                         "Gráfico de Barras - Entrada e Saída de Itens de Atenção Básica por Mês")

class GraficoDeBarrasVacinasCriancas(GraficoDeBarrasBase):
    def __init__(self):
        super().__init__("Entrada - Vacinas1", "Saida - Vacinas1",
                         "Gráfico de Barras - Entrada e Saída de Vacinas (Crianças) por Mês")

class GraficoDeBarrasVacinas(GraficoDeBarrasBase):
    def __init__(self):
        super().__init__("Entrada - Vacinas2", "Saida - Vacinas2",
                         "Gráfico de Barras - Entrada e Saída de Vacinas (Adultos e Idosos) por Mês")

class GraficoDeBarrasTR(GraficoDeBarrasBase):
    def __init__(self):
        super().__init__("Entrada - TR", "Saida - TR",
                         "Gráfico de Barras - Entrada e Saída de Testes Rápidos por Mês")

class GraficoDeBarrasDG(GraficoDeBarrasBase):
    def __init__(self):
        super().__init__("Entrada - DG", "Saida - DG",
                         "Gráfico de Barras - Entrada e Saída de Itens de Distribuição Gratuita por Mês")


# Exemplo de uso
grafico1 = GraficoDeBarrasVacinasCriancas()
grafico1.create_chart()
