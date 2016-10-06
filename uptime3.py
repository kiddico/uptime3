#!/usr/bin/python3
# Nick Chirico
# Oct 6, 2016

# next up is to add an option to see when the machine was turned on.
# just for fun
import time

## read up to the first period of /proc/uptime
f = open('/proc/uptime', 'r')
time = int ( f.read().split ('.',1) [0] )

# Actual calculations - > I decided to do it from the bottom up this time around
## Minutes
minutes = int ( ( time / 60 ) % 60)
overflow = int ( ( time / 60 ) - ( minutes ) )

## Hours
hours = int ( ( overflow / 60 ) % 24 )
overflow = int ( ( overflow / 60 ) - ( hours ) )

## Days
days = int ( ( overflow / 24) % 24 )
overflow = int ( ( overflow / 24 ) - ( days ) )

## Weeks
weeks = int ( (overflow / 7 ) % 7 )


# This will be printed later. Concat on relevant info
output = "Uptime: "

if weeks >= 1:
	output = output + str ( int ( weeks ) ) + " weeks, "

if days >= 1:
	output = output + str ( int ( days ) ) + " days, "

if hours >= 1:
	output = output + str ( int ( hours ) ) + " hours, "

if minutes >= 1:
	output = output + str ( int ( minutes ) ) + " minutes."
# Let's be proper now. In case this is done on the hour mark.
else:
	output += "."

print(output)
