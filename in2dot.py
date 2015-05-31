#!/usr/bin/python3 -B

inputFile = open("mh-dj.in", "r")
outputFile = open("mh-dj.dot", "w");

places = [] # List of places to be sorted by their Longitude
adjList = {}
distances = []

try:
	for entry in inputFile.readlines():

		if "#" == entry[0]:
			continue

		entry = entry.split()

		if 0 == len(entry):
			continue

		assert 3 == len(entry), "Either (Name, Latitude, Longitude) OR (Place1, Place2, Distance) no more, no less"

		if entry[1].isdigit():
			assert 0 < len(entry[1]) < 5, "Latitude of {0} is of wrong size, should be 4 digits".format(entry[0])
			assert 0 < len(entry[2]) < 5, "Longitude of {0} is of wrong size, should be 4 digits".format(entry[0])

			adjList[entry[0]] = {}
			entry.reverse(); # First Long, then Lat, then Name
			places.append(entry);

		else:
			assert entry[0] in adjList.keys()
			assert entry[1] in adjList.keys()

			adjList[entry[0]][entry[1]] = entry[2]
			adjList[entry[1]][entry[0]] = entry[2]

			distances.append(entry)


	places.sort() # Sort by first Long, then Lat, then Name

	outputFile.write("graph mh {\n")
	outputFile.write("\trankdir=LR;\n")
	outputFile.write("\n")

	for name in adjList.keys():
		outputFile.write('\t"{0}" [label="{1}" shape=box]\n'.format(name, name))
	outputFile.write("\n")

	groups = []
	currGroup = []

	for place in places:
		linkExists = False;
		neighbors = adjList[place[2]].keys()
		for curr in currGroup:
			if curr[2] in neighbors:
				linkExists = True;
				break;
		if linkExists:
			groups.append(currGroup)
			currGroup = []
		currGroup.append(place)

	groups.append(currGroup)

	if len(groups) > 0:
		outputFile.write('\t{ rank = min;')
		for place in groups[0]:
			outputFile.write(' "' + place[2] + '";')
		outputFile.write(' }\n')
		groups.pop(0);

	if len(groups) > 0:
		outputFile.write('\t{ rank = max;')
		for place in groups[-1]:
			outputFile.write(' "' + place[2] + '";')
		outputFile.write(' }\n')
		groups.pop();

	for group in groups:
		outputFile.write('\t{ rank = same;')
		for place in group:
			outputFile.write(' "' + place[2] + '";')
		outputFile.write(' }\n')
	outputFile.write("\n")

	for dist in distances:
		outputFile.write('\t"{0}" -- "{1}" [label={2}]\n'.format(dist[0], dist[1], dist[2]))

	outputFile.write("}")

except Exception as exp:
	print("Exception {0}".format(exp))
finally:
	inputFile.close()
	outputFile.close()
