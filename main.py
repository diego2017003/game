# -*- coding: utf-8 -*-
import sys, pygame, random, time
import math
import matplotlib.pyplot as plt 
import numpy as np
pygame.init()
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reaction Lab by stndn")
bg_img = pygame.image.load('WindowsTheme.png')
bg_img2 = pygame.image.load('bg.png')
font = pygame.font.Font('8-Bit Madness.ttf', 24)          
Time_list = []
current_time = []
white = (255,255,255)
black = (0,0,0)
red = (240,0,0)
green = (0,240,0)
yellow = (240,240,0)
blue = (0,0,240)
feedback_atual = ''
start_time = time.time()
running = True
eliminated = True
score = 0
time_pausa = 0
react_time_start = 0
react_time = 0
feedback = ['Mediocre', 'Bom', 'Grande Jogador', 'Lendário']
color_list = [red,green,yellow,blue]
i = random.randrange(0,3,1)
cor = color_list[i]
width = 116
height = 116
rand_x = (screen_width // 2) - width // 2        
rand_y = (screen_height // 2) - height // 2      


def drawText(str, position):

    text = font.render(str, True, white)
    text_surface = text
    text_rect = text.get_rect()
    text_rect.x = position[0]
    text_rect.y = position[1]
    
    window.blit(text_surface, text_rect)
    
  
def drawScreen():

    
    global react_time_start, eliminated
    
    window.fill(black)
    window.blit(bg_img, (0,0))
    
    total_time = round((running_time - start_time) - time_pausa, 2)
    total_time = '{0:.2f}'.format(total_time)

    drawText("Reaction Time: " +str(react_time) +" ms", [0, 0])
    drawText("Score: " +str(score), [365, 0])
    drawText("Feedback: " +str(feedback_atual), [365, 40])
    drawText("Time: " +str(total_time), [670, 0])
    drawText("w: Vermelho", [0, 200])
    drawText("a: Verde " , [0, 240])
    drawText("s: Amarelo ", [0, 280])
    drawText("d: Azul ", [0, 320])
    pygame.draw.rect(window, cor, (rand_x, rand_y, width, height))
    
    if eliminated == True:                      
        react_time_start = time.time()          
        eliminated = False                     


def pause():
    global time_pausa
    paused = True
    paused_time_start = time.time() 

    while paused:
        drawText("PAUSED!", [360, 500] )
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    time_pausa = time_pausa + (time.time() - paused_time_start)
                    paused = False

pygame.mixer.music.load('Megalovania.mp3')
pygame.mixer.music.play(-1)

while running:    
    pygame.time.delay(5)
    running_time = time.time()
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()
            elif event.key == pygame.K_w:
                if cor == color_list[0]:
                    score += 1
                    eliminated = True
                    react_time = str(round(1000*((time.time() - react_time_start))))
                    current_time.append(time.time()-start_time)       
                    Time_list.append(int(react_time))
                    if (time.time()-start_time)>40:
                        running = False

                    if int(react_time) >= 900:
                        feedback_atual = feedback[0]
                        print(feedback[0])
                    elif int(react_time) > 750 and int(react_time) < 900:
                        feedback_atual = feedback[1]
                        print(feedback[1])
                    elif int(react_time) > 500 and int(react_time) <= 750:
                        feedback_atual = feedback[2]
                        print(feedback[2])
                    elif int(react_time) <= 500:
                        feedback_atual = feedback[3]
                        print(feedback[3])
                    rand_x = random.randrange(250, 650, 65)
                    rand_y = random.randrange(200, 500, 50)
                    i= random.randrange(0,4,1)
                    cor = color_list[i]
                else:
                    if (time.time()-start_time)>40:
                        running = False
                    feedback_atual = 'Errooou'
                    eliminated = True
                    score = score-1
                    time_pausa = 0
                    react_time = 0
                    rand_x = (screen_width // 2) - width // 2       
                    rand_y = (screen_height // 2) - height // 2
                    i = random.randrange(0,4,1)
                    cor = color_list[i]   
            elif event.key == pygame.K_a:
                if cor == color_list[1]:
                    score += 1
                    eliminated = True
                    react_time = str(round(1000*((time.time() - react_time_start))))
                    Time_list.append(int(react_time))
                    current_time.append(time.time()-start_time)  
                    if (time.time()-start_time)>40:
                        running = False
                    if int(react_time) >= 900:
                        feedback_atual = feedback[0]
                        print(feedback[0])
                    elif int(react_time) > 750 and int(react_time) < 900:
                        feedback_atual = feedback[1]
                        print(feedback[1])
                    elif int(react_time) > 500 and int(react_time) <= 750:
                        feedback_atual = feedback[2]
                        print(feedback[2])
                    elif int(react_time) <= 500:
                        feedback_atual = feedback[3]
                        print(feedback[3])
                    rand_x = random.randrange(250, 650, 65)
                    rand_y = random.randrange(200, 500, 50)
                    i = random.randrange(0,4,1)
                    cor = color_list[i]
                else:
                    if (time.time()-start_time)>40:
                        running = False
                    feedback_atual = 'Errooou'
                    eliminated = True
                    score = score-1
                    time_pausa = 0
                    react_time = 0
                    rand_x = (screen_width // 2) - width // 2       
                    rand_y = (screen_height // 2) - height // 2     
                    i = random.randrange(0,4,1)
                    cor = color_list[i]
            elif event.key == pygame.K_s:
                if cor == color_list[2]:
                    score += 1
                    eliminated = True
                    react_time = str(round(1000*((time.time() - react_time_start))))
                    Time_list.append(int(react_time))
                    current_time.append(time.time()-start_time)  
                    if (time.time()-start_time)>40:
                        running = False
                    if int(react_time) >= 900:
                        feedback_atual = feedback[0]
                        print(feedback[0])
                    elif int(react_time) > 750 and int(react_time) < 900:
                        feedback_atual = feedback[1]
                        print(feedback[1])
                    elif int(react_time) > 500 and int(react_time) <= 750:
                        feedback_atual = feedback[2]
                        print(feedback[2])
                    elif int(react_time) <= 500:
                        feedback_atual = feedback[3]
                        print(feedback[3])
                    rand_x = random.randrange(250, 650, 65)
                    rand_y = random.randrange(200, 500, 50)
                    i = random.randrange(0,4,1)
                    cor = color_list[i]
                else:
                    if (time.time()-start_time)>40:
                        running = False
                    feedback_atual = 'Errooou'
                    eliminated = True
                    score = score-1
                    time_pausa = 0
                    react_time = 0
                    rand_x = (screen_width // 2) - width // 2       
                    rand_y = (screen_height // 2) - height // 2   
                    i = random.randrange(0,4,1)
                    cor = color_list[i]
            elif event.key == pygame.K_d:
                if cor == color_list[3]:
                    score += 1
                    eliminated = True
                    react_time = str(round(1000*((time.time() - react_time_start))))
                    if int(react_time) >= 900:
                        print(feedback[0])
                    Time_list.append(int(react_time))
                    current_time.append(time.time()-start_time)  
                    if (time.time()-start_time)>40:
                        running = False
                    if int(react_time) > 900 :
                        feedback_atual = feedback[0]
                        print(feedback[0])
                    elif int(react_time) > 750 and int(react_time) < 900:
                        feedback_atual = feedback[1]
                        print(feedback[1])
                    elif int(react_time) > 500 and int(react_time) <= 750:
                        feedback_atual = feedback[2]
                        print(feedback[2])
                    elif int(react_time) <= 500:
                        feedback_atual = feedback[3]
                        print(feedback[3])
                    rand_x = random.randrange(250, 650, 65)
                    rand_y = random.randrange(200, 500, 50)
                    i = random.randrange(0,4,1)
                    cor = color_list[i]
                else:
                    if (time.time()-start_time)>40:
                        running = False
                    eliminated = True
                    feedback_atual = 'Errooou'
                    score = score-1
                    time_pausa = 0
                    react_time = 0
                    rand_x = (screen_width // 2) - width // 2       
                    rand_y = (screen_height // 2) - height // 2       
                    i = random.randrange(0,4,1)
                    cor = color_list[i]
            else:
                if (time.time()-start_time)>40:
                        running = False
                eliminated = True
                feedback_atual = 'Errooou'
                score = score-1
                time_pausa = 0
                react_time = 0
                rand_x = (screen_width // 2) - width // 2       
                rand_y = (screen_height // 2) - height // 2       
                i = random.randrange(0,4,1)
                cor = color_list[i]
    drawScreen()
    pygame.display.update()

tempo_react = np.asarray(Time_list)
react_mean = round(np.mean(tempo_react),2)
runnig2 = 1
while(runnig2):
    pygame.time.delay(5)
    running_time = time.time()
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running2 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                runnig2 = False
    
    window.fill(black)
    window.blit(bg_img2, (0,0))  
    total_time = round((running_time - start_time) - time_pausa, 2)
    total_time = '{0:.2f}'.format(total_time)
    font = pygame.font.Font('8-Bit Madness.ttf', 72)  
    drawText("Game Over", [280, 200])
    font = pygame.font.Font('8-Bit Madness.ttf', 32)
    text = "Tempo medio: " 
    text.encode("utf-8")
    drawText(text +str(react_mean) +" ms", [300, 250])
    drawText("Score: " +str(score), [300, 290])
    font = pygame.font.Font('8-Bit Madness.ttf', 24)
    drawText("Press Q para sair", [300, 530])
    pygame.display.update()
runnig3 = 1
while(runnig3):
    pygame.time.delay(5)
    running_time = time.time()
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running3 = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                runnig3 = False
    
    window.fill(black)
    window.blit(bg_img2, (0,0))  
    total_time = round((running_time - start_time) - time_pausa, 2)
    total_time = '{0:.2f}'.format(total_time)
    font = pygame.font.Font('8-Bit Madness.ttf', 72)  
    drawText("Componentes...", [200, 200])
    font = pygame.font.Font('8-Bit Madness.ttf', 35)
    drawText("Diego Rodrigues Medeiros..........", [200, 250])
    drawText("Renato Lins de Arruda Farias......", [200, 290])
    drawText("Reyne Jasson Marcelino de Brito...", [200, 330])
    font = pygame.font.Font('8-Bit Madness.ttf', 24)
    drawText("Press Q para sair", [300, 530])
    pygame.display.update()


pygame.quit()
