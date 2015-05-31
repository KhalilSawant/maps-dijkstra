class Graph:

	def __init__(self):
		self.adjList = {}

	def addRoad(self, place1, place2, distance):
		if place1 not in self.adjList.keys():
			self.adjList[place1] = {}
		if place2 not in self.adjList.keys():
			self.adjList[place2] = {}

		assert place2 not in self.adjList[place1].keys(), "Duplicate Entry between {0} and {1}".format(place1, place2)
		assert place1 not in self.adjList[place2].keys(), "Duplicate Entry between {0} and {1}".format(place2, place1)

		self.adjList[place1][place2] = int(distance)
		self.adjList[place2][place1] = int(distance)

	def display(self):
		for source in self.adjList.keys():
			print(source, "-->", self.adjList[source]);

	def allSourceDijkstra(self):

		allDist = {}
		allPre = {}

		for source in self.adjList.keys():
			dist, pre = self.dijkstra(source)
			allDist[source] = dist
			allPre[source] = pre

		return allDist, allPre

	def dijkstra(self, source):
		dist = {}
		pre = {}
		unvisited = set()

		for dest in self.adjList.keys():
			unvisited.add(dest)
			dist[dest] = 999999

		dist[source] = 0

		while not 0 == len(unvisited):

			minDist = 999999

			for dest in unvisited:
				if dist[dest] < minDist:
					toBeVisited = dest
					minDist = dist[dest]

			unvisited.remove(toBeVisited)
			curr = toBeVisited

			for dest in self.adjList[curr].keys():
				if dist[dest] > minDist + self.adjList[curr][dest]:
					dist[dest] = minDist + self.adjList[curr][dest]
					pre[dest] = curr

		return dist, pre
