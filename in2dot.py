#!/usr/bin/python3 -B

def addGroupToGroups(groups, group):
	groupId = len(groups)
	for place in group:
		place[0] = groupId
	group.sort()
	group.reverse()
	groups.append(group)

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
			assert entry[0] in adjList.keys(), "{0} not present in list of places".format(entry[0])
			assert entry[1] in adjList.keys(), "{0} not present in list of places".format(entry[1])

			adjList[entry[0]][entry[1]] = entry[2]
			adjList[entry[1]][entry[0]] = entry[2]

			distances.append(entry)


	places.sort() # Sort by first Long, then Lat, then Name

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
			addGroupToGroups(groups, currGroup)
			currGroup = []
		currGroup.append(place)

	addGroupToGroups(groups, currGroup)

	outputFile.write("graph mh {\n")
	outputFile.write("\trankdir=LR;\n\n")

	outputFile.write("\t{\n")
	outputFile.write("\t\tnode [shape=plaintext label=\"\"]\n")
	if len(groups) > 0:
		outputFile.write("\t\t0")
	for i in range(len(groups)-1):
		 outputFile.write(" -- {0}".format(i+1))
	outputFile.write("\n\t}\n\n")

	outputFile.write("\tnode [shape=box]\n")
	for name in adjList.keys():
		outputFile.write('\t"{0}" [label="{1}"]\n'.format(name, name))
	outputFile.write("\n")

	groupId = 0;
	for group in groups:
		outputFile.write('\t{ rank = same;')
		outputFile.write(' "{0}";'.format(groupId))
		for place in group:
			outputFile.write(' "' + place[2] + '";')
		outputFile.write(' rankdir=TB }\n')
		groupId += 1;
	outputFile.write("\n")

	for dist in distances:
		outputFile.write('\t"{0}" -- "{1}" [label={2}]\n'.format(dist[0], dist[1], dist[2]))

	outputFile.write("}")

except Exception as exp:
	print("Exception {0}".format(exp))
finally:
	inputFile.close()
	outputFile.close()
