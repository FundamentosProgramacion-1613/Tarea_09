#encoding: utf-8
#autor: Allan Sánchez Iparrazar
#compilador de 5 funciones

from Myro import pickAFile
from Graphics import * 

#aqui identifica el tipo de funcion que es
def identificarFuncion(contenido):
    
    lista = contenido.split()
    print(lista)
    if str(lista[0]) == "v" :
        return "ventana"
    elif str(lista[0]) == "l":
        return "linea"
    elif str(lista[0]) == "r" :
        return "rectangulo" 
    elif str(lista [0]) == "c" :
        return "circulo"
    elif lista.count("#") >= 1:
        return "comentario"



def main ():
    #1
    archivo = pickAFile()
    data = open(archivo,"r")
    #2
    contenido = data.readline()
    #hacemos un ciclo que dure hasta que el archivo .txt se quede sin lineas
    while contenido != "" :
        #Una vez identificada la funcion pregunta qué función es y ejecuta instrucciones.    
        tipoDeFuncion = identificarFuncion (contenido)
        if tipoDeFuncion == "ventana":
            listaVentana = contenido.split()
            v = Window(str(listaVentana[1]),int(listaVentana[2]),int(listaVentana[3]))
        
        #Dibuja el rectangulo con o sin color    
        elif tipoDeFuncion == "rectangulo":
            listaRectangulo = contenido.split()
            rectanguloUsuario = Rectangle((listaRectangulo[1],listaRectangulo[2]),(listaRectangulo[3],listaRectangulo[4]))
            print(len(listaRectangulo))
            rectanguloUsuario.fill = (None)
            if len(listaRectangulo) == 6 :
                rectanguloUsuario.fill = Color(str(listaRectangulo[5]))
            rectanguloUsuario.draw(v)
                
        #Dibuja una línea con color o sin color
        elif tipoDeFuncion == "linea":
            listaLinea = contenido.split()
            lineaUsuario = Line((listaLinea[1],listaLinea[2]),(listaLinea[3],listaLinea[4]))
            if len(listaLinea) == 6 :  
                print(listaLinea[5])
                lineaUsuario.border = 2
                lineaUsuario.color = Color(listaLinea[5])
            lineaUsuario.draw(v)
            
        #Dibuja la función circulo    
        elif tipoDeFuncion == "circulo":
            listaCirculo = contenido.split()
            circuloUsuario = Circle((int(listaCirculo[1]),int(listaCirculo[2])),int(listaCirculo[3]))
            circuloUsuario.fill = (None)
            if len(listaCirculo) == 5: 
                print(listaRectangulo[4])
                circuloUsuario.fill = Color(str(listaCirculo[4]))
            circuloUsuario.draw(v)
        
        #si es comentario no hace nada
        elif tipoDeFuncion == "comentario":
            pass 
            
        contenido = data.readline()
    #3 liberamos la memoria en bufer
    data.close()

main() 