ALL_SRC_DJ = all-src-dj
GRAPH = graph

MH = mh
MH_MAP = mh-map
MH_DJ = mh-dj

.PHONY: clean $(MH_MAP) $(MH_DJ)

$(MH_DJ): $(ALL_SRC_DJ)
	./$(ALL_SRC_DJ) $(MH)

$(MH_MAP): in2dot.py $(MH).in
	./in2dot.py $(MH)
	neato -Tpdf -n1 $(MH).dot > $(MH).pdf
	evince $(MH).pdf

$(ALL_SRC_DJ): $(ALL_SRC_DJ).o $(GRAPH).o
	$(CXX) -o $@ $^

clean:
	rm -f $(ALL_SRC_DJ)
	rm -f *.o
	rm -f *~
	rm -f *.pdf
	rm -f *.dot
