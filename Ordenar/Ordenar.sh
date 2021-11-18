#!/bin/bash


list=$(find $1 -mindepth 1 -maxdepth 1)
echo ${list[@]}


for c in ${list[@]};
do 
    readarray -d "/" -t name <<< "$c"
    readarray -d "." -t direct <<<  "${name[-1]}"
    mkdir C:\\Users\\isaacsousa\\Desktop\\testc\\HDs\\HD15\\"${direct[0]}"
    ./cat.exe C:\\Users\\isaacsousa\\Desktop\\testc\\HDs\\HD15\\"${direct[0]}"\\ "$c"

done
