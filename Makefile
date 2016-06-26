ALL_SRC_DJ = all-src-dj
GRAPH = graph

MH = mh
MH_MAP = mh-map
MH_DJ = mh-dj

IR = ir
IR_MAP = ir-map

.PHONY: clean $(MH_MAP) $(MH_DJ) $(IR_MAP)

$(MH_DJ): $(ALL_SRC_DJ)
	./$(ALL_SRC_DJ) $(MH)

$(MH_MAP): $(MH).pdf
	evince $(MH).pdf

$(IR_MAP): $(IR).pdf
	evince $(IR).pdf

$(ALL_SRC_DJ): $(ALL_SRC_DJ).o $(GRAPH).o
	$(CXX) -o $@ $^

%.dot : in2dot.py %.in
	./in2dot.py $*

%.pdf : %.dot
	neato -Tpdf -n1 $^ > $@

clean:
	rm -f $(ALL_SRC_DJ)
	rm -f *.o
	rm -f *~
	rm -f *.pdf
	rm -f *.dot
