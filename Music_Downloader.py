
# Bibliotecas necessárias para o funcionamento do programa
import os
import re

import moviepy.editor as mp
import PySimpleGUI as sg
from pytube import YouTube

# Definindo o tema e como será o layout da tela
sg.theme('TanBlue')
layout = [
    [sg.Text("Copie/Cole o Link do vídeo do Youtube")],
    [sg.Text("Link "), sg.InputText(key="linkYT")],
    [sg.Button("Download",), sg.Button("Limpar"), ],
    [sg.Text("", key="lbl1")],
    [sg.Text("", key="lbl2")]
]

# Abrindo a Janela e fazendo configurações padrão
janela = sg.Window("Downloader de áudio", layout, size=(
    500, 200), keep_on_top=True, element_justification='c')

while True:  # Começando a rotina do sistema
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:  # Para fechar o sistema quando click no x
        break
    if evento == "Download":  # Inicia a download do audio do vídeo

        # Variáveis
        link = valores["linkYT"]
        local = 'D:\MUSICAS\Musicas'
        yt = YouTube(link)
        ys = yt.streams.filter(only_audio=True).first().download(local)
        janela["lbl1"].update("Download Completo!")

        # Rotinar 'for' para converter de MP4 para MP3
        for file in os.listdir(local):
            if re.search('mp4', file):
                mp4_path = os.path.join(local, file)
                mp3_path = os.path.join(
                    local, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
                janela["lbl2"].update(
                    f"Seu Download está disponível em '{local}'.")

    if evento == "Limpar":  # Rotina para limapr os campos preenchidos anteriormente
        janela["linkYT"].update("")
        janela["lbl1"].update("")
        janela["lbl2"].update("")


janela.close()  # Fim do programa
