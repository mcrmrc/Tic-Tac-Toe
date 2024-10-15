#Il gioco è quello del filetto:
    #Si ha una griglia 3x3
    #Si hanno due giocatori, che decideranno come chiamarsi
    #Ognuno di loro avrà un suo simbolo
    #Ogni volta il giocatore di turno posizionerà il suo simbolo
        #Se riesce a fare tre simboli di fila vince
        #Altrimenti il turno passa all'altro giocatore
    #Se nessun dei due riesce a fare un tris, la partita è patta

    # o | x | o
    # x | x | o
    # o | o | x

from API import *

griglia =["q", "w", "e", "a", "s", "d", "z", "x", "c"]

giocatori=["giocatore1", "giocatore2"]

turno=0 #1-> giocatore 1     2-> giocatore2     0->Errore


if __name__ == "__main__":
    print("FILETTO")
    giocatori[0]=input("Nome del primo giocatore: ")
    print("{g1} il tuo simbolo sarà la X \n".format(g1=giocatori[0]))

    giocatori[1]=input("Nome del secondo giocatore: ")
    print("{g2} il tuo simbolo sarà la O \n".format(g2=giocatori[1]))

    turno=chiGiocaInizio()
    print("Inizierà {t} \n".format(t=giocatori[turno]))

    stampaGriglia(griglia)
    ancora=True
    while(ancora):
        turnoGiocatore(turno, giocatori, griglia)
        stampaGriglia(griglia)
        ancora=controllaVittoria(turno, giocatori, griglia)
        turno=(turno+1)%2
        
