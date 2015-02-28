from numpy import *

all_tiles = zeros(16).reshape(4,4)				#initialize empty tiles
all_tiles[random.choice(16,2)] = 2		#initialize  2 to random 2 tiles


def move(col):
	new_col = zeros(4)
	j = 0
	prev = None
	for i in range(col.size):
		if col[i] != 0:
			if prev == None:
				prev = col[i]
			else:
				if col[i] == prev:
					new_col[j] = 2*col[i]
					col[i] = 0
					prev = None
					j+=1
				else: 
					new_col[j] = prev
					prev = col[i]
					j+=1
	if prev != None:
		new_col[j] = prev
	return new_col


def move_board(grid, direction):
	if direction == "up":
		grid = rot90(grid, 1) #rotate grid anticlockwise once
		apply_along_axis(move,1,grid) #apply move function for all rows in grid
		grid = rot90(grid, -1)

	if direction == "down":
		grid = rot90(grid, 3) 
		apply_along_axis(move,1,grid)
		grid = rot90(grid, -3)

	if direction == "left":
		apply_along_axis(move,1,grid)

	if direction == "right":
		grid = rot90(grid, 2) 
		apply_along_axis(move,1,grid)
		grid = rot90(grid, -2)

def add_new_tile(grid):
	isZero = grid==0
	new_tile = append(2, zeros(isZero[isZero==True].size-1)
	random.shuffle(new_tile)	#rearrange randomly where the new tile is among the zeros in grid
	grid[isZero] = new_tile 	



		

