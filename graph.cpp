#include "graph.h"
#include <iostream>
#include <assert.h>
#include <limits.h>
#include <set>

Graph::Graph() { nodeCount = 0; }

void Graph::addRoad(unsigned int index1, unsigned int index2, unsigned int dist) {

	assert(index1 <= nodeCount);
	if (index1 == nodeCount)  {
		nodeCount++;
		AdjacencyList obj;
		alv.push_back(obj);
	}
	assert(index2 <= nodeCount);
	if (index2 == nodeCount)  {
		nodeCount++;
		AdjacencyList obj;
		alv.push_back(obj);
	}

	if ( alv[index1].find(index2) != alv[index1].end() ) {
		cout << "Duplicate " << index1 << " " << index2 << endl;
		assert(0);
	}
	alv[index1][index2] = dist;

	if ( alv[index2].find(index1) != alv[index2].end() ) {
		cout << "Duplicate " << index1 << " " << index2 << endl;
		assert(0);
	}
	alv[index2][index1] = dist;
}

void Graph::display() {
	for (unsigned int i = 0; i < nodeCount; i++) {
		cout << "From " << i << endl;
		for (
			AdjacencyList::iterator alIt = alv[i].begin();
			alIt != alv[i].end();
			alIt++
		    ) {
			cout << "\t" << alIt->first << " : ";
			cout << alIt->second << endl;
		}
	}
}

void Graph::djikstra(unsigned int start, unsigned int dist[], int pre[]) {

	assert(start >= 0 && start < nodeCount);
	dist[start] = 0;

	set<unsigned int> unVisited;
	for (unsigned int i = 0; i < nodeCount; i++) unVisited.insert(i);

	while (!unVisited.empty()) {

		int minDist = UINT_MAX;
		unsigned int toBeVisited;

		for (
			set<unsigned int>::iterator suiIt = unVisited.begin();
			suiIt != unVisited.end();
			suiIt++
		    ) {
			if (dist[*suiIt] < minDist) {
				toBeVisited = *suiIt;
				minDist = dist[*suiIt];
			}
		}

		unVisited.erase(toBeVisited);

		for (
			AdjacencyList::iterator alIt = alv[toBeVisited].begin();
			alIt != alv[toBeVisited].end();
			alIt++
		    ) {
			// Relax procedure
			if (dist[alIt->first] > dist[toBeVisited] + alIt->second) {
				dist[alIt->first] = dist[toBeVisited] + alIt->second;
				pre[alIt->first] = toBeVisited;
			}
		}
	}
}
