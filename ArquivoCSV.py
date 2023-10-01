import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class ArquivoCSV(tk.Frame):
    def __init__(self, comboBoxAno, master=None):
        super().__init__(master)
        self.comboBoxAno = comboBoxAno  # A referência ao ComboBox onde os anos serão exibidos
        self.atualizar_arquivo_csv()

    def atualizar_arquivo_csv(self):
        # Verifica se o arquivo "dados.csv" existe, se não, solicita ao usuário selecionar um arquivo CSV
        if os.path.exists("dados.csv"):
            arquivo_selecionado = "dados.csv"
        else:
            arquivo_selecionado = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
            if not arquivo_selecionado:
                return

            # Copia o arquivo selecionado para "dados.csv" e exibe uma mensagem de sucesso
            shutil.copy(arquivo_selecionado, "dados.csv")
            messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso!")

        # Chama a função para atualizar o ComboBox com os anos disponíveis
        self.atualizar_combobox_ano()

    def atualizar_combobox_ano(self):
        anos_set = set()
        try:
            # Lê o arquivo "dados.csv" e extrai os anos das linhas
            with open("dados.csv", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines[1:]:
                    columns = line.strip().split(",")
                    if len(columns) > 0 and columns[0].isdigit():
                        anos_set.add(columns[0])
        except Exception as e:
            print(e)

        # Converte o conjunto de anos em uma lista ordenada e atualiza os valores do ComboBox
        anos_list = sorted(list(anos_set), reverse=True)
        self.comboBoxAno["values"] = anos_list
        if anos_list:
            self.comboBoxAno.set(anos_list[0])  # Define o primeiro ano da lista como valor padrão no ComboBox
