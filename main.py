from GraficoDeBarrasBase import GraficoDeBarrasBase
from GraficoDeBarrasInsumos import GraficoDeBarrasRemedios, GraficoDeBarrasIAB, GraficoDeBarrasVacinasCriancas, \
    GraficoDeBarrasVacinas, GraficoDeBarrasTR, GraficoDeBarrasDG
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

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

# Preencha toda a largura e altura da GUI
window.geometry('800x600')
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# Crie um painel para organizar os botões
painel_de_botoes = ttk.LabelFrame(window, text='Opções', padding=10)
painel_de_botoes.pack(fill='both', expand=True)

# Crie um frame para preencher o espaço abaixo do painel de botões
frame_vazio = ttk.Frame(window)
frame_vazio.pack(fill='both', expand=True)

# Crie um container para os botões
container_de_botoes = ttk.Frame(painel_de_botoes)
container_de_botoes.pack(fill='both', expand=True)

# Crie botões para cada tipo de gráfico
botao_remedios = ttk.Button(container_de_botoes, text='Gráfico de Barras - Medicamentos', command=lambda: mostrar_grafico(GraficoDeBarrasRemedios))
botao_iab = ttk.Button(container_de_botoes, text='Gráfico de Barras - Itens de Atenção Básica', command=lambda: mostrar_grafico(GraficoDeBarrasIAB))
botao_vacinas_criancas = ttk.Button(container_de_botoes, text='Gráfico de Barras - Vacinas (Crianças)', command=lambda: mostrar_grafico(GraficoDeBarrasVacinasCriancas))
botao_vacinas = ttk.Button(container_de_botoes, text='Gráfico de Barras - Vacinas (Adultos e Idosos)', command=lambda: mostrar_grafico(GraficoDeBarrasVacinas))
botao_tr = ttk.Button(container_de_botoes, text='Gráfico de Barras - Testes Rápidos', command=lambda: mostrar_grafico(GraficoDeBarrasTR))
botao_dg = ttk.Button(container_de_botoes, text='Gráfico de Barras - Itens de Distribuição Gratuita', command=lambda: mostrar_grafico(GraficoDeBarrasDG))

# Empacote os botões no container de botões
botao_remedios.pack(fill='both', expand=True)
botao_iab.pack(fill='both', expand=True)
botao_vacinas_criancas.pack(fill='both', expand=True)
botao_vacinas.pack(fill='both', expand=True)
botao_tr.pack(fill='both', expand=True)
botao_dg.pack(fill='both', expand=True)

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

# Crie um botão para receber um arquivo CSV do usuário
botao_arquivo = ttk.Button(painel_de_botoes, text='Selecionar Arquivo CSV', command=receber_arquivo)
botao_arquivo.pack(fill='both', expand=True)

# Inicia a interface gráfica
window.mainloop()
