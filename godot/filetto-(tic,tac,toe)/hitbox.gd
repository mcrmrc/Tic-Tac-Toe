extends CollisionShape2D


# Called when the node enters the scene tree for the first time.
func _ready() -> void: 
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func _input(event): 
	if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
		print("mouse button event at ", event.position)
