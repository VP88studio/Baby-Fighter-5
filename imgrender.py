import pygame, gif_pygame
def renderimg():
    global bg, lefthit, righthit, static, bb1
    bg = pygame.image.load('assets/bg.png')
    lefthit = gif_pygame.load('assets/lefthit.gif')
    righthit = gif_pygame.load('assets/righthit.gif')
    static = gif_pygame.load('assets/static.gif')
    bb1 = gif_pygame.load('assets/bb1.gif')