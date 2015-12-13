from app import models, db

seneca = models.Stimulus(
	name="Seneca the Younger",
	image="seneca.jpg",
	start_year=-4,
	end_year=65,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Seneca_the_Younger",
	description="Legendary orator who became consul. Was forced out by Caesar and eventually killed by his successor, Augustus.")

db.session.add(seneca)
db.session.commit()

ides = models.Stimulus(
	name="Assassination of Julius Caesar",
	image="idesofmarch.jpg",
	start_year=-44,
	end_year=-44,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Assassination_of_Julius_Caesar",
	description="The murder of Caesar by Brutus Cassius and others.")

db.session.add(ides)
db.session.commit()

augustus = models.Stimulus(
	name="Augustus",
	image="augustus.jpg",
	start_year=-63,
	end_year=14,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Augustus",
	description="Founder and first emperor of the Roman Empire.")

db.session.add(augustus)
db.session.commit()

marcusaurelius = models.Stimulus(
	name="Marcus Aurelius",
	image="marcusaurelius.jpg",
	start_year=121,
	end_year=180,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Marcus_Aurelius",
	description="Roman emperor. Famous today for Meditations, his diary.")

db.session.add(marcusaurelius)
db.session.commit()

nero = models.Stimulus(
	name="Nero",
	image="nero.jpg",
	start_year=37,
	end_year=68,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Nero",
	description="Roman emperor who many Romans blamed for the the Great Fire of Rome.")

db.session.add(nero)
db.session.commit()

secondpunicwar = models.Stimulus(
	name="Second Punic War",
	image="secondpunicwar.jpg",
	start_year=-218,
	end_year=-201,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Second_Punic_War",
	description="War between Rome and Carthage where Hannibal invaded Italy.")

db.session.add(secondpunicwar)
db.session.commit()
'''
firsttriumvirate = models.Stimulus(
	name="First Triumvirate",
	image="firsttriumvirate.jpg",
	start_year=-59,
	end_year=-53,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/First_Triumvirate",
	description="Unoffocial alliance between Caesar, Pompey the Great and Crassus.")

db.session.add(firsttriumvirate)
db.session.commit()
'''
pompeythegreat = models.Stimulus(
	name="Pompey the Great",
	image="pompeythegreat.jpg",
	start_year=-106,
	end_year=-58,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Pompey",
	description="Military and political leader of the late Roman Republic. Killed when leading a civil war.")

db.session.add(pompeythegreat)
db.session.commit()

secondtriumvirate = models.Stimulus(
	name="Second Triumvirate",
	image="pompeythegreat.jpg",
	start_year=-43,
	end_year=-33,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Second_Triumvirate",
	description="Official political alliance between Augustus, Mark Antony and Lepidus.")

markantony = models.Stimulus(
	name="Mark Antony",
	image="markantony.jpg",
	start_year=-83,
	end_year=-30,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Mark_Antony",
	description="Roman politician and general who went to war against Rome. Husband of Cleopatra.")

db.session.add(markantony)
db.session.commit()

sackingofcarthage = models.Stimulus(
	name="Sacking of Carthage",
	image="sackingofcarthage.jpg",
	start_year=-149,
	end_year =-146,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Battle_of_Carthage_(c._149_BC)",
	description="The complete descruction of Carthage by Roman ending the rivalry between the states.")

db.session.add(sackingofcarthage)
db.session.commit()

hadrian = models.Stimulus(
	name="Hadrian",
	image="hadrian.jpg",
	start_year=76,
	end_year=138,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Hadrian",
	description="Roman emperor who rebuilt the Pantheon and has Castel Sant'Angelo as mausoleum.")

db.session.add(hadrian)
db.session.commit()

battleofcorinth = models.Stimulus(
	name="Battle of Corinth",
	image="battleofcorinth.jpg",
	start_year=-146,
	end_year=-146,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Battle_of_Corinth_(146_BC)",
	description="Battle between Rome and Greek city states, ending in complete Roman hedgemony over Greece.")

db.session.add(battleofcorinth)
db.session.commit()

battleofcorinth = models.Stimulus(
	name="Battle of Corinth",
	image="battleofcorinth.jpg",
	start_year=-146,
	end_year=-146,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Battle_of_Corinth_(146_BC)",
	description="Battle between Rome and Greek city states, ending in complete Roman hedgemony over Greece.")

firstpunicwar = models.Stimulus(
	name="First Punic War",
	image="firstpunicwar.gif",
	start_year=-264,
	end_year=-241,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/First_Punic_War",
	description="First war between Rome and Carthago which lasted for more than 20 years.")

db.session.add(firstpunicwar)
db.session.commit()

'''
thirdservilewar = models.Stimulus(
	name="Third Servile War",
	image="thirdservilewar.jpg",
	start_year=-264,
	end_year=-241,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Third_Servile_War",
	description="A slave revolt of 120,000 men, women and children of whom Spartacus was a leader.")

db.session.add(thirdservilewar)
db.session.commit()
'''

cicero = models.Stimulus(
	name="Cicero",
	image="cicero.jpg",
	start_year=-106,
	end_year=-43,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Cicero",
	description="Roman philosopher, politician, orator and one of the greatest Latin writers.")

db.session.add(cicero)
db.session.commit()

catotheyounger = models.Stimulus(
	name="Cato the Younger",
	image="catotheyounger.jpg",
	start_year=-95,
	end_year=-46,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Cato_the_Younger",
	description="Roman politician and follower of Stoic philosophy. Remembered for his moral integrity and famous suicide.")

db.session.add(catotheyounger)
db.session.commit()

socrates = models.Stimulus(
	name="Socrates",
	image="socrates.jpg",
	start_year=-469,
	end_year=-399,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Socrates",
	description="Classical Greek philosopher credited as one of the founders of Western philosophy.")

db.session.add(socrates)
db.session.commit()

alexanderthegreat = models.Stimulus(
	name="Alexander the Great",
	image="alexanderthegreat.jpg",
	start_year=-336,
	end_year=-323,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Alexander_the_Great",
	description="Probably the most successful military commander of all time who conquered most of the known world. Undefeated in battle.")

db.session.add(alexanderthegreat)
db.session.commit()

battleofthermopylae = models.Stimulus(
	name="Battle of Thermopylae",
	image="battleofthermopylae.jpg",
	start_year=-480,
	end_year=-480,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Battle_of_Thermopylae",
	description="Famous battle between Greek city states and Persia. King Leonidas made a hold with 300 Spartans.")

db.session.add(battleofthermopylae)
db.session.commit()

battleofsalamis = models.Stimulus(
	name="Battle of Salamis",
	image="battleofsalamis.jpg",
	start_year=-480,
	end_year=-480,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Battle_of_Salamis",
	description="Naval battle between Greek city-states, led by Themistocles, and the Persian Empire. Greek victory.")

db.session.add(battleofsalamis)
db.session.commit()

peloponnesianwar = models.Stimulus(
	name="Peloponnesian War",
	image="peloponnesianwar.png",
	start_year=-431,
	end_year=-404,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Peloponnesian_War",
	description="War between Athens and (mainly) Sparta which lasted for 27 years.")

db.session.add(peloponnesianwar)
db.session.commit()

aristotle = models.Stimulus(
	name="Aristotle",
	image="aristotle.jpg",
	start_year=-384,
	end_year=-322,
	stimulus_type="person",
	wiki_link="https://en.wikipedia.org/wiki/Aristotle",
	description="Greek philosopher and scientist prominent in subjects ranging from physics to ethics.")

db.session.add(aristotle)
db.session.commit()

'''
pyrrhicwar = models.Stimulus(
	name="Pyrrhic War",
	image="pyrrhicwar.png<",
	start_year=-280,
	end_year=-275,
	stimulus_type="event",
	wiki_link="https://en.wikipedia.org/wiki/Pyrrhic_War",
	description="War between Greeks and Romans where Pyrrhus marched on Rome.")

db.session.add(pyrrhicwar)
db.session.commit()
'''

