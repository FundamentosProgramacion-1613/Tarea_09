#encoding: UTF-8
#Autor: Hector David Hernandez Rodriguez
#Tarea 9

from Myro import*
from Graphics import*

def interpretarFuncion(lectura):
    l = lectura.split()

    if str(Lista[0])=="v":
        return "ventana"
    elif (Lista.count("#"))>=1:
        pass
    elif str(Lista[0])=="r":
        return "rectangulo" 
    elif str(Lista [0])=="c":
        return "circulo"
    elif str(Lista[0])=="l":
        return "linea"


def main ():
    miArchivo= pickAFile()
    entrada= open("miArchivo.txt","r")
    lectura= entrada.readline()
    
    while lectura != "":
    
        Funcion=interpretarFuncion(lectura)
        if Funcion == "ventana":
            lVentana = lectura.split()
            v = Window(str(lVentana[1]),int(lVentana[2]),int(lVentana[3]))
            
        elif Funcion == "rectangulo":
            lRectangulo = lectura.split()
            Usuarior = Rectangle((lRectangulo[1],lRectangulo[2]),(lRectangulo[3],lRectangulo[4]))
            Usuarior.fill = (None)
            if (len(lRectangulo)) == 6:
                Usuarior.fill = Color(str(listaRectangulo[5]))    
            Usuarior.draw(v)
                
        elif Funcion == "linea":
            lLinea = lectura.split()
            Usuariol = lLine((lLinea[1],lLinea[2]),(lLinea[3],lLinea[4]))
            if len(lLinea) == 6:  
                Usuariol.border = 5
                Usuariol.color = Color(str(listaLinea[5]))
            Usuariol.draw(v)
            
        elif Funcion == "circulo":
            lCirculo = lectura.split()
            Usuarioc = Circle((int(lCirculo[1]),int(lCirculo[2])),int(lCirculo[3]))
            Usuarioc.fill = (None)
            if (len(lCirculo)) == 5: 
                Usuarioc.fill = Color(str(listaCirculo[4]))
            Usuarioc.draw(v)
        contenido = entrada.readline()
    entrada.close()
main() 