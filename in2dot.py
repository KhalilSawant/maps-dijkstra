#!/usr/bin/python

inputFile = open("mh-dj.in", "r")
outputFile = open("mh-dj.dot", "w");

listOfPlaces = []
setOfPlaces = set()
listOfDistances = []

try:
	for place in inputFile.readlines():
		place = place.split()
		assert 3 == len(place), "Either (Name, Latitude, Longitude) OR (Place1, Place2, Distance) no more, no less"

		if place[1].isdigit():
			assert 0 < len(place[1]) < 5, "Latitude of {0} is of wrong size, should be 4 digits".format(place[0])
			assert 0 < len(place[2]) < 5, "Longitude of {0} is of wrong size, should be 4 digits".format(place[0])

			setOfPlaces.add(place[0])
			place.reverse(); # First Long, then Lat, then Name
			listOfPlaces.append(place);

		else:
			assert place[0] in setOfPlaces
			assert place[1] in setOfPlaces

			listOfDistances.append(place)

	listOfPlaces.sort() # Sort by first Long, then Lat, then Name

	outputFile.write("graph mh {\n")
	outputFile.write("\trankdir=LR;\n")
	outputFile.write("\n")

	for name in setOfPlaces:
		outputFile.write('\t"{0}" [label="{1}" shape=box]\n'.format(name, name))
	outputFile.write("\n")

	if listOfPlaces > 0:
		outputFile.write('\t{ rank = min; "' + listOfPlaces[0][2] + '"; }\n')
		listOfPlaces.pop(0);

	if listOfPlaces > 0:
		outputFile.write('\t{ rank = max; "' + listOfPlaces[-1][2] + '"; }\n')
		listOfPlaces.pop();

	for place in listOfPlaces:
		outputFile.write('\t{ rank = same; "' + place[2] + '"; }\n')
	outputFile.write("\n")

	for dist in listOfDistances:
		outputFile.write('\t"{0}" -- "{1}" [label={2}]\n'.format(dist[0], dist[1], dist[2]))

	outputFile.write("}")

except Exception as exp:
	print "Exception {0}".format(exp)
finally:
	inputFile.close()
	outputFile.close()
