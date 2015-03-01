from numpy import *
from Tkinter import *
from tkFont import Font
from modules import *

score = 0
can_play = True
intList = []
size = 480

def key_listener(event, grid=None, labelList=None):
	gridArray = grid.get_grid()
	if has_next(gridArray) == True:
		key_dict = {'Up': 'up', 'Down': 'down', 'Left': 'left', 'Right': 'right'}
		key = '{}'.format(event.keysym)
		prev = gridArray
		gridArray = move_grid(gridArray, key_dict[key])

		if (gridArray == prev).all():
			pass
		else:
			add_new_tile(gridArray)

		grid.grid = gridArray
		for (m, n), value in ndenumerate(gridArray):
			text = '{}'.format('' if (gridArray[m][n])==0 else int(gridArray[m][n]))
			labelList[4*m+n].config(text=text)
		print key
		print gridArray

	else:
		print "game over"





if __name__ == '__main__':

	Grid = Grid()
	gridArray =  Grid.get_grid()
	root = Tk()
	root.geometry("480x480")
	gridSize = 480
	labelList = []
	for (m, n), value in ndenumerate(gridArray):
	    frame = Frame(root, width=size/4-2, height=size/4-2)
	    font = Font(family='Helvetica', weight='bold', size=size/16	)
	    frame.pack_propagate(0)
	    frame.place(x=n*size/4+1, y=m*size/4+1)
	    label = Label(frame, text='{}'.format('' if (gridArray[m][n])==0 else int(gridArray[m][n])), font=font, fg='#ffffff', bg='#000000')
	    label.pack(fill=BOTH, expand=True)
	    labelList.append(label)

	root.bind('<Key>', lambda event: key_listener(event, grid=Grid, labelList = labelList))
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


