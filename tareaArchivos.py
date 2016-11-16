#encoding: UTF-8
#Autor: Marina Itzel Haro Hernández, A01373471

from Myro import pickAFile
from Graphics import*

def crearVentana(lista):
    global v
    v = Window(lista[3], int(lista[1]), int(lista[2]))
    return v
    
    
def crearRectangulo(lista):
    r = Rectangle((int(lista[1]), int(lista[2])), (int(lista[3]), int(lista[4]))) 
    if len(lista) == 5: 
        r.fill = None
    else:
        r.fill = Color(lista[5])
    r.draw(v)

def crearCirculo(lista):
    c = Circle((int(lista[1]), int(lista[2])), int(lista[3]))
    if len(lista) == 4:
        c.fill = None
    else:
        c.fill = Color(lista[4])
    c.draw(v)
        
def crearLinea(lista):
    l = Line((int(lista[1]), int(lista[2])), (int(lista[3]), int(lista[4])))
    if len(lista) == 6:
        l.color = Color(lista[5])
    l.draw(v)
    
def main():
    nombreArchivo = pickAFile()
    archivo = open(nombreArchivo, "r")
    for lineas in archivo:
        lista = lineas.split() 
    
        if lista[0] == "v":
            v = crearVentana(lista)
        elif lista[0] == "r":
            r = crearRectangulo(lista)
        elif lista[0] == "c":
            c = crearCirculo(lista)
        elif lista[0] == "l":
            l = crearLinea(lista)
    archivo.close()
    
main()
        
    
