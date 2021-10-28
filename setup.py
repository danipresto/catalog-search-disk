from cx_Freeze import setup, Executable

base = None

executables = [Executable("Bucaimgs.py", base=base)] #Nome do .py

packages = ["idna", "os", "openpyxl", "glob", "fnmatch", "isoparser", "sys"] #Todos os pacotes utilizados 
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

#Versão 

setup(
    name = "<first>",
    options = options,
    version = "<1.0>",
    description = '<teste>',
    executables = executables
)





#Executar usando python local\setup.py build

