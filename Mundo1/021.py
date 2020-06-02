'''
Faça um programa em python que abra e 
reproduza o áudio de um arquivo mp3.
'''
import pygame

pygame.mixer.init()
pygame.init()


filename = '/home/mhf/Caladan_Brood/2013_-_Echoes_Of_Battle/02_-_Echoes_Of_Battle.mp3'
pygame.mixer.music.load(filename)

pygame.mixer.music.play()
pygame.event.wait()
