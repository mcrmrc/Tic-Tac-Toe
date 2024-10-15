extends Node2D

var random=RandomNumberGenerator.new()
var giocatoreInit=-1

# Called when the node enters the scene tree for the first time.
func _ready() -> void: 
	print("Filetto")
	random.seed=hash("Godot")
	#
	get_node("giocatore1").get_node("nomeGiocatore").set_text("Marco")
	get_node("giocatore1").get_node("scoreGiocatore").set_text("0")
	print(get_node("giocatore1").get_node("nomeGiocatore").text+" il tuo simbolo sarà la X")
	#
	get_node("giocatore2").get_node("nomeGiocatore").set_text("Paolo")
	get_node("giocatore2").get_node("scoreGiocatore").set_text("0")
	print(get_node("giocatore2").get_node("nomeGiocatore").text+" il tuo simbolo sarà la O")
	#
	startGame()

func startGame(): 
	self.get_node("buttons").startGame()
	giocatoreInit= random.randi_range(0,1)
	print("Inizia il giocatore"+str(giocatoreInit))

func endGame(giocatore):
	print("Gioco Finito")
	print(giocatore)
	if giocatore==0:
		var score=get_node("giocatore1").get_node("scoreGiocatore").text.to_int() 
		get_node("giocatore1").get_node("scoreGiocatore").set_text(str(score+1))
	elif giocatore==1: 
		var score=get_node("giocatore2").get_node("scoreGiocatore").text.to_int() 
		get_node("giocatore2").get_node("scoreGiocatore").set_text(str(score+1))
	startGame()
