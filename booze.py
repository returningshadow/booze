#!/usr/bin/python
def calc(n):
	name = raw_input("What is the name of the alcohol? ") #asks for alcohol name
	size = float(raw_input("What size is the bottle of %s? (in ml) " % (name))) #asks for size of the bottle
	price = float(raw_input("How much does %s cost? " % (name))) #asks for alcohol price
	abv = float(raw_input("What is the ABV of %s? " % (name))) #asks for ABV

	cost_per_ml = price / (size * (abv / 100))
	while(notdone):
		if choice = raw_input("Do you wish to add another bottle? ").lower() = "yes".lower():
			return n + 1
			calc(n)
			else:
				print "%s costs $%s per ml of ethanol." % (name,cost_per_ml) #this is the crap that doesn't work
	#print "%s costs $%s per ml of ethanol." % (name,cost_per_ml)
	

n=0
calc(n)
print str(n)
raw_input()
