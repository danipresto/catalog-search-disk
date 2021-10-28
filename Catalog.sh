#!/bin/bash



if [ "$2" == "img" ] 
then 
    #funçao find para listar arquivos, -iname para filtrar , printf para modificar a saida pra padrao csv
    find $1 -iname "*.jpg" -type f -printf '%p,\n'  >> $3_catalogo_img.csv
fi    

if [ "$2" == "all" ] 
then 
    find $1 -type f -printf '%p,\n' >> $3_catalogo_all.csv
fi    

#para executar :
# bash Catalog.sh "endereço de varredura" + "img "(para buscar apenas imagens ou "all" (para varrer tudo) + nome do .csv
