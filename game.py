import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

direction=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

class GameOfLife:

	def __init__(self,initial):
		if initial==None:
			initial=[]
		self.existing_state=initial
		#print(self.existing_state)
		self.next_state=[]
		self.generation=0
		self.all_neighbours=[]

	#to find the livinig neighbours
	def alive_cells(self,cell):
		living_neighbour=[]
		for i in direction:
			new_cell=[i[0]+cell[0],i[1]+cell[1]]
			if new_cell in self.existing_state:
				living_neighbour.append(new_cell)

		if(len(living_neighbour)==2 or len(living_neighbour)==3):
			if cell not in self.next_state:
				self.next_state.append(cell)
		

	#to revert back the dead cell to alive
	def dead_to_alive(self,cell):
		living_neighbour=[]
		for i in direction:
			new_cell=[i[0]+cell[0],i[1]+cell[1]]
			if new_cell in self.existing_state:
				living_neighbour.append(new_cell)

		if(len(living_neighbour)==3):
			if cell not in self.next_state:
				self.next_state.append(cell)
		

	#to find all 8-neighbours of a cell
	def find_all_neighbour(self,cell):
		for i in direction:
			new_cell=[i[0]+cell[0],i[1]+cell[1]]
			if new_cell not in self.all_neighbours and new_cell not in self.existing_state:
				self.all_neighbours.append(new_cell)
		

		for i in self.all_neighbours:
			self.dead_to_alive(i)


	def generate(self):
		for cell in self.existing_state:
			self.alive_cells(cell)
			self.find_all_neighbour(cell)
				
		self.generation+=1	
		#print(self.next_state," ",self.generation)
		self.existing_state=self.next_state
		self.next_state=[]	




def update(frameNum, img, grid,obj):
	if len(obj.existing_state)==0:
		return
	else:
		obj.generate()
		try:
			newGrid=[[0 for i in range(50)]for i in range(50)]
			new_points=obj.existing_state
		
			for i in new_points:
				newGrid[i[0]][i[1]]=1

			img.set_data(newGrid)
			grid[:] = newGrid[:]
			return img,

		except IndexError:
			boundary=max(obj.existing_state)
			newGrid=[[0 for i in range(boundary[0]+50)]for i in range(boundary[1]+50)]
			new_points=obj.existing_state
		
			for i in new_points:
				newGrid[i[0]][i[1]]=1

			img.set_data(newGrid)
			grid[:] = newGrid[:]
			return img,


def main():
	start_state=[]
	print("Enter cordinates for initial state.e.g:20,11")
	print("Enter 's' to generate the pattern")
	while True:
		user=input("")
		if(user=="S" or user=="s"):
			break
		else:
			cord=user.split(",")
			start_state.append([int(cord[0]),int(cord[1])])
	
	obj=GameOfLife(initial=start_state)
	grid =[[0 for i in range(50)]for i in range(50)]
	for cell in start_state:
		grid[cell[0]][cell[1]]=1
	fig, ax = plt.subplots()
	img = ax.imshow(grid, interpolation='nearest') 
	ani = animation.FuncAnimation(fig, update, fargs=(img, grid,obj, ), 
                                frames = 10, 
                                interval=500, 
                                save_count=50) 
	plt.show()

if __name__ == '__main__': 
    main()   
