import openpyxl; from openpyxl import load_workbook
import os.path; from os import path
import glob
import fnmatch

#HD TESTEADO AMC_GYN HD 29
excel_file = 'Pasta de trabalho.xlsx' 
planilha = load_workbook(excel_file, data_only = True)

elementos = planilha['Busca de Imagens']

paths = []; names = []; inames = []; imagens = []

for i in elementos['E']:
    val = str(i.value)
    inames.append(val)

for i in elementos['H']:
    val = str(i.value)
    paths.append(val)

for i in elementos['B']:
    val = str(i.value)
    imagens.append(val)

for elem in paths:
    filename = os.path.basename(elem)
    names.append(filename)

print(inames)

def find(pat):
       if path.exists(pat):
           print('Existe')
           return True
       else:
           print('Não Existe') 
           return False


def buscaHD():
    achados = []    
    for i in paths:
        if find(i):
            achados.append(i)
    return achados


def buscartudoHD(pattern, path):
    achados = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                achados.append(os.path.join(root, name))
    return achados
               
def buscaforc():
    achados = glob.glob('D\\*.jpg')
    return achados



def listar(caminho, ina):
    checar = []

    for imgs in ina:
        for root, dirs, files in os.walk(caminho):
            for name in files: 
                if imgs in name:
                    checar.append(name)
    return checar


arquivos = listar('D:/contratos/amc/iso', inames)
print(arquivos)




#print(imagens)
imagens_enc = []
for iso, j in zip(arquivos, imagens):
    print('D:/contratos/amc/iso/'+iso+'/'+j+'.jpg')
    if find(iso+j+'.jpg'):
        imagens_enc.append(iso+j+'.jpg')


#resultado = buscaHD()
#print(resultado, len(resultado))

#if len(resultado) == 0:
    #resultado = buscaforc()

#print(resultado)


#print(resultado)