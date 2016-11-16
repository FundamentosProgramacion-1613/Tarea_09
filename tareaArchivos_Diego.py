#encoding: UTF-8
#By Diego
#Compilador de Texto - Graphics

from Graphics import *
from Myro import pickAFile

#Lee Archivo-------------------ARCHIVO LEER-------------------
def leerDoc():
    document=pickAFile()
    return document

#DETERMINA COLOR DADO-------------------COLOR-------------------
def entradaColor(lineInput):
    color = "black"
    if (len(lineInput) == 5 and lineInput[0] == "c") or (len(lineInput) == 6):
        color = lineInput[len(lineInput)-1]      
    return color
    
#CREA UNA VENTANA A PARTIR DEL CODIGO-------------------VENTANA-------------------   
def crearVentana(lineInput):
    win = Window(lineInput[3],int(lineInput[1]),int(lineInput[2]))
    return win
    
#CREA UN RECTANGULO-------------------RECTANGULO-------------------
def crearRect(lineInput,win):
    rect = Rectangle((int(lineInput[1]),int(lineInput[2])),(int(lineInput[3]),int(lineInput[4])))
    rect.fill = Color(entradaColor(lineInput))
    rect.draw(win)
#TRAZA UN CIRCULO-------------------CIRCULO-------------------    
def crearCirc(lineInput,win):
    circ = Circle((int(lineInput[1]),int(lineInput[2])),(int(lineInput[3])))
    circ.fill = Color(entradaColor(lineInput))
    circ.draw(win)
#TRAZA UNA LINEA-------------------LINEA-------------------
def crearLinea(lineInput,win):
    linea1 = Line((int(lineInput[1]),int(lineInput[2])),(int(lineInput[3]),int(lineInput[4])))
    linea1.color = Color(entradaColor(lineInput))
    linea1.draw(win)     
def main():
    document = open(leerDoc(),"r")
    for line in document:
        if not "#" in line:
            lineInput = line.split()
            if lineInput[0] == "v":
                win = crearVentana(lineInput)
            if lineInput[0] == "r":
                crearRect(lineInput,win)
            if lineInput[0] == "c":
                crearCirc(lineInput,win)
            if lineInput[0] == "l":
                crearLinea(lineInput,win)        
main()