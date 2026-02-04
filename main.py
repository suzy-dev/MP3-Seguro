import customtkinter as ctk
import subprocess
import threading
from tkinter import filedialog

caminho_destino = ""

def limpar_url(url):
    if "&" in url:
        return url.split("&")[0]
    return url

def selecionar_pasta():
    global caminho_destino
    caminho = filedialog.askdirectory()
    if caminho:
        caminho_destino = caminho
        label_pasta.configure(text=f"Salvar em: {caminho}")

def acao_baixar():
    url_bruta = entry_url.get().strip()
    
    if not url_bruta:
        label_status.configure(text="Por favor, cole um link!", text_color="orange")
        return

    url_limpa = limpar_url(url_bruta)
    
    progress_bar.pack(pady=20, after=label_pasta) 
    progress_bar.set(0)
    progress_bar.start()
    
    threading.Thread(target=executar_download, args=(url_limpa,), daemon=True).start()

def executar_download(url):
    pasta_final = caminho_destino if caminho_destino else r"C:\Users\suzana.araujo\Downloads"
    caminho_executavel = r"C:\Users\suzana.araujo\Downloads\yt-dlp.exe"
    
    label_status.configure(text="⏳ Baixando... aguarde.", text_color="yellow")

    comando = [
        caminho_executavel, "-x", "--audio-format", "mp3",
        "--audio-quality", "0", "-o", f"{pasta_final}/%(title)s.%(ext)s", url
    ]
    
    resultado = subprocess.run(comando, capture_output=True, text=True)
    
    progress_bar.stop()
    
    if resultado.returncode == 0:
        progress_bar.set(1)
        label_status.configure(text="Sucesso! Música no pendrive.", text_color="green")
    else:
        progress_bar.pack_forget() # Esconde se der erro para não confundir
        label_status.configure(text="Erro no download. Verifique o link.", text_color="red")

app = ctk.CTk()
app.title("Suzana's Music Downloader")
app.geometry("550x500")

ctk.CTkLabel(app, text="Link do YouTube", font=("Arial", 22, "bold")).pack(pady=20)
entry_url = ctk.CTkEntry(app, placeholder_text="Cole o link aqui...", width=450)
entry_url.pack(pady=10)

btn_pasta = ctk.CTkButton(app, text="📁 Escolher Pasta/Pendrive", command=selecionar_pasta, fg_color="#4A4A4A")
btn_pasta.pack(pady=10)

label_pasta = ctk.CTkLabel(app, text="Padrão: Pasta Downloads", font=("Arial", 11, "italic"))
label_pasta.pack(pady=5)

progress_bar = ctk.CTkProgressBar(app, width=400)

btn_baixar = ctk.CTkButton(app, text="📥 BAIXAR EM MP3", command=acao_baixar, 
                           font=("Arial", 14, "bold"), height=45, fg_color="#1f6aa5")
btn_baixar.pack(pady=10)

label_status = ctk.CTkLabel(app, text="", font=("Arial", 12))
label_status.pack(pady=15)

app.mainloop()