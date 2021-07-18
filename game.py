import pygame
from pygame.locals import *
from random import seed
from random import random
import pygame_menu
import math

from pygame_menu.events import EXIT, MenuAction
def Comecar(s):
    global state 
    state = s
    return
def trocar_nome(n):
    global nome 
    nome = n
    return
class Jogo:
    state = 0
    nome = ''
    tempos = []

    def change_state():
        if(state==0):
            Jogo.state = 1
            print(Jogo.state)
        elif(state==1):
            Jogo.state = 2
            print(Jogo.state)  
        return
    def change_screen(cor,pos,r):
        Jogo.state==0:
        if Jogo.state == 0:
            SCREEN_WIDTH = 600
            SCREEN_HEIGHT = 600
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            menu = pygame_menu.Menu('Jogo de atenção', 600, 600,
                    theme=pygame_menu.themes.THEME_BLUE)
            menu.add.text_input('Nome :', default='Jogador1')
            menu.add.button('Iniciar',action=Jogo.change_state())
            menu.add.button('Sair', pygame_menu.events.EXIT)
            menu.mainloop(screen)
        if Jogo.state == 1:
            SCREEN_WIDTH = 600
            SCREEN_HEIGHT = 600
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.fill((255, 255, 255))
            pygame.draw.circle(screen, cor, pos, r)
            pygame.display.update()
        return  



pygame.init()
seed(0)
state = 0
circle_colors = [(255,0,0),(0,255,0),(0,0,255)]
cicle_radius = (int(100*random())) + 50
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

#surf = pygame.Surface((50, 50))
#surf.fill((0,0,0))
jogo1 = Jogo
lista_cor = [(255,0,0),(0,255,0),(0,0,255),(200,200,0)]
indice = round(3*random())
cor =  lista_cor[indice]
radius = 50+round(50*random())
x = 250+round(500*random())
y = 250+round(500*random())
pos = (x,y)
while running:
    jogo1.change_screen(cor,pos,radius)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == K_w:
               seed(9)
               print('w')
               indice = round(300*random()/100)
               cor =  lista_cor[indice]
               radius = 50+round(50*random())
               x = 250+round(50000*random()/100)
               y = 250+round(50000*random()/100)
               jogo1.change_screen(cor,pos,radius)
            elif event.key == K_a:
               seed(3)
               print('a')
               indice = round(300*random()/100)
               cor =  lista_cor[indice]
               radius = 50+round(50*random())
               x = 250+round(50000*random()/100)
               y = 250+round(50000*random()/100)
               jogo1.change_screen(cor,pos,radius)
            elif event.key == K_s:
               seed(0)
               print('s')
               indice = round(300*random()/100)
               cor =  lista_cor[indice]
               radius = 50+round(50*random())
               x = 250+round(50000*random()/100)
               y = 250+round(50000*random()/100)
               jogo1.change_screen(cor,pos,radius)
            elif event.key == K_d:
               seed(30)
               print('d')
               indice = round(300*random()/100)
               cor =  lista_cor[indice]
               radius = 50+round(50*random())
               x = 250+round(50000*random()/100)
               y = 250+round(50000*random()/100)
               jogo1.change_screen(cor,pos,radius)
        elif event.type == pygame.QUIT:
            running = False


