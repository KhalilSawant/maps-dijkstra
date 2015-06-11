#!/usr/bin/python3 -B

inputFile = open("mh-dj.in", "r")
outputFile = open("mh-dj.dot", "w")

places = [] # List of places to be sorted by their Longitude
adjList = {}
distances = []

try:
	minY = 999999
	minX = 999999

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

			if int(entry[2]) < minX:
				minY = int(entry[2])
			if int(entry[1]) < minY:
				minY = int(entry[1])

			places.append(entry)

		else:
			assert entry[0] in adjList.keys(), "{0} not present in list of places".format(entry[0])
			assert entry[1] in adjList.keys(), "{0} not present in list of places".format(entry[1])

			adjList[entry[0]][entry[1]] = entry[2]
			adjList[entry[1]][entry[0]] = entry[2]

			distances.append(entry)

	outputFile.write("graph mh {\n")
	outputFile.write("\tnode [shape=box fontsize=36]\n\n")

	for place in places:
		outputFile.write('\t"{0}" [label="{1}" pos="{2},{3}!"]\n'.format(place[0], place[0], 36*(int(place[2])-minX), 36*(int(place[1])-minY)) )
	outputFile.write("\n")

	for dist in distances:
		outputFile.write('\t"{0}" -- "{1}" [label={2} fontsize=48]\n'.format(dist[0], dist[1], dist[2]))

	outputFile.write("\n}")

except Exception as exp:
	print("Exception {0}".format(exp))
finally:
	inputFile.close()
	outputFile.close()
