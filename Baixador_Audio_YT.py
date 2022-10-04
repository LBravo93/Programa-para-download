import os
import re
from time import sleep

import moviepy.editor as mp
import PySimpleGUI as sg
from pytube import YouTube

layout = [
    [sg.Text("Copie/Cole o Link do vídeo do Youtube")],
    [sg.Text("Link "), sg.InputText(key="linkYT")],
    [sg.Button("Download"), sg.Button("Limpar")],
    [sg.Text("", key="lbl1")],
    [sg.Text("", key="lbl2")]
]

janela = sg.Window("Downloader de áudio", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == "Download":

        # Variáveis
        link = valores["linkYT"]
        local = 'D:\MUSICAS\Musicas'
        yt = YouTube(link)
        ys = yt.streams.filter(only_audio=True).first().download(local)
        janela["lbl1"].update("Download Completo!")
        for file in os.listdir(local):
            if re.search('mp4', file):
                mp4_path = os.path.join(local, file)
                mp3_path = os.path.join(
                    local, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
        janela["lbl2"].update(
            f"Seu Download está dispível em '{local}'.")
    if evento == "Limpar":
        janela["linkYT"].update("")
        janela["lbl1"].update("")
        janela["lbl2"].update("")


janela.close()
