#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "include/dirent.h"
#include <iostream>
#include <chrono>

auto start = std::chrono::high_resolution_clock::now();

static int find_direct(const char* dirname)
{
    DIR* dir;
    char buffer[PATH_MAX + 2];
    char* p = buffer;
    const char* src;
    char* end = &buffer[PATH_MAX];
    int ok;

    src = dirname;
    while (p < end && *src != '\0') {
        *p++ = *src++;
    }
    *p = '\0';

    dir = opendir(dirname);
    if (dir != NULL) {
        struct dirent* ent;

        while ((ent = readdir(dir)) != NULL) {
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
                /* Output file name with directory */
                printf("%s\n", buffer);
                break;

            case DT_DIR:
               
                if (strcmp(ent->d_name, ".") != 0
                    && strcmp(ent->d_name, "..") != 0) {
                    find_direct(buffer);
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
    bool CurrentDt = false;
    int i;
    int ok;
    const char* directory = "D:\\";


    i = 1;
    if (CurrentDt) {
        while (i < argc) {
            ok = find_direct(argv[i]);
         
            if (!ok) {
                exit(EXIT_FAILURE);
            }
            i++;
        }

        if (argc == 1) {
            find_direct(".");
        }
    }
    else {
        find_direct(directory);
    }

    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
    duration = duration / 1000000;
    std::cout << "Tempo gasto : " << duration.count() << "Segundos" << std::endl;
    return EXIT_SUCCESS;
}

