#!/usr/bin/python3
# Nick Chirico
# Oct 19, 2016

import sys
from uptime3 import up, origin

def main():
	# read up to the first period of /proc/uptime
	f = open('/proc/uptime', 'r')
	time = int ( f.read().split('.',1)[0] )

	# So I have no idea how to properly implement flags.
	# The plan is 0 = default, 1 = orgin, 2 = both.
	to_print = 0
	if (len(sys.argv) > 1 ):
		for arg in sys.argv:
			if arg == "-o" or arg == "--origin":
				if( to_print != 2):
					to_print=1
			if  arg == "-a" or arg == "--all":
				to_print=2

	if ( to_print == 0 ):
		up(time)
	if ( to_print == 1 ):
		origin(time)
	if ( to_print == 2 ):
		up(time)
		origin(time)



if __name__ == "__main__":
	main()
