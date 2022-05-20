import pygame
import random
pygame.init()
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
    if brojmina<0:
        print("Broj mina ne može biti manji od 1!\n")
        print("------------------------------------------------------------")
    brojmina=int(input("Upiši broj mina koji želiš imati: "))
    print("------------------------------------------------------------")

    
