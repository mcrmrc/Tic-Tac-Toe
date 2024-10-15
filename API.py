import random

#Ritorna l'indice relativo alla cella scelta
def cellaSceltaCorretta(scelta, griglia):
    if(scelta=="q"):
        if(griglia[0]!="q"):
            return False
        return 1
    elif(scelta=="w"):
        if(griglia[1]!="w"):
            return False
        return 2
    elif(scelta=="e"):
        if(griglia[2]!="e"):
            return False
        return 3
    elif(scelta=="a"):
        if(griglia[3]!="a"):
            return False
        return 4
    elif(scelta=="s"):
        if(griglia[4]!="s"):
            return False
        return 5
    elif(scelta=="d"):
        if(griglia[5]!="d"):
            return False
        return 6
    elif(scelta=="z"):
        if(griglia[6]!="z"):
            return False
        return 7
    elif(scelta=="x"):
        if(griglia[7]!="x"):
            return False
        return 8
    elif(scelta=="c"):
        if(griglia[8]!="c"):
            return False
        return 9
    else:
        return False

#Controlla se il giocatore ha vinto
def controllaVittoria(turno, giocatori, griglia):
    simbolo=getSimboloGiocatore(turno)
    for i in range(3):
        #Controllo tutte le righe
        if(griglia[0+3*i]==simbolo and griglia[1+3*i]==simbolo and griglia[2+3*i]==simbolo):
            print("{g} ha vinto".format(g=giocatori[turno]))
            return False
        #Controllo le colonne
        if(griglia[0+1*i]==simbolo and griglia[3+1*i]==simbolo and griglia[6+1*i]==simbolo):
            print("{g} ha vinto".format(g=giocatori[turno]))
            return False
        #Controllo le diagonali
        if(griglia[0]==simbolo and griglia[4]==simbolo and griglia[8]==simbolo):
            print("{g} ha vinto".format(g=giocatori[turno]))
            return False
        if(griglia[2]==simbolo and griglia[4]==simbolo and griglia[6]==simbolo):
            print("{g} ha vinto".format(g=giocatori[turno]))
            return False
    return  True

#Ritorna il simbolo associato al giocatore
def getSimboloGiocatore(turno):
    if(turno==0):
        return "X"
    elif(turno==1):
        return "O"
    else:
        raise Exception("Turno non vlaido")

#Metodo per stampare la griglia di gioco
def stampaGriglia(griglia):
    stringa=""
    count=0
    for simbolo in griglia:
        stringa+=" | "
        if(simbolo is not None):
            stringa+=simbolo
        count+=1
        if(count%3==0):
            stringa+=" |\n"
    print(stringa)

#Metodo per decidere il primo giocatore a iniziare
def chiGiocaInizio():
    rand= random.Random(5)
    #random.seed(2)
    return rand.getrandbits(1)

#Fa procedere il turno del giocatore
def turnoGiocatore(turno, giocatori, griglia):
    print("{g}. Dove posizioni il simbolo?".format(g=giocatori[turno]))

    posizione=input("Premi la lettera della cella voluta  ")
    while(not cellaSceltaCorretta(posizione, griglia)):
        posizione=input("Scelta non valida. Rimetti la lettera della cella voluta  ")
    
    #cambiaCellaGriglia(turno, cellaSceltaCorretta(posizione, griglia))
    griglia[cellaSceltaCorretta(posizione, griglia)-1]=getSimboloGiocatore(turno) #Cambia la cella della griglia
    