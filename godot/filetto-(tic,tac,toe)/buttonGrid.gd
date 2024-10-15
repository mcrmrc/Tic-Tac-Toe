extends Button

var id=-1

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	self.pressed.connect(self._button_pressed)
	self.disabled=false
	id=self.name.replace("Button","").to_int() 

func _button_pressed(): 
	self.disabled=true
	print("Premuto il pulsante: "+self.name)
	var sprite=self.get_node("Sprite2D")
	if sprite is Sprite2D: 
		if get_parent().getSimbolo()=="x":
			sprite.texture=load("res://x_filetto.png")
		elif get_parent().getSimbolo()=="o": 
			sprite.texture=load("res://o_filetto.png")
		else:
			print("Errore buttonGrid L-27")
	get_parent().aggiorna(id-1) 
