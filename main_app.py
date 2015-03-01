from numpy import *
from Tkinter import *
from tkFont import Font
from modules import *

score = 0
can_play = True
intList = []
size = 480

def key_listener(event, grid=None):
	key_dict = {'Up': 'up', 'Down': 'down', 'Left': 'left', 'Right': 'right'}
	key = '{}'.format(event.keysym)
	gridArray = grid.get_grid()
	gridArray = move_grid(gridArray, key_dict[key])
	add_new_tile(gridArray)
	grid.grid = gridArray
	for (m, n), value in ndenumerate(gridArray):
		text = int(gridArray[m][n])
		label.config(text=text, fg='#ffffff', bg='#000000')

	print key
	print gridArray



if __name__ == '__main__':

	Grid = Grid()
	gridArray =  Grid.get_grid()
	root = Tk()
	root.geometry("480x480")
	gridSize = 480
	for (m, n), value in ndenumerate(gridArray):
	    frame = Frame(root, width=size/4-2, height=size/4-2)
	    font = Font(family='Helvetica', weight='bold', size=size/16	)
	    frame.pack_propagate(0)
	    frame.place(x=n*size/4+1, y=m*size/4+1)
	    label = Label(frame, text=int(value), font=font, fg='#ffffff', bg='#000000')
	    label.pack(fill=BOTH, expand=True)
	root.bind('<Key>', lambda event: key_listener(event, grid=Grid))
	root.mainloop()


	'''
	while can_play==True or score>=2048:
		print grid
		direction = raw_input("Enter direction: ")
		prev = grid
		grid = move_grid(grid, direction)
		if (grid == prev).all():
			pass
		else:
			add_new_tile(grid)
			can_play = has_next(grid)

'''


