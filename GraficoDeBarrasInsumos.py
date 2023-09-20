from GraficoDeBarrasBase import GraficoDeBarrasBase

class GraficoDeBarrasRemedios(GraficoDeBarrasBase):
    def __init__(self, frame):
        super().__init__("Entrada - Remedios", "Saida - Remedios",
                         "Gráfico de Barras - Entrada e Saída de Medicamentos por Mês", frame)

class GraficoDeBarrasIAB(GraficoDeBarrasBase):
    def __init__(self, frame):
        super().__init__("Entrada - IAB", "Saida - IAB",
                         "Gráfico de Barras - Entrada e Saída de Itens de Atenção Básica por Mês", frame)

class GraficoDeBarrasVacinasCriancas(GraficoDeBarrasBase):
    def __init__(self, frame):
        super().__init__("Entrada - Vacinas1", "Saida - Vacinas1",
                         "Gráfico de Barras - Entrada e Saída de Vacinas (Crianças) por Mês", frame)

class GraficoDeBarrasVacinas(GraficoDeBarrasBase):
    def __init__(self, frame):
        super().__init__("Entrada - Vacinas2", "Saida - Vacinas2",
                         "Gráfico de Barras - Entrada e Saída de Vacinas (Adultos e Idosos) por Mês", frame)

class GraficoDeBarrasTR(GraficoDeBarrasBase):
    def __init__(self, frame):
        super().__init__("Entrada - TR", "Saida - TR",
                         "Gráfico de Barras - Entrada e Saída de Testes Rápidos por Mês", frame)

class GraficoDeBarrasDG(GraficoDeBarrasBase):
    def __init__(self, frame):
        super().__init__("Entrada - DG", "Saida - DG",
                         "Gráfico de Barras - Entrada e Saída de Itens de Distribuição Gratuita por Mês", frame)

