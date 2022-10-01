
import os
import re
from time import sleep

import moviepy.editor as mp
from pytube import YouTube

from modulo_cores import amarelo, azul, verde, vermelho

# Imput para digitar o link do vídeo e o local onde deseja salvar o mp3
print(amarelo('*' * 47))
print(amarelo('Programa para download de músicas do Youtube'))
print(amarelo('*' * 47))
print()

validador = True
while validador == True:
    print(azul('1 - Baixar Música'))
    print(azul('2 - Finalizar Programa'))
    resp = int(input(azul('Digite sua opção: ')))

    if resp == 1 or resp == 2:
        validador = False
    else:
        print(vermelho(
            'Resposta inválida!!!\nDigite apenas números inteiros válidos [1 ou 2].'))
        print()

    sleep(0.5)

    if resp == 1:
        link = input(azul('Cole/Digite o link do vídeo do youtube: ')).strip()
        local = 'D:\MUSICAS\Musicas'
        yt = YouTube(link)

        # Download

        print(azul('Baixando...'))
        ys = yt.streams.filter(only_audio=True).first().download(local)
        print(verde('Download completo!!!'))
        # convertendo MP4 para MP3
        print(azul('Convertendo arquivo para MP3. Por favor Aguarde...'))
        print()
        for file in os.listdir(local):
            if re.search('mp4', file):
                mp4_path = os.path.join(local, file)
                mp3_path = os.path.join(
                    local, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
        print()

        print(verde('Pronto...'))
        print(verde(f'Seu MP3 está disponível em {amarelo(local)}'))
        print()
    elif resp == 2:
        print(vermelho('Programa finalizado!!!'))
        validador = False
