import pronouncing
import pyttsx3
import tkinter as tk
from tkinter import ttk, messagebox

# Inicializa o motor de síntese de voz
engine = pyttsx3.init()

# Função para obter a pronúncia de uma palavra
def obter_pronuncia(palavra):
    pronuncia = pronouncing.phones_for_word(palavra)
    if pronuncia:
        return pronuncia[0]  # Retorna a primeira pronúncia encontrada
    else:
        return "Pronúncia não encontrada."

# Função para atualizar a pronúncia ao digitar
def atualizar_pronuncia(event=None):
    palavra = entrada_palavra.get().strip().lower()  # Obtém a palavra digitada
    if palavra:
        pronuncia = obter_pronuncia(palavra)
        label_pronuncia.config(text=f"Como se fala: {pronuncia}")
    else:
        label_pronuncia.config(text="Como se fala:")

# Função para reproduzir a pronúncia em áudio
def reproduzir_pronuncia():
    palavra = entrada_palavra.get().strip().lower()
    if palavra:
        try:
            engine.say(palavra)
            engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao reproduzir a pronúncia: {e}")
    else:
        messagebox.showwarning("Aviso", "Por favor, digite uma palavra.")

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Como se Fala em Inglês")
janela.geometry("500x200")

# Rótulo e entrada para a palavra
rotulo_palavra = ttk.Label(janela, text="Digite uma palavra em inglês:")
rotulo_palavra.pack(pady=10)

entrada_palavra = ttk.Entry(janela, width=30)
entrada_palavra.pack(pady=5)
entrada_palavra.bind("<KeyRelease>", atualizar_pronuncia)  # Atualiza a pronúncia ao digitar

# Rótulo para exibir a pronúncia
label_pronuncia = ttk.Label(janela, text="Como se fala:", font=("Arial", 12))
label_pronuncia.pack(pady=10)

# Botão para reproduzir a pronúncia em áudio
botao_reproduzir = ttk.Button(janela, text="Ouvir Pronúncia", command=reproduzir_pronuncia)
botao_reproduzir.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
    