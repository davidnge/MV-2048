from numpy import *
from Tkinter import *
from tkFont import Font
from modules import *

# {(number value color: tile background color)}
color_dict = { 2: ('#776e65', '#eee4da'), 4: ('#776e65', '#ede0c8'), 8: ('#f9f6f2', '#f2b179'), 16: ('#f9f6f2', '#f59563'), 32: ('#f9f6f2', '#f67c5f'), 64: ('#f9f6f2', '#f65e3b'), 128:('#f9f6f2', '#edcf72'), 256: ('#f9f6f2', '#edcc61'), 512: ('#f9f6f2', '#edc850'),1024: ('#f9f6f2', '#edc53f'),2048: ('#f9f6f2', '#edc22e'), 'zero' : '#ccc0b3'}

def displayImg(root=None, status=None):
	winner = "winner.gif"
	loser = "loser.gif"
	img = None
	if status == "loser":
		img = PhotoImage(file=loser)
	elif status == "winner":
		img = PhotoImage(file=winner)

	imgLabel = Label(root, image=img, height=480, width=480)
	imgLabel.photo = img
	imgLabel.pack()

def key_listener(event, grid=None, labelList=None, root=None):
	gridArray = grid.get_grid()

	#Can still play
	if grid.has_next(gridArray) == True:

		key_dict = {'Up': 'up', 'Down': 'down', 'Left': 'left', 'Right': 'right'}
		key = '{}'.format(event.keysym)
		prev = gridArray
		gridArray = grid.move_grid(key_dict[key])

		# wins the game
		if amax(gridArray) == 2048: #if highest tile == 2048
			winner = "winner"
			displayImg(root=root, status=winner)

		if (gridArray == prev).all(): #same keystroke doesnt change tile positions
			pass
		else:
			grid.add_new_tile(gridArray)

		grid.grid = gridArray
		root.title('Your Score: {}'.format(int(grid.get_score())))

		#redraw tiles after a move has been made
		for (m, n), value in ndenumerate(gridArray):
			text = '{}'.format('' if (gridArray[m][n])==0 else int(gridArray[m][n]))
			labelList[4*m+n].config(text=text, fg=color_dict['zero'] if (gridArray[m][n])==0 else color_dict[value][0], bg=color_dict['zero'] if (gridArray[m][n])==0 else color_dict[value][1])

	#Lose Game
	else:
		loser = "loser"
		displayImg(root=root, status=loser)


if __name__ == '__main__':

	Grid = Grid()
	gridArray =  Grid.get_grid()
	score = 0
	root = Tk()
	root.geometry("480x480")
	gridSize = 480
	labelList = []
	root.title('Bring it on!')

	#draw initial tiles
	for (m, n), value in ndenumerate(gridArray):
	    frame = Frame(root, width=gridSize/4-2, height=gridSize/4-2)
	    font = Font(family='Clear Sans', weight='bold', size=40)
	    frame.pack_propagate(0)
	    frame.place(x=n*gridSize/4+1, y=m*gridSize/4+1)
	    label = Label(frame, text='{}'.format('' if (gridArray[m][n])==0 else int(gridArray[m][n])), font=font, fg=color_dict[2][0], bg=color_dict['zero'] if (gridArray[m][n])==0 else color_dict[value][1])
	    label.pack(fill=BOTH, expand=True)
	    labelList.append(label)

	root.bind('<Key>', lambda event: key_listener(event, grid=Grid, labelList = labelList, root=root))
	root.mainloop()




