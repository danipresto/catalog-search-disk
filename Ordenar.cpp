#include <fstream>
#include <iostream>
#include <vector>
#include "include/dirent.h"
#include <sstream>
#include <set>

//Lê um .csv e separa o conteúdo em pastas

void writetp(const char* name, std::string lin, std::string path)
{
	std::string nam = name;
	if (lin.find(nam) != std::string::npos)
	{
		std::string fname = path + nam;
		std::string pat = path + nam + "\\" + nam + ".csv";
		std::string file = fname + "\\" + nam + ".csv";
		mkdir(fname.c_str());
		std::ofstream mycont(pat.c_str(), std::ios_base::app);
		mycont << lin << "\n";
	}
}


int main(int arg, char* argv[]) 
{	
	//std::cout << arg << "\n";
	std::string path = argv[1]; //DIRETORIO PARA SALVAR OS ARQUIVOS
	std::ifstream catalog(argv[2]); //LOCAL DO ARQUIVO .CSV
	std::set<std::string> direct;  std::vector<std::string> content;
	std::fstream logs; std::string line; std::string part;

	
	
	while (std::getline(catalog, line))
		{	
        	std::stringstream nline(line);
			int i = 0;
          	while(std::getline(nline, part, '/'))
			{	 
  			 	content.push_back(part);
				if (i == 4){
					break;
				}
				i++;
			}
	
        
			

			if(line.find("contratos") != std::string::npos)
			{	
                writetp(content[4].c_str(), line, path);
            } 
			else 
			{
				std::cout << "Não é Parte de contratos/" << std::endl;
			}

			content.clear();
		}
    }


