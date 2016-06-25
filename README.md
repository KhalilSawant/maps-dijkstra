# maps-dijkstra
Graph like rendering of Map, and Dijkstra's Algorithm

<map-name>.in is the input file which contains two types of entries

1. Town-names with the latitude and longitude

2. Two town-names with the intervening distance

in2dot.py converts this input file into .dot file, which can be used to be rendered as a graph using GraphViz

all-src-dj.py or all-src-dj runs all-source Dijkstra Algorith on the input file, with graph.py and graph.cpp respectively modeling the graph


# Commandsa

In Makefile

./in2dot.py <map-name>
neato -Tpdf -n1 <map-name>.dot > <map-name>.pdf
neato -Tps -n1 <map-name>.dot > <map-name>.ps

all-src-dj.py/all-src-dj <map-name>
