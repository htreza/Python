#Developed by Henrique Treza

#Leitor de audio mp3

import pygame
pygame.init()
pygame.mixer.music.load('goku.mp3')
pygame.mixer.music.play()
pygame.event.wait()
