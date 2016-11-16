#encoding: UTF-8
#Autor: Adrian Tellez
#Tarea de Archivos

from Graphics import *
from Myro import pickAFile
 
def hacerVentana(lista):
    global v
    v = Window(lista[3], int(lista[1]), int(lista[2]))
    return v
     
     
def hacerRectangulo(lista):
    r = Rectangle((int(lista[1]), int(lista[2])), (int(lista[3]), int(lista[4]))) 
    if len(lista) != 5: 
        r.fill = Color(lista[5])
    r.draw(v)
 
def hacerCirculo(lista):
    c = Circle((int(lista[1]), int(lista[2])), int(lista[3]))
    if len(lista) != 4:
        c.fill = Color(lista[4])
    c.draw(v)
       
def hacerLinea(lista):
    l = Line((int(lista[1]), int(lista[2])), (int(lista[3]), int(lista[4])))
    if len(lista) == 6:
        l.color = Color(lista[5])
    l.draw(v)
     
def main():
    elegirArchivo = (pickAFile())
    archivo = open(elegirArchivo, "r")
    for lineas in archivo:
        lista = lineas.split() 
        if lista[0] == "v":
            v = hacerVentana(lista)
        elif lista[0] == "r":
            r = hacerRectangulo(lista)
        elif lista[0] == "c":
            c = hacerCirculo(lista)
        elif lista[0] == "l":
            l = hacerLinea(lista)
    
    archivo.close()   
    
    
main()