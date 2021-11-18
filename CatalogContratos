#!/bin/bash

#colocar o codigo do disco (c ,d , e , etc...)
list=$(find /$1/contratos -mindepth 2 -maxdepth 2 -type d)
echo ${list[@]}
#Laço para criar um csv para cada pasta dentro de contratos
for c in ${list[@]};
do
     readarray -d "/" -t name <<<"$c" 

     if [ ! -d "${name[-2]}" ]
      then 
          mkdir "${name[-2]}";

     fi
     echo ${name[*]};
     find $c -type f -printf '%p,\n' >> "${name[-2]}/${name[-1]}".csv

done
