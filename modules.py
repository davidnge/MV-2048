from numpy import *


class Grid:

	def __init__(self):
		self.grid = zeros(16).reshape(4,4)		#initialize empty tiles
		self.add_new_tile(self.grid)
		self.add_new_tile(self.grid)
		self.score = 0

	def get_grid(self):
		return self.grid

	def get_score(self):
		return self.score 

	def move(self, col):
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
						self.score += new_col[j]
						print self.score
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


	def move_grid(self, direction):
		if direction == "left":
			self.grid = apply_along_axis(self.move,1,self.grid)
		if direction == "right":
			self.grid = rot90(self.grid, 2) 
			self.grid = apply_along_axis(self.move,1,self.grid)
			self.grid = rot90(self.grid, -2)
		if direction == "down":
			self.grid = rot90(self.grid, 3) 
			self.grid = apply_along_axis(self.move,1,self.grid)
			self.grid = rot90(self.grid, -3)
		if direction == "up":
			self.grid = rot90(self.grid, 1) #rotate grid anticlockwise once
			self.grid = apply_along_axis(self.move,1,self.grid) #apply move function for all rows in grid
			self.grid = rot90(self.grid, -1)

		return self.grid

	def add_new_tile(self, grid):
		isZero = grid==0
		new_tile = append(2, zeros(isZero[isZero==True].size-1))
		random.shuffle(new_tile)	
		grid[isZero] = new_tile 

	def has_adjacent(self, grid):
		Right = "right"
		Up = "up"
		Down = "down"
		Left = "left"
		grid_copy = copy(grid)
		if((self.move_grid(Up)==grid_copy).all() and (self.move_grid(Down)==grid_copy).all() and (self.move_grid(Right)==grid_copy).all() and (self.move_grid(Left)==grid_copy).all()):
			return False
		else:
			return True

	def has_next(self, grid):
		isZero = grid==0
		if isZero[isZero==True].size < 1 and self.has_adjacent(grid)==False:
			return False
		else:
			return True




		

