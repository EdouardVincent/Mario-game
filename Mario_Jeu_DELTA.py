#Jeu du Mario
#Créé par Edouard Vincent 
#GitHub :EdouardVincent
#Email : edouardvinc@protonmail.ch
#Code sur GitHub : EdouardVincent/A-little-Mario-game-first-test
#Ln = 460

import pygame
from pygame.locals import*
import time
import sys
from tkinter import*

FPS = 150
FPSCLOCK = pygame.time.Clock()
FPSCLOCK.tick(FPS)

#création de variables :
saut_mario_brique1 = 0
mario_brique1 = 0
mario_brique2 = 0
cote = "droite"
direction = ""
tombee = ''
mort = 0
condition1=0
condition2=0
condition3=0
condition4=0
menu = 1
partie=0

pygame.init()
font=pygame.font.Font(None, 50)
font2=pygame.font.Font(None, 40)
font3=pygame.font.Font(None, 200)
texte = font.render("Objectif : NE PAS SE FAIRE TOUCHER PAR LES LASERS !",1,(255,255,0))
GameOver = font.render("GAME OVER !",1,(0,255,0))
Play = font3.render("   JEU             MARIO",1,(255,255,255))
Du = font3.render("      DU",1,(255,255,255))
pygame.display.set_icon(pygame.image.load("C:\Jeu personnages\icone.ico"))
bouton_jouer = pygame.image.load("C:\Jeu personnages\OIP (12).png")
bouton_quitter = pygame.image.load("C:\Jeu personnages\OIP (14).png")
Mario__normal__droite__image = pygame.image.load("C:\Jeu personnages\Mario-normal-droite-_2_.gif")
Mario__normal__gauche__image = pygame.image.load("C:\Jeu personnages\Mario-normal-gauche-_2_.gif")
Mario__saut__droit__image = pygame.image.load("C:\Jeu personnages\Mario-saut-droit.gif")
Mario__saut__gauche__image = pygame.image.load("C:\Jeu personnages\Mario-saut-gauche.gif")
laser__image = pygame.image.load("C:\Jeu personnages\laser.png")
brique = pygame.image.load("C:\Jeu personnages\Brick_block.png")
Mario__mort__droite__image = pygame.image.load("C:\Jeu personnages\Mario_mort_droite.gif")
Mario__mort__gauche__image = pygame.image.load("C:\Jeu personnages\mario_mort_gauche.gif")
bg = pygame.image.load = pygame.image.load("C:\Jeu personnages\OIP (1).jpg")
img=Mario__normal__droite__image

#classes and functions#################################################

class joueur () : 

    def __init__ (self) :
        self.pos_x = 0
        self.pos_y = 760
        self.image = img
        self.increment_horizontal = 20
        self.increment_vertical = 10

    def affichage (self) :
        fenetre.blit(self.image, (self.pos_x, self.pos_y))

    def calcul_deplacement_droite (self) :
        self.pos_x+=self.increment_horizontal
        
    def calcul_deplacement_gauche (self) :
        self.pos_x-=self.increment_horizontal
        
    def calcul_deplacement_haut (self) :
        self.pos_y-=self.increment_vertical
        
    def calcul_deplacement_bas (self) :
        self.pos_y+=self.increment_vertical
        
class Plateforme () :
    def __init__ (self) :
        self.pos_x = 0
        self.pos_y = 0
        self.image = brique
        self.rect = self.image.get_rect(topleft = (self.pos_x, self.pos_y-38))
        
    def affichage (self) :
        fenetre.blit(self.image, (self.pos_x, self.pos_y))
    
class Laser () :
    def __init__ (self) :
        self.pos_x = 0
        self.pos_y = 0
        self.image = laser__image 
        self.increment = 5
        
    def affichage (self) :
        fenetre.blit(self.image, (self.pos_x, self.pos_y))
        
    def calcul_deplacement_gauche (self) :
        self.pos_x -= self.increment
        
def terminate() :
    pygame.quit()
    sys.exit()

################################################################################

Laser1 = Laser() #instanciation 
Laser2 = Laser() #instanciation 
Laser3 = Laser() #instanciation 
Laser4 = Laser() #instanciation 
Mario = joueur()
Brique1 = Plateforme()
Brique2 = Plateforme()

start_ticks=pygame.time.get_ticks()
seconds=(pygame.time.get_ticks()-start_ticks)

pygame.key.set_repeat(1,20)

if menu == 1 :
    
    while menu: # boucle principale
        
        Laser1.pos_x = 1600 #bas
        Laser1.pos_y = 810
        Laser1.image = laser__image

        Laser2.pos_x = 800
        Laser2.pos_y = 810
        Laser2.image = laser__image

        Laser3.pos_x = 1200 #haut
        Laser3.pos_y = 650
        Laser3.image = laser__image

        Laser4.pos_x = 400
        Laser4.pos_y = 650
        Laser4.image = laser__image

        Mario.pos_x = 0
        Mario.pos_y = 760

        Brique1.pos_x = 490
        Brique1.pos_y = 799
        Brique1.image = brique
        
        Brique2.pos_x = 590
        Brique2.pos_y = 700
        Brique2.image = brique

        pygame.display.set_caption('Menu')
    
        for event in pygame.event.get():
            if event.type == QUIT :
                terminate()
                
            if event.type == KEYDOWN :
                
                if event.key == K_ESCAPE :
                    terminate()
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
            
                jouer = bouton_jouer.get_rect(topleft = (715, 100))
                quitter = bouton_quitter.get_rect(topleft = (715, 300))
            
                if jouer.collidepoint(event.pos) :
                    menu = 0
                    partie = 1
                
                if quitter.collidepoint(event.pos) :
                    terminate()
                    
        fenetre = pygame.display.set_mode((1700,1000))
        fenetre.blit(bouton_jouer,(715, 100))
        fenetre.blit(bouton_quitter,(715, 300))
        fenetre.blit(Play,(170,760))
        fenetre.blit(Du,(520,760))
        pygame.display.flip()
        
        if partie == 1 :
            
            Mario.image = Mario__normal__droite__image
            pygame.display.set_caption('Mario Niveau 1')
            fenetre.blit(bg, (-100, -100))
            fenetre.blit (texte, (0,0))
            Mario.affichage ()
            pygame.display.flip()
            time.sleep(2)
            pygame.key.set_repeat(1,20)
            partie = 1

            while True :
                
                seconds=(pygame.time.get_ticks()-start_ticks)/1000
        
                for event in pygame.event.get():
            
                    if event.type == QUIT:
                        terminate()
                
                    elif event.type == KEYDOWN:
                
                        if (event.key == K_LEFT or event.key == K_q) :
                            direction = "gauche"
                            cote = "gauche"
                
                        elif (event.key == K_RIGHT or event.key == K_d) :
                            direction = "droite"
                            cote="droite"
                
                        elif (event.key == K_UP or event.key == K_z) :
                            direction = "haut"

                        if event.type == QUIT:
                            terminate()
                
                        if event.key == K_ESCAPE:
                            terminate()
                
                Laser1.calcul_deplacement_gauche ()
                Laser2.calcul_deplacement_gauche ()
                Laser3.calcul_deplacement_gauche ()
                Laser4.calcul_deplacement_gauche ()
                
                Mario.rect = img.get_rect(topleft = (Mario.pos_x, Mario.pos_y))
                Brique1.rect = brique.get_rect(topleft = (Brique1.pos_x, Brique1.pos_y-18))
                Brique2.rect = brique.get_rect(topleft = (Brique2.pos_x, Brique2.pos_y-18))
  
                if direction == "gauche" :
                    if mort == 1 :
                        direction = ""
                        
                    if Mario.pos_x == 0 :
                        Mario.calcul_deplacement_droite()
                    Mario.calcul_deplacement_gauche()
                    Mario.image = Mario__normal__gauche__image
                    direction = ""
            
                    if Mario.pos_y < 760 and mario_brique1 == 0 and mario_brique2 == 0 :
                        direction="haut"
                        Mario.calcul_deplacement_droite()
                        
                        if tombee != '' :
                            direction = ""
                        
                    if Mario.pos_y < 660 and mario_brique1 == 1  and mario_brique2 == 0 :
                        direction="haut"
                        Mario.calcul_deplacement_droite ()
                        
                    if Mario.pos_y < 560 and mario_brique2 == 1 and mario_brique1 == 0 :
                        direction="haut"
                        Mario.calcul_deplacement_droite ()
                        
                        if tombee != '' :
                            direction = ""
                
                if direction == "droite" :
                    if mort == 1 :
                        direction = ""
                    
                    if Mario.pos_x == 1690 :
                        Mario.calcul_deplacement_gauche ()
                    Mario.calcul_deplacement_droite()
                    Mario.image = Mario__normal__droite__image
                    direction = ""
            
                    if Mario.pos_y < 760 and mario_brique1 == 0 and mario_brique2 == 0 :
                        direction="haut"
                        Mario.calcul_deplacement_gauche()
                        
                        if tombee != '' :
                            direction = ""
                        
                    if Mario.pos_y < 660 and mario_brique1 == 1 and mario_brique2 == 0 :
                        direction="haut"
                        Mario.calcul_deplacement_gauche()
                        
                    if Mario.pos_y < 560 and mario_brique2 == 1 and mario_brique1 == 0 :
                        direction="haut"
                        Mario.calcul_deplacement_gauche()
                        
                        if tombee != '' :
                            direction = ""
                        
                if direction == "haut":
                    if mort == 1 :
                        direction = ""
                        
                    condition1=condition1+1
    
                    if condition1 < 20.2 :#calcul de la montée du Mario
                        Mario.calcul_deplacement_haut()
                        if cote == "droite" :
                            Mario.image = Mario__saut__droit__image
   
                        if cote == "gauche" :
                            Mario.image = Mario__saut__gauche__image
                      
                    if condition1 > 20 :#calcul de la descente du Mario
                        Mario.calcul_deplacement_bas()
                
                        if Mario.rect.colliderect(Brique1.rect):
                            saut_mario_brique1 = 1
                            condition1=40
                            mario_brique1=1
                            mario_brique2 = 0
                                
                        if Mario.rect.colliderect(Brique2.rect): 
                            condition1=40
                            mario_brique2=1
                            mario_brique1= 0
                
                        if cote == "droite" :
                            Mario.image = Mario__saut__droit__image
                        
                            if condition1 >= 40 :
                                direction = ""
                                condition1=0
                                Mario.image = Mario__normal__droite__image
                          
                        if cote == "gauche" :
                            Mario.image = Mario__saut__gauche__image
                 
                            if condition1 >= 40 :
                                direction = ""
                                condition1=0
                                Mario.image = Mario__normal__gauche__image
                                

                if Mario.rect.collidepoint(Laser1.pos_x, Laser1.pos_y):
                    mort = 1

                if Mario.rect.collidepoint(Laser2.pos_x, Laser2.pos_y):
                    mort = 1

                if Mario.rect.collidepoint(Laser3.pos_x, Laser3.pos_y):
                    mort = 1
           
                if Mario.rect.collidepoint(Laser4.pos_x, Laser4.pos_y):
                    mort = 1

                if mario_brique1 == 1 and mario_brique2 == 0 and Mario.pos_x > Brique1.pos_x+140 :
                    tombee = 'droite_brique1'
                    mario_brique1=0
                    
                if mario_brique1 == 1 and mario_brique2 == 0 and Mario.pos_x < Brique1.pos_x-95 :
                    tombee = 'gauche_brique1'
                    mario_brique1 = 0
                    
                if mario_brique2 == 1 and mario_brique1 == 0 and Mario.pos_x > Brique2.pos_x+140 :
                    tombee = 'droite_brique2'
                    mario_brique2=0
                    
                if mario_brique2 == 1 and mario_brique1 == 0 and Mario.pos_x < Brique2.pos_x-95 :
                    tombee = 'gauche_brique2'
                    mario_brique2 = 0
                
                if tombee == 'droite_brique1' :
                    condition2=condition2+1
                    Mario.image = Mario__mort__droite__image
                    Mario.calcul_deplacement_bas()
            
                    if condition2==10 :
                        Mario.image = Mario__normal__droite__image
                        tombee = ''
                        condition2=0
        
                if tombee == 'gauche_brique1' :
                    condition2=condition2+1
                    Mario.image = Mario__mort__gauche__image
                    Mario.calcul_deplacement_bas()
            
                    if condition2== 10 :
                        Mario.image = Mario__normal__gauche__image
                        tombee = ''
                        condition2=0
                        
                if tombee == 'droite_brique2' :
                    condition4=condition4+1
                    Mario.image = Mario__mort__droite__image
                    Mario.calcul_deplacement_bas()
            
                    if condition4==20 :
                        Mario.image = Mario__normal__droite__image
                        tombee = ''
                        condition4=0
                        
                if tombee == 'gauche_brique2' :
                    print("bonjour")
                    condition4=condition4+1
                    Mario.image = Mario__mort__gauche__image
                    Mario.calcul_deplacement_bas()
            
                    if condition4== 10 :
                        Mario.image = Mario__normal__gauche__image
                        tombee = ''
                        condition4=0
                        mario_brique1 = 1
            
                if Laser1.pos_x <= 0 : #Si le laser touche le coté gauche alors revenir de l'autre coté
                    Laser1.pos_x = 1700

                if Laser2.pos_x <= 0 : #Si le laser touche le coté gauche alors revenir de l'autre coté
                    Laser2.pos_x = 1700

                if Laser3.pos_x <= 0 : #Si le laser touche le coté gauche alors revenir de l'autre coté
                    Laser3.pos_x = 1700
            
                if Laser4.pos_x <= 0 : #Si le laser touche le coté gauche alors revenir de l'autre coté
                    Laser4.pos_x = 1700

        
                if mort == 1 :
                
                    menu=1
                    condition3=condition3+1
                    Mario.calcul_deplacement_bas()
        
                    if Mario.image == Mario__normal__droite__image :
                        Mario.image = Mario__mort__droite__image
            
                    if Mario.image == Mario__normal__gauche__image :
                        Mario.image = Mario__mort__gauche__image
           
                    direction = ""
                    fenetre.blit (GameOver, (650,100))
                    secondes = str(seconds)
                    fenetre.blit(bg, (0,0))
                    texte2 = font.render(secondes,1,(255,255,255))
                    texte3 = font.render("Tu as tenu              secondes",1,(255,255,255))
                    fenetre.blit (texte3, (505,200))
                    fenetre.blit (texte2, (765,200))
                    #son.stop()
            
                    if condition3 >= 50 :
                        direction = ""
                        mario_brique1 = 0
                        mario_brique2 = 0
                        condition1 = 0
                        condition2 = 0
                        condition3 = 0
                        condition4=0
                        mort = 0
                        time.sleep(3)
                        partie = 0
                        tombee = ''
                        break
                        menu = 1
                        
                fenetre.blit(bg, (-100,-100))#à la fin, on affiche tout dans le but d'avoit plusieurs instances à afficher en meme temps
                Brique2.affichage ()
                Brique1.affichage ()
                Mario.affichage ()
                Laser1.affichage ()
                Laser2.affichage ()
                Laser3.affichage ()
                Laser4.affichage ()
                pygame.display.flip()

