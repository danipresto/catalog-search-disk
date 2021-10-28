#!/bin/bash

if [ "$2" == "img" ] 
then 
    find $1 -iname "*.jpg" -type f -printf '%p,\n'  >> $3_catalogo_img.csv
fi    

if [ "$2" == "all" ] 
then 
    find $1 -type f -printf '%p,\n' >> $3_catalogo_all.csv
fi    

#para executar coloque "endereço de varredura" + "img "(para buscar apenas imagens ou "all" (para varrer tudo)
