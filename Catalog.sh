#!/bin/bash

find /d  -iname "*.jpg" | paste -sd ',\n' >> catalogo.csv
