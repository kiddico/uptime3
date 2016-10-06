#!/usr/bin/python3
# Nick Chirico
# Oct 6, 2016

import time

# First up is to get the uptime in seconds from the system file
f = open('/proc/uptime', 'r')
time = f.read()



# Remove unused value, everything after the '.', then finaly make it an int
time = int(time.split(' ', 1)[0].split('.',1)[0])



# Minutes
minutes = int ( ( time / 60 ) % 60)
overflow = int ( ( time / 60 ) - ( minutes ) )

# hours
hours = int ( ( overflow / 60 ) % 24 )
overflow = int ( ( overflow / 60 ) - ( hours ) )

# days
days = int ( ( overflow / 24) % 24 )
overflow = int ( ( overflow / 24 ) - ( days ) )

# weeks
weeks = int ( (overflow / 7 ) % 7 )



output = "Uptime: "

if weeks >= 1:
	output = output + str ( int ( weeks ) ) + " weeks, "

if days >= 1:
	output = output + str ( int ( days ) ) + " days, "

if hours >= 1:
	output = output + str ( int ( hours ) ) + " hours, "

if minutes >= 1:
	output = output + str ( int ( minutes ) ) + " minutes."
else:
	output += "."

print(output)
