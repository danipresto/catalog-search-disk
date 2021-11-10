#include <fstream>
#include <iostream>
#include <vector>
#include "include/dirent.h"
#include <thread> 



/* Lê um .csv já e separa ele em novos por contrato em novos arquivos .csv */
 
void writetp(const char* name, std::string lin, std::string path)
{
	std::string nam = name;
	if (lin.find(nam) != std::string::npos)
	{
		std::string pat = path + nam + "\\" + nam + ".csv";
		std::ofstream mycont(pat.c_str(), std::ios_base::app);
		mycont << lin << "\n";
	}
}


int main(int arg, char* argv[]) 
{	
	//std::cout << arg << "\n";
	std::string path = argv[1]; //DIRETORIO PARA SALVAR OS ARQUIVOS
	std::ifstream catalog(argv[2]); //LOCAL DO ARQUIVO .CSV
	std::vector<std::string> Contracts = {"amc", "detran", "goiania", "goiania-corredor", "maracanau"}; //Falta Adicionar todos os contratos
	std::fstream logs; std::string line;

	
	for (std::string elem : Contracts) {
		std::string fname = path + elem;
		std::string file = fname + "\\" + elem + ".csv";
		mkdir(fname.c_str());
		std::fopen(file.c_str(), "w");
	}	

	while (std::getline(catalog, line))
		{	
			if(line.find("contratos") != std::string::npos)
			{	
				writetp("detran", line, path); 
				writetp("amc", line, path); 
				writetp("goiania", line, path); 
				writetp("goiania-corredor", line, path); 
				writetp("maracanau", line, path);

			}
			else 
			{
				std::cout << "Não é Parte de contratos/" << std::endl;
			}
		}
}


