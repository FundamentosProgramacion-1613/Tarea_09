#encoding: UTF-8
#Karla Valeria Alcantara Duarte
#Tarea 9
from Graphics import *
from Myro import pickAFile

def crearVentana(lista):
    v = Window(lista[3],int(lista[1]),int(lista[2]))
    return v
       
def crearRectangulo(v,lista):
    rectangulo = Rectangle((int(lista[1]),int(lista[2])),(int(lista[3]),int(lista[4])))
    rectangulo.fill = Color(elegirColor(lista))
    rectangulo.draw(v)
    
def crearLinea(v,lista):
    linea = Line((int(lista[1]),int(lista[2])),(int(lista[3]),int(lista[4])))
    linea.fill = Color(elegirColor(lista))
    linea.draw(v)
    
def crearCirculo(v,lista):
    circulo = Circle((int(lista[1]),int(lista[2])),int(lista[3]))
    circulo.fill = Color(elegirColor(lista))
    circulo.draw(v)
    
def elegirColor(lista):
    color = None
    if lista[0]=="c":
        color = lista[4]
    elif len(lista)==5 and lista[0]=="l":
        color = "black"
    elif len(lista)==6:
        color = lista[5]
    return color             

def main():
    nombreArchivo = pickAFile()
    print(nombreArchivo)
    archivo = open(nombreArchivo,"r")
    texto = archivo.readline()
    while texto!= "":
        lista = texto.split()
        if lista[0]=="v":
            v = crearVentana(lista)
        
        elif lista[0]=="r":
            crearRectangulo(v,lista)
        
        elif lista[0]=="l":
            crearLinea(v,lista)
        
        elif lista[0]=="c":
            crearCirculo(v,lista)
            
        texto = archivo.readline()
            
      
    archivo.close()
    
        
    
    
    
    
main()   
    