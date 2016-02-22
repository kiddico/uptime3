uptime3:
	g++ --std=c++11 -o uptime3 uptime3.cpp

install: uptime3
	cp uptime3 /usr/local/bin

clean:
	rm -f *~
	rm -f .*~
