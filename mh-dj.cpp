#include <iostream>
#include "graph.h"
#include <fstream>
#include <string>
#include <sstream>
#include <assert.h>
#include <stdlib.h>
#include <limits.h>

void split(const string& entry, vector<string>& entries) {
	istringstream iss(entry);
	string word;
	while (iss >> word)
		entries.push_back(word);
}

void traverse(unsigned int dist[], int pre[], int start, int curr, const vector<string>& indexToNameMap) {
	if (pre[curr] != -1) traverse(dist, pre, start, pre[curr], indexToNameMap);
	cout << indexToNameMap[curr] << "(" << dist[curr] << ") ";
}

int main(int argc, char* argv[]) {

	Graph g;
	map<string, unsigned int> nameToIndexMap;
	vector<string> indexToNameMap;

	ifstream fin;
	fin.open("mh-dj.in");

	string entry;

	while (getline(fin, entry) && !fin.eof()) {

		if ('#' == entry[0])
			continue;

		vector<string> entries;
		split(entry, entries);

		if ( 0 == entries.size() )
			continue;

		assert( 3 == entries.size() );

		if (!isdigit(entries[1][0])) {

			string& place1 = entries[0];
			string& place2 = entries[1];
			unsigned int dist = atoi(entries[2].c_str());

			map<string, unsigned int>::iterator it1 = nameToIndexMap.find(place1);
			unsigned int index1;
			if ( it1 == nameToIndexMap.end() ) {
				index1 = nameToIndexMap.size();
				nameToIndexMap[place1] = index1;

				indexToNameMap.push_back(place1);
				assert(indexToNameMap[index1] == place1);

			} else index1 = it1->second;

			map<string, unsigned int>::iterator it2 = nameToIndexMap.find(place2);
			unsigned int index2;
			if ( it2 == nameToIndexMap.end() ) {
				index2 = nameToIndexMap.size();
				nameToIndexMap[place2] = index2;

				indexToNameMap.push_back(place2);
				assert(indexToNameMap[index2] == place2);

			} else index2 = it2->second;

			g.addRoad(index1, index2, dist);
		}
	}

	//	g.display();

	unsigned int nodeCount = nameToIndexMap.size();

	unsigned int allDist[nodeCount][nodeCount];
	int allPre[nodeCount][nodeCount];

	for (unsigned int i = 0; i < nodeCount; i++) {
		for (unsigned int k = 0; k < nodeCount; k++) {
			allDist[i][k] = UINT_MAX;
			allPre[i][k] = -1;
		}
	}

	for (unsigned int i = 0; i < nodeCount; i++) {
		g.djikstra(i, allDist[i], allPre[i]);
	}

	cout << "Name List : ";
	for (
		map<string, unsigned int>::iterator it = nameToIndexMap.begin();
		it != nameToIndexMap.end();
		it++
	    ) {
		cout << it->first << " ";
	}
	cout << endl;

	cout << "<From> <To> : To End enter dummy values" << endl;

	while (true) {
		string from, to; cin >> from; cin >> to;

		map<string, unsigned int>::iterator itFrom = nameToIndexMap.find(from);
		if (itFrom == nameToIndexMap.end()) break;
		unsigned int fromIndex = itFrom->second;

		map<string, unsigned int>::iterator itTo = nameToIndexMap.find(to);
		if (itTo == nameToIndexMap.end()) break;
		unsigned int toIndex = itTo->second;

		cout << "From " << from << " to " << to << " = " << allDist[fromIndex][toIndex] << "Km : ";
		traverse(allDist[fromIndex], allPre[fromIndex], fromIndex, toIndex, indexToNameMap);
		cout << endl;
	}

	return 0;
}
