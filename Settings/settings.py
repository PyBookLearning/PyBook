	

class Settings:


	def __init__(self, wizard_names,wizard_blood,choice_of_side, age, gender,eye_colour, hair_colour, equipment, pet, magic_house):
		self.wizard_names= ['Harry', 'Hermione', 'Ron', 'Voldemort', 'Dumbledore','Neville Longbottom']
		self.moggle= ['dudley_family']
		self.wizard_blood= ['pure blood', 'half blood', 'moggle']
		self.choice_of_side= ['evil', 'good']
		self.spells['expeliarmus', 'alomora', 'avadakadabra']
		self.age= range(150)
		self.gender= ['male', 'female', 'animal/creature']
		self.eye_colour= ['blue', 'red', 'brown', 'black', 'yellow', 'grey']
		self.hair_colour= ['blue', 'red', 'brown', 'black', 'blond', 'grey', 'bold']
		self.equipment= ['presents','glasses', 'wand', 'bag', 'Rememberless', 'purple turban', 'invisible cape']
		self.pet= ['owl', 'rat', 'cat', 'frog', 'dog', 'cat', 'eagle', 'snake', 'eagle']
		self.magic_house= ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']



	def geography(self):
		poudlard= ['gryffindor_quarter', 'hufflepuff_room','ravenclaw_room', 'event_room', 'dumbledore_office','library', 'class_room', 'hospital_wing', 'forbidden_forest', 'dungeon','sky']
		london= ['ministry_of_magic','harry_home', 'zoo','hogwarts_express','the_burrow', 'diagon_alley', 'sky']
		home_rooms=['kitchen', 'living room', 'bedroom']
	
	def talksto(self, wizard_names, speak):
		speak= False
		wizard1 = self.wizard_names[''] 
		wizard2 = self.wizard_names['']
		moggle1= self.moggle_name['']
		moggle2= self.moggle_name['']
		if wizard_names or self.moggle >= 2:
			speak= True
			wizard1.talksto(wizard2) or wizard1.talksto(moggle1) or wizard1.talksto(moggle2) or moggle1.talksto(moggle2) or moggle1.talksto(wizard1)

		else:
			speak= True
			wizard_names.append()
			moggle_name.append()
			wizard1.talksto(wizard2) or wizard1.talksto(moggle1) or wizard1.talksto(moggle2) or moggle1.talksto(moggle2) or moggle1.talksto(wizard1)
				
	def answerto(self, wizard_names, answer):
		answer= False
		if wizard1.talksto(wizard2) or wizard1.talksto(moggle1) or wizard1.talksto(moggle2) or moggle1.talksto(moggle2) or moggle1.talksto(wizard1):
			answer= True
			individual2[''].answerto(individual1[''])
		else individual2[''].talksto(individual1['']):
			answer=True
			individual1[''].answerto(individual2[''])



	def staywith(self, wizard_names, geography):
		staying= False
		

	def movesto(self, wizard_names, geography):
		teleportation= False
		wizard1 = self.wizard_names['']
		place1= geography(poudlard [''] or london[''])
		place2= geography(poudlard[''] or london[''])
		if wizard1 in place1:
			teleportation= True
			wizard1.movesto(place2)

	def arrivesfrom(self, wizard_names):
		arrival= self.wizard_names['']
		arrival.arrivesfrom(geography(poudlard[''] or london['']))

	def grabs(self, wizard_names, equipment):
		grabbing = False
		wizard1grabs= self.wizard_names['']
		itembeinggrabbed= self.equipment['']
		if wizard1grabs and itembeinggrabbed:
			grabbing= True
			wizard1grabs.grabs(itembeinggrabbed)
		else:
			grabbing= False

	def gives(self, wizard_names, equipment):
		giving = False
		wizard1gives= self.wizard_names['']
		itembeinggiven= self.equipment['']
		if wizard1gives and itembeinggiven:
			giving= True
			wizard1gives.gives(itembeinggrabbed)
		else:
			giving= False


	
	def leaves(self,wizard_names):
		leaving= False
		wizard1leaving= wizard_names['']
		wizard2beingleft= wizard_names ['']
		if wizard1leaving and wizard2beingleft:
			leaving= True
			wizard1leaving.leaves(wizard2beingleft)
		else:
			leaving = True
			wizard2beingleft.leaves(wizard1leaving)

	def fights(self, wizard_names):
		fighting= False
		wizard1fighting= wizard_names['']
		wizard2fighting= wizard_names['']
		if wizard1fighting and wizard2fighting:
			fighting= True
			wizard1fighting.fights(wizard2fighting)
		else:
			fighting= False

	def injures(self, fights, wizard1fighting, wizard2fighting):
		injuring= False
		if wizard1fighting.fights(wizard2fighting):
			injuring= True
			wizard1fighting.injures(wizard2fighting) or wizard2fighting.injures(wizard1fighting)
		else:
			injuring= False

	def kills(self, fights, wizard1fighting, wizard2fighting):
		killing= False
		if wizard1fighting.fights(wizard2fighting):
			killing= True
			wizard1fighting.kills(wizard2fighting) or wizard2fighting.kills(wizard1fighting)
		else:
			killing= False

	def casts(self, spells, wizard_names, wizard1fighting, wizard2fighting):
		casting= False
		wizard1spells= self.spells['']
		wizard2spells= self.spells['']
		if wizard1spells:
			casting= True
			wizard1spells.casts()
		elif wizard2spells:
			casting= True
			wizard2spells.casts()
		else:
			casting= False
