#encoding: UTF-8
#Marlon Brandon Velasco Pinello, A01379404
#Tarea #9
from Myro import pickAFile
from Graphics import *

def crearVentana(parametro):
    v=Window(str(parametro[3]),int(parametro[1]),int(parametro[2]))
    return v
    
def dibujarRectangulo(parametro,v):
    rectangulo=Rectangle((int(parametro[1]),int(parametro[2])),(int(parametro[3]),int(parametro[4])))
    if len(parametro)<6:
        rectangulo.fill=(None)
    else:
        rectangulo.fill=Color(str(parametro[5]))
    rectangulo.draw(v)

def dibujarCirculo(parametro,v):
    circulo=Circle((int(parametro[1]),int(parametro[2])),int(parametro[3]))
    if len(parametro)<5:
        circulo.fill=(None)
    else:
        circulo.fill=Color(str(parametro[4]))
    circulo.draw(v)

def dibujarLinea(parametro,v):
    linea=Line((int(parametro[1]),int(parametro[2])),(int(parametro[3]),int(parametro[4])))
    if len(parametro)<6:
        linea.color=Color("Black")
    else:
        linea.color=Color(str(parametro[5]))
    linea.draw(v)
    
def main():
    nombreArchivo=pickAFile()
    entrada=open(nombreArchivo,"r")
    while True:
        codigo=entrada.readline()
        if codigo!="":
            parametro=codigo.split()
            if parametro[0]=="#":
                pass
            elif parametro[0]=="v":
                v=crearVentana(parametro)
            elif parametro[0]=="r":
                dibujarRectangulo(parametro,v)
            elif parametro[0]=="c":
                dibujarCirculo(parametro,v)
            elif parametro[0]=="l":
                dibujarLinea(parametro,v)
        else:
            break
    #da pausa a la pantalla hasta que se da clic en ella
    #v.getMouse()
    #cierra la pantalla
    #v.close()
    
main()

            


