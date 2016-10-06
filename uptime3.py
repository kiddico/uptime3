#!/usr/bin/python3
# Nick Chirico
# Oct 6, 2016

# next up is to add an option to see when the machine was turned on.
# just for fun
import datetime
import calendar
import sys

# Given the uptime in seconds, prints the date and time the system came up.
def sincewhen(time):
	delta = datetime.timedelta(seconds=time)
	origin = str ( datetime.datetime.now() - delta )
	fo = origin.replace(" ","-")
	fo = fo.replace(":","-")
	fo = fo.replace(":","-")
	fo = fo.split(".",1)[0]
	fo = fo.split("-")

	# Get month from provided number
	since = calendar.month_name[int(fo[1])]
	# Everyhting date related
	since += " " + fo[2].replace("0","") + " " + fo[0] + " at "
	# everything time related
	since += fo[3] + ":" + fo[4] + "."

	print("Up since: ", since)
	return



def main():
	## read up to the first period of /proc/uptime
	f = open('/proc/uptime', 'r')
	time = int ( f.read().split('.',1)[0] )

	# Actual calculations - > I decided to do it from the bottom up this time around
	## Minutes
	minutes = int (( time/60 ) % 60 )
	overflow = int (( time/60 ) - ( minutes ))

	## Hours
	hours = int (( overflow/60 ) % 24 )
	overflow = int (( overflow/60 ) - ( hours ))

	## Days
	days = int (( overflow/24 ) % 24 )
	overflow = int (( overflow/24 ) - ( days ))

	## Weeks
	weeks = int (( overflow/7 ) % 7 )


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

	if (len(sys.argv) > 1 ):
		for arg in sys.argv:
			if arg == "-o" or arg == "--origin":
				sincewhen(time)



if __name__ == "__main__":
	main()
