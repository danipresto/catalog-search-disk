import os, pandas as pd, sys

# Inicialização de variáveis/estruturas de dados

root = sys.argv[1]
listPath = []
listFile = []

# Percorrendo a arvore de diretórios com os.walk ,e salvando os nomes dos arquivos e nome dos caminhos em listas separadas

for path, subdirs, files in os.walk(root):
    for name in files:
        if(name.endswith('.jpg')):
            listPath.append(path)
            listFile.append(name)


# Convertendo listas para formato de dataframe

dfListsP = pd.DataFrame(listPath)
dfListsF = pd.DataFrame(listFile)


#Concatenando os df e passando para formato csv em arquivo .txt

dfMerge = pd.concat([dfListsP,dfListsF],axis=1)
dfMerge = dfMerge.set_axis(['Caminho','Nome'],axis='columns')
dfMerge['HD'] = sys.argv[2]
cols = dfMerge.columns.tolist()
cols = cols[-1:] + cols[:-1]
dfMerge = dfMerge[cols]
dfMerge.to_csv(path_or_buf = os.getcwd() + "\\planilha.txt",sep = ',')
