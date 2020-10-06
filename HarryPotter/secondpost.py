
#Settings Used for first_scene
class Settings:
	def __init__(self, wizard_names,wizard_blood,choice_of_side, age, gender,eye_colour, hair_colour, equipment, pet, magic_house):
		self.wizard_names= ['Harry_Potter', 'Minerva_McGonagall','Albus_Dumbledore', 'Rebeus_Hagrid']
	
	def geography(self):
		london= ['Godricks_allow']

	def talksto(self, wizard_names, speak):
		speak= False
		wizard1 = self.wizard_names[''] 
		wizard2 = self.wizard_names['']
		if wizard_names >= 2:
			speak= True
			wizard1.talksto(wizard2) or wizard2.talksto(wizard1) 
		
	def answerto(self, wizard_names, answer):
		answer= False
		if wizard1.talksto(wizard2) or wizard2.talksto(wizard1)
			answer= True
			wizard2[''].answerto(wizard1[''])
		else wizard2[''].talksto(wizard1['']):
			answer=True
			wizard1[''].answerto(wizard2[''])

# Introduction
class Chapter1:
	def first_scene(self):
		context= london[0]
		#Macgonald speaks to Dumbledore
		wizard1[1].talksto(wizard2[2])
		wizard1.imput(f"Where is the kid?")
		wizard2[2].answerto(wizard1[1])
		print(f"{wizard_names[0]} 'is with' {wizard_names[3]}")
		wizard1[1].answerto(wizard1[2])
		wizard1.imput(f"Are you sure we can trust {wizard_names[3]} with the baby?")
		# Hagrid with McGonagall
		wizard1[3].talksto(wizard2[1])
		wizard1.imput('the kid is safe in my hand')
		wizard2[2].answerto(wizard1[3])
		print(f"I know {wizard_names[3]}, I would trust you with my own life")
		
