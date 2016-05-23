MH_DJ = mh-dj
GRAPH = graph

all: clean $(MH_DJ)
	./$(MH_DJ)

$(MH_DJ): $(MH_DJ).o $(GRAPH).o
	$(CXX) -o $@ $^

clean:
	rm -f $(MH_DJ)
	rm -f *.o
	rm -f *~
