import settings.py
# All settings, self functions including action definition are available in my twitter Bio 

class the_Fellowship_of_the_ring:
	def first_scene(self):
		context= self.geography.middle_earth['Shire','Old_Forest','Rivendell']
		wizard1= self.wizard_name['Gandalf']
		hobbit1= self.hobbit_names['Frodo_Baggins', 'Samwise_Gamgee', 'Merry_Brandybuck', 'Pippin_Took']
		darkrider1= self.dark_names['Dark_riders']
		equipment1= self.equipment['the_ring']
		ringmission= hobbit1[0].destroys(equipment1[0])
		wizard1.gives(equipment1[0])
		hobbit1[0].receives(equipment1[0])
		wizard1.talksto(hobbit1[0])
		wizard1.input(f"You need to bring the ring infront of the fellowship, will you meet me in {context[2]}?)"
		if inputs == 'Yes':
			hobbit1[0,1,2,3].movesto(context[1])
		if input == 'No':
			hobbit1.staysin(context[0])
			darkrider1.kills(hobbit1)
			darkrider1.grabs(equipment1[0])
			ringmission= False
		else:
			break




			




