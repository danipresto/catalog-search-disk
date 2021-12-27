import datetime
import subprocess, sys
import pandas as pd
import numpy as np
import shutil
import matplotlib.pyplot as plt
import time
import os

def calculate_size(path):

    while True: #Para evitar erros de leitura 

        try:
            print(f"ETAPA {path}")
            p = subprocess.Popen(["powershell.exe",  #Executa o robocopy
                "C:/Users/daniel/Desktop/HDsize/size.ps1", path], 
                stdout=sys.stdout)
                
            p.communicate()

            data = pd.read_csv("sizes.txt", encoding='cp1252', error_bad_lines=False) #codificação da saída do LOG

        
            x = np.array(data)

            timepass = x[4][0].split()   
            timepass = timepass[3]

            pastas = x[1][0].split()
            pastas = pastas[1]


            direct = x[2][0].split()
            direct = direct[1]

            Bytes = x[3][0].split()
            Bytes = round(float(Bytes[1])/1024**3, 3)

            print(Bytes, direct, pastas, timepass) 
            sucess = True
        
        except pd.errors.ParserError:
            continue
        
        break

    return Bytes, direct, pastas, timepass



BytesCon = []; directs = []; files= []; timepassed = []; 

#testando no HD02

def plot():

    root, contratos, files = next(os.walk("D:/contratos"))
    print(contratos) #testando no HD02
    for i in contratos:
        i = "D:/contratos/"+i
        Bytes, direct, filess, timepass = calculate_size(i) #calcular tamanho por contrato
        BytesCon.append(Bytes) #tamanho das pastas 
        directs.append(direct) 
        files.append(filess)
        timepassed.append(timepass) 


    total, used, free = shutil.disk_usage("D:/")

    print("Total: %d GB" % (total // (2**30))) #Calculando o tamanho total do disco 
    print("Free: %d GB" % (free // (2**30))) #Calculando o espaço livre do disco 

    freeD = (free // (2**30)) #divindo por 2 elevado a trinta 
     
    Name = str(datetime.datetime.now().time())
    Name = Name.replace('.', '_')
    Name = Name.replace(':', '_')

    contratos.append('Livre')
    labels2 = contratos
    labels = []
    
    Bytes.append(freeD)
    sizes = Bytes

    for e, i in zip(contratos, sizes):
        labels.append(f"{e} \n {sizes} GBs")
    colors = ['#ff9999','#66b3ff','#99ff99', '#0f0f0f']
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors = colors,labels=labels, startangle=90)


    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax1.axis('equal')  
    plt.tight_layout()
    fig.savefig(Name+"size.png")
   

    plt.clf()
    fig2 = plt.figure(2)
    x_Axis = np.arange(len(labels[0:3]))
    print(x_Axis)
    plt.bar(x_Axis - 0.2, directs, 0.4, label = 'Nº Diretórios') #criar o gráfico de barras para nº direto/arq por contrat
    plt.bar(x_Axis + 0.2, files, 0.4, label = 'Nº Arquivos') 

    
    plt.xticks(x_Axis, labels2[0:3])
    plt.title("Diretórios e Arquivos por Contrato")

    plt.savefig(Name+"bar.png") #plot circular, o nome do arquivo contem a hora em que ele foi criado

    
while True:
    plot()
    time.sleep(4000)
