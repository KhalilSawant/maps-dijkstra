#!/usr/bin/python3 -B

from graph import Graph

def traverse(dist, pre, start, curr):
	if pre[curr] != start:
		traverse(dist, pre, start, pre[curr])
	print(" {0}({1})".format(curr, dist[curr]), end="")


inputFile = open("mh-dj.in", "r")

try:

	g = Graph()

	for entry in inputFile.readlines():

		if "#" == entry[0]:
			continue

		entry = entry.split()

		if 0 == len(entry):
			continue

		assert 3 == len(entry), "Either (Name, Latitude, Longitude) OR (Place1, Place2, Distance) no more, no less"

		if not entry[1].isdigit():
			g.addRoad(entry[0], entry[1], entry[2]);

	allDist, allPre = g.allSourceDijkstra()

	placeNames = list(allDist.keys())
	placeNames.sort()
	print("Name List :",end="")
	for place in placeNames:
		print(" " + place, end="")
	print("")

	print("<From> <To> : To Quit enter dummy values")
	while True:
		try:
			start, end = input().split()
		except Exception:
			continue

		if start not in placeNames or end not in placeNames:
			print(start, "or", end, "not in known places, quitting")
			break

		print("From", start, "to", end, "=", allDist[start][end], "Km:", end="")
		traverse(allDist[start], allPre[start], start, end)
		print("")

except Exception as exp:
	print("Exception {0}".format(exp))
finally:
	inputFile.close()
