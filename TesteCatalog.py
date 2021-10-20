import os,pandas as pd, numpy as np


root = os.getcwd()
path = os.path.join(root, "targetdirectory")
listPath = []
listFile = []


for path, subdirs, files in os.walk(root):
    for name in files:
        listPath.append(path)
        listFile.append(name)


dfListsP = pd.DataFrame(listPath)
dfListsF = pd.DataFrame(listFile)

dfMerge = pd.concat([dfListsP,dfListsF],axis=1)
df_Merge = df_Merge.set_axis(['Caminho','Nome'],axis='columns')
df_Merge.to_csv(path_or_buf = os.getcwd() + "\\planilha.txt",sep = ',')
