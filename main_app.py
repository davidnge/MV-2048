from modules import *

grid = zeros(16).reshape(4,4)
add_new_tile(grid)
add_new_tile(grid)	
score = 0
can_play = True


while can_play==True or score>=2048:
	print grid
	direction = raw_input("Enter direction: ")
	prev = grid
	grid = move_board(grid, direction)
	if (grid == prev).all():
		pass
	else:
		add_new_tile(grid)
		can_play = has_next(grid)





