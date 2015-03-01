from numpy import *


class Grid:
	def __init__(self):
		self.grid = zeros(16).reshape(4,4)		#initialize empty tiles
		add_new_tile(self.grid)
		add_new_tile(self.grid)

	def get_grid(self):
		return self.grid



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


def move_grid(grid, direction):
	if direction == "left":
		grid = apply_along_axis(move,1,grid)
	if direction == "right":
		grid = rot90(grid, 2) 
		grid = apply_along_axis(move,1,grid)
		grid = rot90(grid, -2)
	if direction == "down":
		grid = rot90(grid, 3) 
		grid = apply_along_axis(move,1,grid)
		grid = rot90(grid, -3)
	if direction == "up":
		grid = rot90(grid, 1) #rotate grid anticlockwise once
		grid = apply_along_axis(move,1,grid) #apply move function for all rows in grid
		grid = rot90(grid, -1)
	return grid

def add_new_tile(grid):
	isZero = grid==0
	new_tile = append(2, zeros(isZero[isZero==True].size-1))
	random.shuffle(new_tile)	
	grid[isZero] = new_tile 

def has_adjacent(grid):
	Right = "right"
	Up = "up"
	Down = "down"
	Left = "left"
	grid_copy = copy(grid)
	if((move_grid(grid_copy, Up)==grid).all() and (move_grid(grid_copy, Down)==grid).all() and (move_grid(grid_copy, Right)==grid).all() and (move_grid(grid_copy, Left)==grid).all()):
		return False
	else:
		return True

def has_next(grid):
	isZero = grid==0
	if isZero[isZero==True].size < 1 and has_adjacent(grid)==False:
		return False
	else:
		return True




		

