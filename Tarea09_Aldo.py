
from Graphics import *
from Myro import pickAFile

def crearVentana(comando):
    v = Window(comando[3],int(comando[1]),int(comando[2]))

    return v
def dibujarRectangulo(comando,v):
    r = Rectangle((int(comando[1]),int(comando[2])),(int(comando[3]),int(comando[4])))
    if len(comando)>5:
        r.fill = Color(comando[5])
    r.draw(v)

def dibujarLinea(comando,v):
    l = Line((int(comando[1]),int(comando[2])),(int(comando[3]),int(comando[4])))
    if len(comando)>5:
        l.color = Color(str(comando[5]))
    l.draw(v)

def dibujarCirculo(comando,v):
    c = Circle((int(comando[1]),int(comando[2])),int(comando[3]))
    if len(comando)>4:
        c.fill = Color(comando[4])
    c.draw(v)
    
def main():
    documento = pickAFile()
    entrada = open(documento,"r")
    for linea in entrada:
        comando = linea.split()
        if comando[0] == "v":
            v = crearVentana(comando)
        if comando[0] == "r":
            dibujarRectangulo(comando,v)
        if comando[0] == "l":
            dibujarLinea(comando,v)
        if comando[0] == "c":
            dibujarCirculo(comando,v)
        print(comando)
    entrada.close()
main()
