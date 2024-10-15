extends Node2D

var giocatore=-1
var simbolo=["x","o"]
var griglia=[
	"","", "",
	"","", "",
	"","", ""
]

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	self.giocatore=get_parent().giocatoreInit
	print("Bottoni Griglia "+str(giocatore)) 

func getSimbolo():
	return simbolo[giocatore]

func  startGame():
	var children=self.get_children()
	for child in children:
		child.disabled=false
		child.get_node("Sprite2D").texture=null
	griglia=[
		"","", "",
		"","", "",
		"","", ""
	]

func hasWon():
	#print("controllaVittoria")
	for i in range(3): 
		#Controllo tutte le righe 
		if(griglia[0+3*i]==simbolo[giocatore] and griglia[1+3*i]==simbolo[giocatore] and griglia[2+3*i]==simbolo[giocatore]):  
			return true
		#Controllo le colonne
		if(griglia[0+1*i]==simbolo[giocatore] and griglia[3+1*i]==simbolo[giocatore] and griglia[6+1*i]==simbolo[giocatore]):  
			return true
		#Controllo le diagonali
		if(griglia[0]==simbolo[giocatore] and griglia[4]==simbolo[giocatore] and griglia[8]==simbolo[giocatore]):  
			return true
		if(griglia[2]==simbolo[giocatore] and griglia[4]==simbolo[giocatore] and griglia[6]==simbolo[giocatore]):  
			return true
	return  false

func aggiorna(id):
	print("aggiornaArray"+str(id))
	griglia[id]=simbolo[giocatore]
	print(griglia)
	if not hasWon(): 
		self.giocatore=(self.giocatore+1)%2 
	else:
		get_parent().endGame(giocatore)
