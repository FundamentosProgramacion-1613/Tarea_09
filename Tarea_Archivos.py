#encoding: UTF-8
#Jesús Perea
#Tarea_Archivos
from Graphics import *
from Myro import pickAFile

def dibujarRectangulo(contenido,v):
    palabra = contenido.split()
    print(palabra)
    numx1 = int(palabra[1])
    numy1 = int(palabra[2])
    numx2 = int(palabra[3])
    numy2 = int(palabra[4])
    color = palabra[5]
    rectangulo = Rectangle((numx1,numy1),(numx2,numy2))
    rectangulo.color = Color(color)
    rectangulo.draw(v)
        
def definirVentana(contenido):
    palabra = contenido.split()
    print(palabra)
    x = int(palabra[1])
    y = int(palabra[2])
    nombre = palabra[3]
    print(x,y,nombre)
    v = Window(nombre,x,y)
    return v

def dibujarCirculo(contenido,v):
    palabra = contenido.split()
    print(palabra)
    centx = int(palabra[1])
    centy = int(palabra[2])
    radio = int(palabra[3])
    color = palabra[4]
    circulo = Circle((centx,centy),radio)
    circulo.color = Color(color)
    circulo.draw(v)

def dibujarLinea(contenido,v):
    palabra = contenido.split()
    print(palabra)
    numx1 = int(palabra[1])
    numy1 = int(palabra[2])
    numx2 = int(palabra[3])
    numy2 = int(palabra[4])
    linea = Line((numx1,numy1),(numx2,numy2))
    print(len(palabra))
    if len(palabra)== 6:
        color = palabra[5]
        linea.color = Color(color)
    linea.draw(v)

def main():
    
    archivo = open(pickAFile())
    contenido = archivo.readline()
    #letra = archivo.read()

    while contenido != "":
        lista = contenido.split()
        if lista[0] == "v":
            v = definirVentana(contenido)
        elif lista[0] == "r": 
            dibujarRectangulo(contenido,v)
        elif lista[0] == "c":
            dibujarCirculo(contenido,v)
        elif lista[0] == "l":
            dibujarLinea(contenido,v)
        contenido = archivo.readline()

    archivo.close()
main()