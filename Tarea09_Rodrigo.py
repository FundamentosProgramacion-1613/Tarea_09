# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Tarea 9 sobre Archivos

from Graphics import *
from Myro import pickAFile

# Función que dibuja una ventana con nombre y dimensiones definidas por el archivo
def dibujarVentana(parametros):
    global ventana
    ventana = Window(parametros[3], int(parametros[1]), int(parametros[2]))

# Función que dibuja un rectángulo en ventana con dimensiones definidas por el archivo
def dibujarRectangulo(parametros):
    rectangulo = Rectangle((int(parametros[1]), int(parametros[2])), (int(parametros[3]), int(parametros[4])))
    if len(parametros) == 5: #son cinco porque también se cuenta el comando r
        rectangulo.fill = None
    else:
        rectangulo.fill = Color(parametros[5])
    rectangulo.draw(ventana)

# Función que dibuja un círculo en ventana con dimensiones definidas por el archivo
def dibujarCirculo(parametros):
    circulo = Circle((int(parametros[1]), int(parametros[2])), int(parametros[3]))
    if len(parametros) == 4:
        circulo.fill = None
    else:
        circulo.fill = Color(parametros[4])
    circulo.draw(ventana)

# Función que dibuja una linéa en ventana con dimensiones definidas por el archivo
def dibujarLinea(parametros):
    linea = Line((int(parametros[1]), int(parametros[2])), (int(parametros[3]), int(parametros[4])))
    if len(parametros) == 6:
        linea.color = Color(parametros[5])
    linea.draw(ventana)
    
# Función que dibuja un triángulo en ventana con deimensiones definidasp or el archivo
def dibujarTriangulo(parametros):
    triangulo = Polygon((int(parametros[1]), int(parametros[2])), (int(parametros[3]), int(parametros[4])), (int(parametros[5]), int(parametros[6])))
    if len(parametros) == 7:
        triangulo.fill = None
    else:
        triangulo.fill = Color(parametros[7])
    triangulo.draw(ventana)
    
def main():
    archivo = open(pickAFile(), "r")
    for comando in archivo:
        parametros = comando.split() #lista con el comando y parametros que se desean ejecutar
        if parametros[0] == "#":
            continue
        elif parametros[0] == "v":
            dibujarVentana(parametros)
        elif parametros[0] == "r":
            dibujarRectangulo(parametros)
        elif parametros[0] == "c":
            dibujarCirculo(parametros)
        elif parametros[0] == "l":
            dibujarLinea(parametros)
        elif parametros[0] == "t":
            dibujarTriangulo(parametros)
        else: 
            print("comando inválido")
    archivo.close()      
main()