#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
#include <string>


int main(int argc, char* argv[])
{

    std::vector<std::string> Encontrado; std::ofstream Encont;
    Encont.open("resultado.txt"); //Cria um .txt para armazenar os resultados 
    std::string contrato = argv[1]; std::string arquivo = argv[2]; //Recebe os argumentos 
    std::string path = "F:\\Users\\isaacsousa\\Desktop\\testc\\HDs"; //caminho dos catálogos
    std::ifstream catalogo; std::string lin;

    for (auto const& file : std::filesystem::recursive_directory_iterator(path)) //acessa todas as pastas no diretório
    {
       
        if (file.path().string().find(contrato) != std::string::npos && file.path().string().find("videos") == std::string::npos) //acessa somente as pastas do contrato, não acessa a subpasta videos
        {   
            std::cout << file.path().string() << std::endl;
            catalogo.open(file.path().string().c_str());//abre o .csv
            unsigned int cl = 0; //contar as linhas 
            while (std::getline(catalogo, lin))
            {
                std::getline(catalogo, lin);
                cl++;
                
                    if ((file.path().string().find(contrato) != std::string::npos)) //checar se essa condição é necessária 
                    {
                        if (argc == 4) //usar 3 argumentos na busca
                        {
                            if (lin.find(arquivo) != std::string::npos && lin.find(argv[3]) != std::string::npos) //se encontrar a entrada do usuário na linha 
                            {
                                Encontrado.push_back(lin);
                                Encont << file.path().string() << "  ";
                                Encont << lin << "\n";
                                std::cout << "Encontrado" << std::endl;
                                std::cout << lin << std::endl;
                                std::cout << file.path().string() << std::endl;
                                std::cout << "Linha: " << cl << std::endl;
                            }
                        }
                        else {
                            //usar 2 argumentos na busca
                            if (lin.find(arquivo) != std::string::npos)
                            {
                                Encontrado.push_back(lin);
                                Encont << file.path().string() << "  ";
                                Encont << lin << "\n";
                                std::cout << "Encontrado" << std::endl;
                                std::cout << lin << std::endl;
                                std::cout << file.path().string() << std::endl;
                                std::cout << "Linha: " << cl << std::endl;
                            }
                        }
                }
            }
            catalogo.close();
        }
    }
}

/* g++ Search.cpp -o Search.exe
   Search.exe contrato arquivo*/
