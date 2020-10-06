#See Settings post for function detail
from secondpost.py import talksto(), answerto(), getsangry(), getshappy()

#Settings used for this scene

class Settings:
	def __init__(self, wizard_names,moggle_names):
		self.wizard_names= ['Harry_Potter']
		self.moggle_names= ['Vernon_Dursley','Dudley_Dursley', 'Petunia_Dursley']
		
	def geography(self):
		london= ['Number_4_Private_Drive']
		Number_4_Private_Drive= ['cubboard_under_the_stairs', 'kitchen']

class Chapter1:
def second_scene(self):
		present= []
		moggle1= self.moggle_names
		moggle2= self.moggle_names
		wizard1= self.wizard_names
#Harry wakes from his bed and join the kitchen for Dudley's birthday, dialogue
		moggle1[1].talksto(wizard1[0])
		moggle1.input('Do you know what day it is today?')
		if input == 'Yes':
		wizard1[0].answerto(moggle1[1])
		print('Your birthday I guess')
		elif input == 'No':
			wizard1[0].answerto(moggle1[1])
			print('I guess I will soon find out')
		else:
			break
# Dudley asks his father Vernon about his birthday presents
		moggle1[1].talksto(moggle2[0])
		moggle1.input(f"How many {presents} did I get this year?")
		present.append(input)
		for presents in present:
			if presents <= 38:
				moggle1[1].getsangry()
				moggle2[2].buys(presents)
				present.append(36+2)
			elif presents >= 38:
				moggle1[1].getshappy()


		
		
		