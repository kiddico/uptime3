#!/usr/bin/python3
# Nick Chirico
# Oct 6, 2016

import datetime
import calendar
import sys

# Given the uptime in seconds, prints the date and time the system came up.
def origin(time):
	delta = datetime.timedelta(seconds=time)
	origin = str ( datetime.datetime.now() - delta )
	formatted = origin.replace(" ","-")
	formatted = formatted.replace(":","-")
	formatted = formatted.replace(":","-")
	formatted = formatted.split(".",1)[0]
	formatted = formatted.split("-")

	# Get month from provided number
	since = calendar.month_name[int(formatted[1])]
	# Everyhting date related
	since += " " + formatted[2].replace("0","") + " " + formatted[0] + " at "
	# everything time related
	since += formatted[3] + ":" + formatted[4] + "."

	print("Up since:", since)

def up(time):
	# Actual Calculations
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
