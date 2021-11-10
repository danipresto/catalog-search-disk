/*AINDA EM IMPLEMENTAÇÃO*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h> //Biblioteca de diretórios 
#include <iostream>
#include <chrono>   //Biblioteca de medições de tempo
#include <fstream>  //Biblioteca de leitura e escrita de arquivos


auto start = std::chrono::high_resolution_clock::now(); //Inicia a contagem
/* Função p/ listar diretórios. 
Recebe o nome do diretório, um inteiro para escrever a ordem no csv 
e o objeto arquivo */

static int find_direct(const char* dirname, std::ofstream* myfile) 
{
    DIR* dir; 
    char buffer[PATH_MAX + 2]; //Array com tamanho máximo de subdiretórios a pesquisar
    char* p = buffer; //Ponteiro na posição inicial da array
    const char* src; 
    char* end = &buffer[PATH_MAX];
    int ok;


    src = dirname;
    while (p < end && *src != '\0') { //Enquanto o ponteiro p não estiver na última posição incrementar o valor de p; 
        *p++ = *src++;
    }
    *p = '\0';

    dir = opendir(dirname); //Abri o diretório e armazena em objeto do tipo DIR
    if (dir != NULL) {
        struct dirent* ent;

        while ((ent = readdir(dir)) != NULL) { //Enquanto houver subdiretórios em dir
            char* q = p;
            char c;

            if (buffer < q) {
                c = q[-1];
            }
            else {
                c = ':';
            }

         
            if (c != ':' && c != '/' && c != '\\') {
                *q++ = '/';
            }

           
            src = ent->d_name;
            while (q < end && *src != '\0') {
                *q++ = *src++;
            }
            *q = '\0';

            switch (ent->d_type) {
            case DT_LNK:
            case DT_REG:
                
               
                *myfile << buffer << "\n";

                break;

            case DT_DIR:
               
                if (strcmp(ent->d_name, ".") != 0
                    && strcmp(ent->d_name, "..") != 0) {
                    find_direct(buffer, myfile);
                }
                break;

            default:;
            }

        }

        closedir(dir);
        ok = 1;

    }
    else {
       
        printf("Cannot open directory %s\n", dirname);
        ok = 0;
    }

    return ok;
}


int main(int argc, char* argv[])
{
    bool CurrentDt = true; //usar comando de linha ou a variável directory como inicio. false usa a variável.
    int i;
    int ok;
    const char* directory = "D:\\";
    std::ofstream catalog;
    catalog.open("C:\\Users\\isaacsousa\\Desktop\\Isaac\\catalog.csv"); //diretório para criação do .csv

    i = 1;
    if (CurrentDt) {
        while (i < argc) {
            ok = find_direct(argv[i], &catalog);
         
            if (!ok) {
                exit(EXIT_FAILURE);
            }
            i++;
        }

        if (argc == 1) {
            find_direct(".", &catalog);
        }
    }
    else {
        find_direct(directory, &catalog);
    }

    catalog.close();
    auto stop = std::chrono::high_resolution_clock::now(); //Para de contar o tempo
    auto duration = std::chrono::duration_cast<std::chrono::seconds>(stop - start);
    std::cout << "Tempo gasto : " << duration.count() << "Segundos" << std::endl; 
    return 0;
}


/* Uso: g++ Local\\Catalog.cpp -o nome.exe
   nome.exe diretório a buscar */
