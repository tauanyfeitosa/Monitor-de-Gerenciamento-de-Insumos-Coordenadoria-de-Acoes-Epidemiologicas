import os
import shutil
from tkinter import filedialog, messagebox
import tkinter as tk


class ArquivoCSV(tk.Frame):
    def __init__(self, comboBoxAno, master=None):
        super().__init__(master)
        self.comboBoxAno = comboBoxAno
        self.atualizar_arquivo_csv()  # Chama a função para atualizar o arquivo CSV

    def atualizar_arquivo_csv(self):
        # Verifica se já existe um arquivo "dados.csv" no diretório atual
        if os.path.exists("dados.csv"):
            arquivo_selecionado = "dados.csv"
        else:
            # Se não existir, permite ao usuário selecionar um arquivo
            arquivo_selecionado = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
            if not arquivo_selecionado:
                # Se o usuário não selecionar um arquivo, saia do método
                return

            # Copia o arquivo selecionado para "dados.csv"
            shutil.copy(arquivo_selecionado, "dados.csv")
            messagebox.showinfo("Sucesso", "Arquivo copiado com sucesso!")

        # Atualiza as opções da caixa de combinação de anos
        self.atualizar_combobox_ano()

    def atualizar_combobox_ano(self):
        anos_set = set()
        try:
            with open("dados.csv", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines[1:]:
                    columns = line.strip().split(",")
                    if len(columns) > 0 and columns[0].isdigit():
                        anos_set.add(columns[0])
        except Exception as e:
            print(e)  # Exiba a mensagem de erro para diagnóstico

        anos_list = sorted(list(anos_set), reverse=True)
        self.comboBoxAno["values"] = anos_list
        if anos_list:
            self.comboBoxAno.set(anos_list[0])

