from GraficoDeBarrasBase import GraficoDeBarrasBase
from GraficoDeBarrasInsumos import GraficoDeBarrasRemedios, GraficoDeBarrasIAB, GraficoDeBarrasVacinasCriancas, \
    GraficoDeBarrasVacinas, GraficoDeBarrasTR, GraficoDeBarrasDG
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox  # Importe a biblioteca messagebox

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

# Função para receber e salvar o arquivo CSV
def receber_arquivo():
    try:
        # Abre uma caixa de diálogo para o usuário selecionar o arquivo CSV
        arquivo_selecionado = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])

        # Verifica se um arquivo foi selecionado
        if arquivo_selecionado:
            # Copie o arquivo selecionado para a raiz do projeto
            import shutil
            arquivo_destino = "dados.csv"
            shutil.copy(arquivo_selecionado, arquivo_destino)
            messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao copiar o arquivo: {str(e)}")

# Cria um botão para receber um arquivo CSV do usuário
botao_arquivo = ttk.Button(window, text='Selecionar Arquivo CSV', command=receber_arquivo)
botao_arquivo.pack()

# Inicia a interface gráfica
window.mainloop()
