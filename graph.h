#include <map>
#include <vector>

using namespace std;

class Graph {
	public:
		Graph();
		void addRoad(unsigned int index1, unsigned int index2, unsigned int dist);
		void display();
		void djikstra(unsigned int start, unsigned int dist[], int pre[]);
	private:
		unsigned int nodeCount;
		typedef map<unsigned int, unsigned int> AdjacencyList;
		vector<AdjacencyList> alv;
};
