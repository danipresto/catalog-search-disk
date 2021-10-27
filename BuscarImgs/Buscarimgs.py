import openpyxl; from openpyxl import load_workbook
import os
import glob
import fnmatch
import isoparser

#############
# Lê a planilha do excel, procura os diretórios da planilha e os .iso utilizando busca por padrão. 
# Dentro dos arquivos .iso busca por imagens. 
# Retorna uma array com todos os diretórios/imagens
############


#HD TESTETADO AMC_GYN HD 29 / HD 17
excel_file = 'Pasta de trabalho.xlsx' 
sheet = load_workbook(excel_file, data_only = True)

elements = sheet['Busca de Imagens']

paths = []; names = []; inames = []; images = [] 

for i in elements['E']: #Criando array com nomes das pastas
    val = str(i.value)
    inames.append(val)

for i in elements['H']: #Criando array com os diretórios dos arquivos segundo a planilha 
    val = str(i.value)
    paths.append(val)

for i in elements['B']: #Criando array com os nomes das imagens 
    val = str(i.value)
    images.append(val)

for elem in paths:
    filename = os.path.basename(elem) #Criando array com os nomes extraidos dos diretórios das planilhas
    names.append(filename)

print(inames)


def check_path(pat): #Recebe um diretório e checa a se ele existe
       if os.path.exists(pat):
           print('Existe')
           return True
       else:
           print('Não Existe') 
           return False


def searchHD(paths): #Recebe uma array com diretórios e checa todos. Retorna uma array com todos encontrados
    found = []    
    for i in paths:
        if check_path(i):
            found.append(i)
    return found


def searchALLHD(pattern, path): #Recebe um nome de arquivo e um diretório. Retorna uma array com todos os resultados que contém o nome 
    found = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                found.append(os.path.join(root, name))
    return found


def strong_search(): #Ainda em implementação. Retorna todos os valores com o padrão .jpg
    found = glob.glob('D\\*.jpg')
    return found


def searchfPattern(caminho, ina): #Faz o mesmo que searchALLHD mas sem utilizar o módulo fnmatch.
    check = []

    for imgs in ina:
        for root, dirs, files in os.walk(caminho):
            for name in files: 
                if imgs in name:
                    check.append(name)
    return check

 
def SearchISO(pathtosearch, imagesv): #Recebe um diretório de um arquivo .iso e uma array de nomes de imagens. Testa se as imagens estão no .iso e retorna uma tupla do par diretório/imagem
    iso = isoparser.parse(pathtosearch)
    isofiles = []
    Ifound = []
    for file in iso.record().children:
        isofiles.append(str(file.name))
    for imgs in imagesv:
        for elem in isofiles:
            if (imgs[:6] in elem) and (imgs not in Ifound):
                Ifound.append(imgs)
    return (pathtosearch, Ifound)     


def ImagesISO(filestotest, pathinHD, imagesvt): #Recebe um array com arquivos .iso, o diretório dos arquivos .iso e a array de imagens. Retorna uma array com os pares diretório/imagem 
    PairsIm = []
    for elem in filestotest:
        PairsIm.append(SearchISO(pathinHD+elem, imagesvt))
    return PairsIm    




#Busca usando Dados da Planilha

ImagPL = []

for cel in paths:
    if (check_path(cel)):
        ImagPL.append(cel)

print(ImagPL)

#Busca nos arquivos .iso

filesf = searchfPattern('D:/contratos/amc/iso', inames)
print(filesf)

#myfi = SearchISO("D:\\contratos\\amc\\iso\\AMC - FORTALEZA-REMESSA0874-17122014.iso", images)
Myresult = ImagesISO(filesf, "D:\\contratos\\amc\\iso\\", images)
print((Myresult))
for i in Myresult:
    print(i[1])
    if i[1] == []:
        Myresult.remove(i)
        
print(Myresult)
