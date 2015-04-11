#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
//welcome to inline defenition hell

class writef {
	public:
		//constructor assigns filename and opens/assigns stream
		writef(std::string file){
			orig=file;
			streams.insert(std::make_pair(file,new std::fstream(file.c_str(),std::fstream::out)));
		}
		
		~writef(){
			std::map<std::string, std::fstream*>::iterator iter;
			for(iter=streams.begin();iter!=streams.end();++iter){
				iter->second->close();
				delete iter->second;
			}
		}
		template <typename T>
		void write(T object){
			*streams[orig]<<object;
		};
		//streams.insert(std::makepair("file",stream pointer))
		template <typename T>
		void write(T object,std::string newfile){
			std::ofstream temp;
			auto search=streams.find(newfile);
			if(search==streams.end()){//in other words: if(it isn't already there)
				streams.insert(std::make_pair(newfile,new std::fstream(newfile.c_str(),std::fstream::out)));
				search = streams.find(newfile);
				*(search->second)<<object;
			}
			else{
				*(search->second)<<object;
			}
		};
	private:
		std::string orig;
		std::map<std::string,std::fstream*> streams;
		std::fstream* strm;
};

class readf{
	public:
		readf(std::string file){
			orig=file;
			streams.insert(std::make_pair(file,new std::fstream(file.c_str(),std::fstream::in)));
		}
		
		~readf(){
			std::map<std::string, std::fstream*>::iterator iter;
			for(iter=streams.begin();iter!=streams.end();++iter){
				iter->second->close();
				delete iter->second;
			}
		}
		void look(){
			std::map<std::string, std::fstream*>::iterator iter;
			for(iter=streams.begin();iter!=streams.end();++iter)
				std::cout<<iter->first;
		}	
		std::string read(std::string newfile){
			std::string temp;
			auto search = streams.find(newfile);
			if(search==streams.end()){//in other words: if(it isn't already there)
				//makes a new pair. the name of the file the stream goes to, and a stream with the appropriate stream pointer
				streams.insert(std::make_pair(newfile,new std::fstream(newfile.c_str(),std::fstream::in)));
				search = streams.find(newfile);
				*(search->second)>>temp;
				//std::cout<<search->second<<std::endl;
				return temp;
				//need to close this later in the destructor
			}
			else{
				*(search->second)>>temp;
				return temp;
			}
		}

		std::string read(){
			std::string temp;
			*(streams[orig])>>temp;
			return temp;
		}

	private:
		std::string orig;
		std::fstream* strm;
		std::map<std::string,std::fstream*> streams;
};
