#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <string>
#include <iostream>
#include <filesystem>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <assert.h>

int main(int argc, char* argv[])
{
   
    std::filesystem::path::preferred_separator;
    std::string file = argv[2]; // diretório da pasta de armazenamento
    std::string path = argv[1]; // Local dos arquivos de HDs
    std::string line;
    std::vector<std::string> paths;
    const char* pch;
    for (const auto& entry : std::filesystem::recursive_directory_iterator(path)) {
        paths = {};
        char* cstr = new char[entry.path().string().length() + 1];
        strcpy(cstr, entry.path().string().c_str());
        pch = strtok(cstr, "/ \\");
        while (pch != NULL)
        {
            paths.push_back(pch);
            pch = strtok(NULL, "/ \\");

        }
        if (paths.size() >= 4) {
            if (!std::filesystem::exists(file + "/" + paths[2])) {
                std::filesystem::create_directory(file + "/" + paths[2]);
            }

            if (!std::filesystem::exists(file + "/" + paths[2] + "/" + paths[3])) {
                std::filesystem::create_directory(file + "/" + paths[2] + "/" + paths[3]);
            }

            std::string nwf = file + "/" + paths[2] + "/" + paths[3] + "/" + paths[3] + ".csv";
            std::ofstream catalog(nwf.c_str(), std::ios_base::app);
            
            catalog << entry.path().string() << '\n';
        }
    }
}

/* Compilar usando: g++ Catalog.cpp -std=c++17 -o Catalog.exe
   Executar usando: .\Catalog.exe LocaldoCatalogo Localdo.csv */
