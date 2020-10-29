import os

bestand = open("klasgenoten.txt","r")

tekst_regel = bestand.readline()
tekst_regel = tekst_regel.strip()

while tekst_regel:
    os.mkdir(tekst_regel)


    tekstregel = bestand.readline()
    tekstregel = tekst_regel.strip()
