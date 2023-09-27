# Importando a classe GraficoDeBarrasBase do módulo GraficoDeBarrasBase
from GraficoDeBarrasBase import GraficoDeBarrasBase

# Definindo a classe GraficoDeBarrasRemedios que herda da classe GraficoDeBarrasBase
class GraficoDeBarrasRemedios(GraficoDeBarrasBase):
    def __init__(self, frame, anoSelecionado):
        # Chamando o construtor da classe base com os seguintes parâmetros:
        # - "Entrada - Remedios" como o título do gráfico de entrada
        # - "Saida - Remedios" como o título do gráfico de saída
        # - "Gráfico de Barras - Entrada e Saída de Medicamentos por Mês" como o título geral do gráfico
        # - frame como o argumento para o frame no qual o gráfico será exibido
        # - anoSelecionado como o ano para o qual os dados do gráfico serão filtrados
        super().__init__("Entrada - Remedios", "Saida - Remedios",
                         "Gráfico de Barras - Entrada e Saída de Medicamentos por Mês", frame, anoSelecionado)

# Definindo a classe GraficoDeBarrasIAB que herda da classe GraficoDeBarrasBase
class GraficoDeBarrasIAB(GraficoDeBarrasBase):
    def __init__(self, frame, anoSelecionado):
        # Chamando o construtor da classe base com os seguintes parâmetros:
        # - "Entrada - IAB" como o título do gráfico de entrada
        # - "Saida - IAB" como o título do gráfico de saída
        # - "Gráfico de Barras - Entrada e Saída de Itens de Atenção Básica por Mês" como o título geral do gráfico
        # - frame como o argumento para o frame no qual o gráfico será exibido
        # - anoSelecionado como o ano para o qual os dados do gráfico serão filtrados
        super().__init__("Entrada - IAB", "Saida - IAB",
                         "Gráfico de Barras - Entrada e Saída de Itens de Atenção Básica por Mês", frame, anoSelecionado)

# Definindo a classe GraficoDeBarrasVacinasCriancas que herda da classe GraficoDeBarrasBase
class GraficoDeBarrasVacinasCriancas(GraficoDeBarrasBase):
    def __init__(self, frame, anoSelecionado):
        # Chamando o construtor da classe base com os seguintes parâmetros:
        # - "Entrada - Vacinas1" como o título do gráfico de entrada
        # - "Saida - Vacinas1" como o título do gráfico de saída
        # - "Gráfico de Barras - Entrada e Saída de Vacinas (Crianças) por Mês" como o título geral do gráfico
        # - frame como o argumento para o frame no qual o gráfico será exibido
        # - anoSelecionado como o ano para o qual os dados do gráfico serão filtrados
        super().__init__("Entrada - Vacinas1", "Saida - Vacinas1",
                         "Gráfico de Barras - Entrada e Saída de Vacinas (Crianças) por Mês", frame, anoSelecionado)

# Definindo a classe GraficoDeBarrasVacinas que herda da classe GraficoDeBarrasBase
class GraficoDeBarrasVacinas(GraficoDeBarrasBase):
    def __init__(self, frame, anoSelecionado):
        # Chamando o construtor da classe base com os seguintes parâmetros:
        # - "Entrada - Vacinas2" como o título do gráfico de entrada
        # - "Saida - Vacinas2" como o título do gráfico de saída
        # - "Gráfico de Barras - Entrada e Saída de Vacinas (Adultos e Idosos) por Mês" como o título geral do gráfico
        # - frame como o argumento para o frame no qual o gráfico será exibido
        # - anoSelecionado como o ano para o qual os dados do gráfico serão filtrados
        super().__init__("Entrada - Vacinas2", "Saida - Vacinas2",
                         "Gráfico de Barras - Entrada e Saída de Vacinas (Adultos e Idosos) por Mês", frame, anoSelecionado)

# Definindo a classe GraficoDeBarrasTR que herda da classe GraficoDeBarrasBase
class GraficoDeBarrasTR(GraficoDeBarrasBase):
    def __init__(self, frame, anoSelecionado):
        # Chamando o construtor da classe base com os seguintes parâmetros:
        # - "Entrada - TR" como o título do gráfico de entrada
        # - "Saida - TR" como o título do gráfico de saída
        # - "Gráfico de Barras - Entrada e Saída de Testes Rápidos por Mês" como o título geral do gráfico
        # - frame como o argumento para o frame no qual o gráfico será exibido
        # - anoSelecionado como o ano para o qual os dados do gráfico serão filtrados
        super().__init__("Entrada - TR", "Saida - TR",
                         "Gráfico de Barras - Entrada e Saída de Testes Rápidos por Mês", frame, anoSelecionado)

# Definindo a classe GraficoDeBarrasDG que herda da classe GraficoDeBarrasBase
class GraficoDeBarrasDG(GraficoDeBarrasBase):
    def __init__(self, frame, anoSelecionado):
        # Chamando o construtor da classe base com os seguintes parâmetros:
        # - "Entrada - DG" como o título do gráfico de entrada
        # - "Saida - DG" como o título do gráfico de saída
        # - "Gráfico de Barras - Entrada e Saída de Itens de Distribuição Gratuita por Mês" como o título geral do gráfico
        # - frame como o argumento para o frame no qual o gráfico será exibido
        # - anoSelecionado como o ano para o qual os dados do gráfico serão filtrados
        super().__init__("Entrada - DG", "Saida - DG",
                         "Gráfico de Barras - Entrada e Saída de Itens de Distribuição Gratuita por Mês", frame, anoSelecionado)
