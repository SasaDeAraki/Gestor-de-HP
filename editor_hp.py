import tkinter as tk
from tkinter import ttk
import json
import os
from gestor_hp import atualizar_imagem

# Caminho para os JSONs
JSON_DIR = os.path.join(os.getcwd(), "json")
PERSONAGENS = ["trex", "buzz", "ze", "festor", "renna"]
CAMPOS = ["current_hp", "current_heat", "structure", "stress", "max_hp", "max_heat"]

class EditorHP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de HP dos Mechas")
        self.geometry("400x400")
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        self.frames = {}

        for nome in PERSONAGENS:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=nome.capitalize())
            self.frames[nome] = frame
            self.criar_interface(frame, nome)

    def criar_interface(self, frame, nome_personagem):
        entradas = {}
        json_path = os.path.join(JSON_DIR, f"{nome_personagem}.json")

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except:
            dados = {campo: 0 for campo in CAMPOS}

        for i, campo in enumerate(CAMPOS):
            label = ttk.Label(frame, text=campo)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            entrada = ttk.Entry(frame)
            entrada.grid(row=i, column=1, padx=10, pady=5)
            entrada.insert(0, str(dados.get(campo, 0)))
            entradas[campo] = entrada

        def salvar():
            novo_dado = {campo: int(entradas[campo].get()) for campo in CAMPOS}
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(novo_dado, f, indent=4, ensure_ascii=False)
            print(f"{nome_personagem}.json salvo com sucesso!")
            atualizar_imagem()

        botao_salvar = ttk.Button(frame, text="Salvar", command=salvar)
        botao_salvar.grid(row=len(CAMPOS), column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    app = EditorHP()
    app.mainloop()
