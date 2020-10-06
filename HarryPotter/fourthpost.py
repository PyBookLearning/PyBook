from HarryPotter.py import grabs, gives
#New Settings used for this scene
class Settings:
	def __init__(self, wizard_names,moggle_names):
		self.wizard_names= ['Harry_Potter']
		self.moggle_names= ['Vernon_Dursley','Dudley_Dursley','Petunia_Dursley']
		self.equipment= ['admission_letter']
		self.pet= ['owl']
		
	def geography(self):
		london= ['Number_4_Private_Drive']
		Number_4_Private_Drive= ['cubboard_under_the_stairs', 'kitchen']
		england= ['Hut_on_the_rock']

	def movesto(self, wizard_names, geography):
		teleportation= False
		wizard1 = self.wizard_names['']
		place1= geography(poudlard [''] or london[''])
		place2= geography(poudlard[''] or london[''])
		if wizard1 in place1:
			teleportation= True
			wizard1.movesto(place2)

	def destroy(self, wizard_names, equipment):
		destroying= False
		wizard1 = self.wizard_names['']
		moggle1= self.moggle_name['']
		equipment1= self.equipment['']
		if wizard1 or moggle1 and equipment1:
			destroying= True
			wizard1.destroy(equipment1)
			moggle1.destroy(equipment1)

class Chapter1:
def third_scene(self):
	context= geography(london[0], Number_4_Private_Drive[0,1])
	letter= f"('Dear Mr {wizard_names[0]}, We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry')"
	admission_letters= [range()]
	pet1= self.pet[0]
	wizard1= self.wizard_names[0]
	moggle1= self.moggle_names [0,1,2]
	wizard1.grabs(letter)= False
	while pet1.gives(letter) and moggle_names[0].destroy(equipment[0]):      #1
		for admission_letter in admission_letters.range(sys.maxsize):        #2 and 3
			admission_letters.append('letter') 								 #4
	wizard1.grabs(letter)= True	
		if wizard1.grabs(letter) = True:									 #5
			break
	wizard1.movesto(england[0])												 #6
	moggle1.movesto(england[0])												 #7

#We create a while lopp here to represent each letter sent by an owl to harry that ends up not being read and destroy by Vernon (#1)
#Here we nest a for loop to say that for every letter that is destroyed the item goes in our admission_letter list (#2)
#sys.maxsize says that the number of destroyed letters can be infiite (#3)
#append is here to say that every elements is added in our list as a letter (#4)
#We end the while loop if Harry manages to grab a letter symbolized by the break control(#5)
#The scene ends with all our characters moving to Hut on the Rock which is the lighthouse that Vernon rents to escape Hogwart's letter (#6&7)




