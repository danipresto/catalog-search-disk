import sys
from PySide6 import QtGui, QtWidgets, QtCore 
import openpyxl; from openpyxl import load_workbook
import os

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
                                            #definindo a resolução da tela
        self.left = 0 
        self.top = 0
        self.width = 500
        self.height = 300

        self.tittle = 'Busca de arquivos'
        self.initUI()
        self.p = None
        self.infor3 = None

        #self.Createtoolbar()             
    
    def initUI(self):  #Criar os butões e as caixas de texto
        
        self.setWindowTitle(self.tittle)
        self.setWindowIcon(QtGui.QIcon("download.jpg")) #Adicionando o ícone da Mobit 
        self.setGeometry(self.left, self.top, self.width, self.height) 
        self.Layout = QtWidgets.QGridLayout(self)
        QtGui.QCursor.setPos(300,300) #Posição do cursor
        self.Layout.setVerticalSpacing(30)
        self.Layout.setHorizontalSpacing(25)

#Criando os botões
        self.button1 = QtWidgets.QPushButton("INICIAR PESQUISA") 
        self.button2 = QtWidgets.QPushButton("Buscar por .iso")       
        self.button3 = QtWidgets.QPushButton("Pesquisar por Planilha")

        self.button1.setMaximumWidth(200)
        self.button1.setMinimumWidth(175)
        
#Cores dos botões
        self.button1.setStyleSheet("background-color : rgb(27, 29, 35);")
        self.button2.setStyleSheet("background-color : rgb(27, 29, 35);")
        self.button3.setStyleSheet("background-color : rgb(27, 29, 35);")
        
#Criando as legendas        
        self.text = QtWidgets.QLabel("BUSCA DE ARQUIVOS EM HDs", alignment=QtGui.Qt.AlignCenter)
        self.text1 = QtWidgets.QLabel("Pesquisar por Arquivo Único")   
        self.text3 = QtWidgets.QLabel(alignment=QtGui.Qt.AlignCenter)

        self.text.setStyleSheet("color : white; font-size: 20px")
        self.text1.setStyleSheet("color : white; font-size: 15px")
      
        self.textbox1 = QtWidgets.QLineEdit(alignment=QtGui.Qt.AlignLeft)
        self.textbox2 = QtWidgets.QLineEdit(alignment=QtGui.Qt.AlignLeft)
      
        self.textbox1.setPlaceholderText("Insira o Contrato: ")
        self.textbox2.setPlaceholderText("Insira o Arquivo: ")
    
        self.textbox1.setMaximumWidth(150)
        self.textbox1.setMaximumHeight(75)
        self.textbox1.setMinimumHeight(25)
        self.textbox1.setMinimumWidth(175)
        self.textbox2.setMinimumHeight(25)
        self.textbox2.setMaximumWidth(350)
        
     
        
       
#Definindo layout geral       
        self.setStyleSheet("color : white; background-color : rgb(44, 49, 60); font-size: 12px")

#Adicionando as funcionalidades na matriz da tela
        self.Layout.addWidget(self.text, 1, 1)
        self.Layout.addWidget(self.button3, 1, 0)
        self.Layout.addWidget(self.text1, 2, 0)
        self.Layout.addWidget(self.textbox1, 3, 0)
        self.Layout.addWidget(self.textbox2, 3, 1)
        self.Layout.addWidget(self.button1, 3, 3)
        self.Layout.addWidget(self.button2, 4, 3)
        self.Layout.addWidget(self.text3, 4, 1)
        
#Chama os eventos caso os botões ou a tecla enter sejam pressionados         
        self.textbox1.returnPressed.connect(self.magic) #chama as funções 
        self.textbox2.returnPressed.connect(self.magic)

        self.button1.clicked.connect(self.starts)
        self.button2.clicked.connect(self.typesearch1)
        

        self.myfile = "Search.exe" #arquivo do c++ já compilado, ele que executa as buscas e cria o resultado.txt


#Definindo o que acontece quando enter é pressionado
    @QtCore.Slot()
    def magic(self):
        self.infor1 = self.textbox1.text()
        self.infor2 = self.textbox2.text()
        print(self.infor1, self.infor2)
        self.textbox1.clear()
        self.textbox2.clear()

#Vai ser removido
    @QtCore.Slot()
    def typesearch1(self):
        self.infor3 = ".iso"  


#Em implementação, objetivo é pesquisar por todos elementos em uma planilha.

    def search_using_csv(self): 
        excel_file = 'EntradadoUsuário.xlsx' #Ainda em implementação
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
    

        
        self.message("EXECUTANDO BUSCA... ")
        for e in paths:
            self.p = QtCore.QProcess()  
            self.p.finished.connect(self.process_finished)  
            self.p.start(self.myfile, [self.infor1, e, "using_csv"])


    def starts(self): #botão de iniciar a pesquisa

        if self.infor3 is None:
            if self.p is None:  
                self.message("EXECUTANDO BUSCA... ")
                self.p = QtCore.QProcess()  
                self.p.finished.connect(self.process_finished)  
                self.p.start(self.myfile, [self.infor1, self.infor2]) #chama o programa Search.exe
        else:
            if self.p is None:  
                self.message("EXECUTANDO BUSCA... ")
                self.p = QtCore.QProcess()  
                self.p.finished.connect(self.process_finished)  
                self.p.start(self.myfile, [self.infor1, self.infor2, self.infor3]) #chamando o .exe

    def process_finished(self):
        self.message("BUSCA CONCLUÍDA !") #Quando concluir muda o texto
        self.p = None

    def message(self, txt):
        self.text3.setText(txt)
#Não implementado
    def Createtoolbar(self):
        self.mainToolBar = QtWidgets.QToolBar('Main')
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])


    widget = MyWidget()

    qRect = widget.frameGeometry()
    centerPoint = QtGui.QScreen.availableGeometry(QtWidgets.QApplication.primaryScreen()).center()
    qRect.moveCenter(centerPoint)
    widget.move(qRect.topLeft())


    widget.show() 

    sys.exit(app.exec())    

