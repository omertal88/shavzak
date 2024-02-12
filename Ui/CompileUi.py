from os import path
from subprocess import call
from PyQt5.uic import compileUiDir
from glob import glob

compileUiDir(path.dirname(__file__), from_imports = True, import_from = "Ui")

qrcFiles = glob(path.join(path.dirname(__file__), "*.qrc"))

for qrcFile in qrcFiles:
    
    call(["pyrcc5", qrcFile, "-o", qrcFile.replace(".qrc", "_rc.py")])