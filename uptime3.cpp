#include <stdio.h>
#include "strd.hpp"
int main(){
	//getting time from the uptime file in unix
	readf uptimefile("/proc/uptime");
	int time = std::stoi(uptimefile.read());
	
	int weeks   = time    / (7*24*60*60);
	int days    = time    / (24*60*60)   - 7*weeks;
	int hours   = time    / (60*60)      - 7*24*weeks    -24*days;
	int minutes = time    / (60)         - 7*24*60*weeks -24*60*days - 60*hours; 	 

	std::string uptime = "Up Time: ";
	
	if(weeks !=0)
		if(weeks==1)
			uptime += std::to_string(weeks) + " week, ";
		else
			uptime += std::to_string(weeks) + " weeks, ";
	
	if(days !=0)
		if(days==1)
			uptime += std::to_string(days)  + " day, ";
		else
			uptime += std::to_string(days)  + " days, ";
				
	if(hours !=0)
		if(hours==1)
			uptime += std::to_string(hours) + " hour, ";
		else
			uptime += std::to_string(hours) + " hours, ";

	if(minutes !=0)
		if(minutes==1)
			uptime += std::to_string(minutes) + " minute.";
		else
			uptime += std::to_string(minutes) + " minutes.";

	
	std::cout<<uptime<<std::endl;
}
