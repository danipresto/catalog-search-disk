import openpyxl; from openpyxl import load_workbook
import os
import glob
import fnmatch
import isoparser

#HD TESTEADO AMC_GYN HD 29
excel_file = 'Pasta de trabalho.xlsx' 
sheet = load_workbook(excel_file, data_only = True)

elements = sheet['Busca de Imagens']

paths = []; names = []; inames = []; images = []

for i in elements['E']:
    val = str(i.value)
    inames.append(val)

for i in elements['H']:
    val = str(i.value)
    paths.append(val)

for i in elements['B']:
    val = str(i.value)
    images.append(val)

for elem in paths:
    filename = os.path.basename(elem)
    names.append(filename)

print(inames)

def check_path(pat):
       if os.path.exists(pat):
           print('Existe')
           return True
       else:
           print('Não Existe') 
           return False


def searchHD():
    found = []    
    for i in paths:
        if check_path(i):
            found.append(i)
    return found


def searchALLHD(pattern, path):
    found = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                found.append(os.path.join(root, name))
    return found
               
def strong_search():
    found = glob.glob('D\\*.jpg')
    return found



def searchfPattern(caminho, ina):
    check = []

    for imgs in ina:
        for root, dirs, files in os.walk(caminho):
            for name in files: 
                if imgs in name:
                    check.append(name)
    return check

 
def SearchISO(pathtosearch, imagesv):
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



def ImagesISO(filestotest, pathinHD, imagesvt):
    PairsIm = []
    for elem in filestotest:
        PairsIm.append(SearchISO(pathinHD+elem, imagesvt))
    return PairsIm    


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