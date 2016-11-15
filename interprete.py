#encoding:UTF-8
#Autor: José Javier Rodríguez Mota
#Descripción: Interprete de Python
#Importamos las librerias necesarias
from Myro import pickAFile
from Graphics import *
#Esta función lee el archivo que tenemos
def leerArchivo():
    #Elegimos el documento
    documento=pickAFile()
    #Imprimimos mensaje bonito
    print("Abriendo documento "+documento+". Por favor espere...")
    #Regresamos la dirección del documento
    return documento
#Dibujamos ventana
def hacerVentana(texto):
    #Aquí asignamos todos los valores de la ventana
    v= Window(texto[3],int(texto[1]),int(texto[2]))
    return v
#Dibujamos rectángulos
def hacerRectangulo(texto,v):
    #Aquí está cómo hacer rectángulos
    rectangulo=Rectangle((int(texto[1]),int(texto[2])),(int(texto[3]),int(texto[4])))
    rectangulo.fill=Color(elegirColor(texto))
    rectangulo.draw(v)
#Esta es la función que se llama en cada una de las otras, da un color de acuerdo a lo solicitado    
def elegirColor(texto):
    #Primero asignamos que color no tiene ningún valor
    color=None
    #Revisamos qué tan largo es texto
    if len(texto)==6:
        #Le damos un valor al texto, en caso que sea línea o rectángulo
        color=texto[5]
    #Si no tenía color asignado revisamos si era línea para darle black    
    elif texto[0]=='l':
        color='black'
    #Si es círculo es más pequeño por lo que el len es diferente    
    elif texto[0]=='c' and len(texto)==5:
        color=texto[4]
    return color
#Definimos hacer círculo
def hacerCirculo(texto,v):
    circulo=Circle((int(texto[1]),int(texto[2])),int(texto[3]))
    circulo.fill=Color(elegirColor(texto))
    circulo.draw(v)
#Dibujamos línea    
def hacerLinea(texto,v):
    linea=Line((int(texto[1]),int(texto[2])),(int(texto[3]),int(texto[4])))
    linea.color=Color(elegirColor(texto))
    linea.draw(v)
#Definimos nuestro main    
def main():
    #Primero abrimos el documento deseado
    doc=open(leerArchivo(),'r')
    #Leemos la primera línea
    contenido=doc.readline()
    #Revisamos cada línea
    while contenido!='':
        #Hacemos una lista con el contenido de la línea
        texto=contenido.split()
        #Revisamos que no sea comentario la línea
        if not any('#' in lista for lista in texto):
            #Si es ventana, manda a función ventana
            if texto[0]=='v':
                v=hacerVentana(texto)
            #Si es rectángulo, manda a función rectángulo    
            if texto[0]=='r':
                hacerRectangulo(texto,v)
            #Si es círculo, manda a función círculo    
            if texto[0]=='c':
                hacerCirculo(texto,v)
            #Si es línea, manda a función línea    
            if texto[0]=='l':
                hacerLinea(texto,v)        
        #Cambiamos de línea
        contenido=doc.readline()
    #Al acabar el loop finalizamos con un mensaje bonito    
    print("Felicidades, el archivo ha sido leido correctamente")
    #Cerramos el documento
    doc.close()
#Ejecutamos el código    
main()
