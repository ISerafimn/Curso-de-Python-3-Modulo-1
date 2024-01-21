# Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3

import pygame

'''from audioplayer import AudioPlayer

AudioPlayer("ex021-music.mp3").play(block=True)'''

# Metodo Guanabara

pygame.init()

pygame.mixer.music.load('ex021-music.mp3')
pygame.mixer.music.play()
