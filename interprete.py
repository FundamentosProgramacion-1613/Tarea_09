#encoding:UTF-8
#Autor: José Javier Rodríguez Mota
#Descripción: Interprete de Python
from Myro import pickAFile
from Graphics import *
def leerArchivo():
    documento=pickAFile()
    print("Abriendo documento "+documento+". Por favor espere...")
    return documento
def hacerVentana(texto):
    v= Window(texto[3],int(texto[1]),int(texto[2]))
    return v
def hacerRectangulo(texto,v):
    rectangulo=Rectangle((int(texto[1]),int(texto[2])),(int(texto[3]),int(texto[4])))
    rectangulo.fill=Color(elegirColor(texto))
    rectangulo.draw(v)
def elegirColor(texto):
    color=None
    if len(texto)==6:
        color=texto[5]
    elif texto[0]=='l':
        color='black'
    elif texto[0]=='c' and len(texto)==5:
        color=texto[4]
    return color
def hacerCirculo(texto,v):
    circulo=Circle((int(texto[1]),int(texto[2])),int(texto[3]))
    circulo.fill=Color(elegirColor(texto))
    circulo.draw(v)
def hacerLinea(texto,v):
    linea=Line((int(texto[1]),int(texto[2])),(int(texto[3]),int(texto[4])))
    linea.color=Color(elegirColor(texto))
    linea.draw(v)
def main():
    doc=open(leerArchivo(),'r')
    contenido=doc.readline()
    while contenido!='':
        texto=contenido.split()
        if not any('#' in lista for lista in texto):
            if texto[0]=='v':
                v=hacerVentana(texto)
            if texto[0]=='r':
                hacerRectangulo(texto,v)
            if texto[0]=='c':
                hacerCirculo(texto,v)
            if texto[0]=='l':
                hacerLinea(texto,v)        
        contenido=doc.readline()
    print("Felicidades, el archivo ha sido leido correctamente")
    doc.close()
main()
