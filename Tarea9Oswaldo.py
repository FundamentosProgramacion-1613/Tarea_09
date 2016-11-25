#Oswaldo Morales Rodriguez
#A01378566
#Dibujar lo que se pide en el archivo
#Encoding: UTF-8

from Graphics import *
from Myro import *
 
def hacerVentana(valor):
    global v
    v = Window(valor[3], int(valor[1]),int(valor[2]))
    
    
def hacerRectangulo(valor):
    rectangulo = Rectangle((int(valor[1]),int(valor[2])), (int(valor[3]), int(valor[4])))
    if len(valor) == 5:
        rectangulo.fill = None
    else:
        rectangulo.fill = Color(valor[5])
    rectangulo.draw(v)
    
def hacerCirculo(valor):
    circulo = Circle((int(valor[1]),int(valor[2])),int(valor[3]))
    if len(valor)== 4:
        circulo.fill = None
    else:
        circulo.fill = Color(valor[4])
    circulo.draw(v)
    
    
def hacerLinea(valor):
    linea = Line((int(valor[1]), int(valor[2])),(int(valor[3]), int(valor[4])))
    if len(valor) == 5:
        linea.fill= None
    else:
        linea.fill = Color(valor[5])
    linea.draw(v)
    
def main():
    archivo = open(pickAFile(),"r")
    linea = archivo.readline()
    while linea!="":
        valor= linea.split()
        
        if valor[0]=="#":
            linea = archivo.readline()

        elif valor[0]=="v":
            hacerVentana(valor)
            linea = archivo.readline()

        elif valor[0]=="r":
            hacerRectangulo(valor)
            linea = archivo.readline()

        elif valor[0]=="c":
            hacerCirculo(valor)
            linea = archivo.readline()
            
        elif valor[0]=="l":
            hacerLinea(valor)
            linea = archivo.readline()
    
    
main()