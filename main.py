from GraficoDeBarrasBase import GraficoDeBarrasBase
from GraficoDeBarrasInsumos import GraficoDeBarrasRemedios, GraficoDeBarrasIAB, GraficoDeBarrasVacinasCriancas, \
    GraficoDeBarrasVacinas, GraficoDeBarrasTR, GraficoDeBarrasDG
import tkinter as tk
from tkinter import ttk

def mostrar_grafico(grafo_class):
    nova_janela = tk.Toplevel(window)
    nova_janela.title(f'Gráfico de {grafo_class.__name__}')
    nova_janela.geometry('1400x700')

    # Crie uma instância da classe de gráfico com os argumentos necessários
    grafico = grafo_class(nova_janela)
    grafico.create_chart()

# Cria a janela principal
window = tk.Tk()
window.title('Exemplo de GUI com Gráfico')
window.geometry('800x400')

# Cria botões para cada tipo de gráfico
botao_remedios = ttk.Button(window, text='Gráfico de Barras - Medicamentos', command=lambda: mostrar_grafico(GraficoDeBarrasRemedios))
botao_iab = ttk.Button(window, text='Gráfico de Barras - Itens de Atenção Básica', command=lambda: mostrar_grafico(GraficoDeBarrasIAB))
botao_vacinas_criancas = ttk.Button(window, text='Gráfico de Barras - Vacinas (Crianças)', command=lambda: mostrar_grafico(GraficoDeBarrasVacinasCriancas))
botao_vacinas = ttk.Button(window, text='Gráfico de Barras - Vacinas (Adultos e Idosos)', command=lambda: mostrar_grafico(GraficoDeBarrasVacinas))
botao_tr = ttk.Button(window, text='Gráfico de Barras - Testes Rápidos', command=lambda: mostrar_grafico(GraficoDeBarrasTR))
botao_dg = ttk.Button(window, text='Gráfico de Barras - Itens de Distribuição Gratuita', command=lambda: mostrar_grafico(GraficoDeBarrasDG))

# Empacote os botões na janela
botao_remedios.pack()
botao_iab.pack()
botao_vacinas_criancas.pack()
botao_vacinas.pack()
botao_tr.pack()
botao_dg.pack()

# Inicia a interface gráfica
window.mainloop()