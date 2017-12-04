from pathlib import Path
from json import loads
from json import dump

def loadData():
	contacts = []
	
	contactsFile = Path("contacts.json")
	
	if contactsFile.is_file():
		contacts = loads(open("contacts.json").read())
			
	return contacts


def saveData(contacts):
	with open("contacts.json", "w") as fout:
		dump(contacts, fout)
