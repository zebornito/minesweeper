import pygame
import random
pygame.init()
pozboja=(192,192,192)
rubboja=(128,128,128)
sirina=int(input("Upiši koliko ćeš kućica imati u širinu: "))
print("------------------------------------------------------------")
while sirina<1:
    print("Širina ne može biti manja od 1!")
    print("------------------------------------------------------------")
    sirina=int(input("Upiši koliko ćeš kućica imati u širinu: "))
    print("------------------------------------------------------------")
visina=int(input("Upiši koliko ćeš kućica imati u visinu: "))
print("------------------------------------------------------------")
while visina<1:
    print("Visina ne može biti manja od 1!")
    print("------------------------------------------------------------")
    visina=int(input("Upiši koliko ćeš kućica imati u visinu: "))
    print("------------------------------------------------------------")
brojmina=int(input("Upiši broj mina koji želiš imati: "))
while brojmina<1 or brojmina>sirina*visina:
    if brojmina>sirina*visina:
        print("Broj mina ne može biti veći od broja kućica!")
        print("------------------------------------------------------------")
    elif brojmina<0:
        print("Broj mina ne može biti manji od 1!\n")
        print("------------------------------------------------------------")
    brojmina=int(input("Upiši broj mina koji želiš imati: "))
    print("------------------------------------------------------------")
kucica=32
rub=16
gorerub=100
ekransirina=kucica*sirina+rub*2
ekranvisina=kucica*visina+gorerub
display=pygame.display.set_mode((ekransirina, ekranvisina))
pygame.display.set_caption("Minesweeper")
spr_praznakucica=pygame.image.load("sprajt/nis.png")
spr_zastava=pygame.image.load("sprajt/zastava.png")
spr_kucica=pygame.image.load("sprajt/kucica.png")
spr_kuc1=pygame.image.load("sprajt/1.png")
spr_kuc2=pygame.image.load("sprajt/2.png")
spr_kuc3=pygame.image.load("sprajt/3.png")
spr_kuc4=pygame.image.load("sprajt/4.png")
spr_kuc5=pygame.image.load("sprajt/5.png")
spr_kuc6=pygame.image.load("sprajt/6.png")
spr_kuc7=pygame.image.load("sprajt/7.png")
spr_kuc8=pygame.image.load("sprajt/8.png")
spr_mina=pygame.image.load("sprajt/mina.png")
spr_minakrivo=pygame.image.load("sprajt/minakrivo.png")
spr_minastisnuo=pygame.image.load("sprajt/minastisnuo.png")
mreza=[]
mine=[]
def pisiText(txt, s, yOff=0):
    text=pygame.font.SysFont("Calibri",s,True).render(txt,True,(0,0,0))
    rect=text.get_rect()
    rect.center=(sirina*kucica/2+border,visina*kucica/2+gorerub+yOff)
    display.blit(text,rect)
class mreza:
    def __init__(self, xmreza, ymreza, type):
        self.xmreza=xmreza
        self.ymreza=ymreza
        self.stisnuo=False
        self.minastisnuo=False
        self.minakrivo=False
        self.zastava=False
        self.rect=pygame.Rect(rub+self.xMreza*kucica,gorerub+self.ymreza*kucica,kucica,kucica)
        self.izn=type
    def drawGrid(self):
        if self.minakrivo:
            display.blit(spr_minakrivo,self.rect)
        else:
            if self.stisnuo:
                if self.izn==-1:
                    if self.minastisnuo:
                        display.blit(spr_minastisnuo,self.rect)
                    else:
                        display.blit(spr_mina,self.rect)
                else:
                    if self.izn==0:
                        display.blit(spr_praznakucica,self.rect)
                    elif self.izn==1:
                        display.blit(spr_kuc1,self.rect)
                    elif self.izn==2:
                        display.blit(spr_kuc2,self.rect)
                    elif self.izn==3:
                        display.blit(spr_kuc3,self.rect)
                    elif self.izn==4:
                        display.blit(spr_kuc4,self.rect)
                    elif self.izn==5:
                        display.blit(spr_kuc5,self.rect)
                    elif self.izn==6:
                        display.blit(spr_kuc6,self.rect)
                    elif self.izn==7:
                        display.blit(spr_kuc7,self.rect)
                    elif self.izn==8:
                        display.blit(spr_kuc8,self.rect)

            else:
                if self.zastava:
                    display.blit(spr_zastava, self.rect)
                else:
                    display.blit(spr_kucica, self.rect)






