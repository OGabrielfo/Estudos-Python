import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('C:/Users/Gabrielfo/Music/Biel/Gorillaz - clint eastwood.mp3')
pygame.mixer.music.play()
pygame.event.wait()
