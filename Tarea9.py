#encoding: UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descripción: Tarea #9
from Graphics import*
def main():
    archivo=open("archivoTarea9.txt","r")
    linea=archivo.readline(0)
    for linea in archivo:
        lista=linea.split()
        if lista[0]=="v":
            valor1=int(lista[1])
            valor2=int(lista[2])
            #print(valor1,valor2)
            v=Window(lista[3],valor1,valor2)
        elif lista[0]=="r":
            valor1=int(lista[1])
            valor2=int(lista[2])
            valor3=int(lista[3])
            valor4=int(lista[4])
            if len(lista)>5:
                r=Rectangle((valor1,valor2),(valor3,valor4))
                r.fill=Color(lista[5])
                #l.border=90
                r.draw(v)
                #print (lista)
            else:
                r.Rectangle((valor1,valor2),(valor3,valor4))
                r.draw(v)
        elif lista[0]=="c":
            valor1=int(lista[1])
            valor2=int(lista[2])
            radio=int(lista[3])
            if len(lista)>4:
                c=Circle((valor1,valor2),radio)
                c.fill=Color(lista[4])
                c.draw(v)
            else:
                c=Circle((valor1,valor2),radio)
                c.draw(v)
        elif lista[0]=="l":
            valor1=int(lista[1])
            valor2=int(lista[2])
            valor3=int(lista[3])
            valor4=int(lista[4])
            if len(lista)>5:
                l=Line((valor1,valor2),(valor3,valor4))
                l.fill=Color(lista[5])
                #l.border=90
                l.draw(v)
                #print (lista)
            else:
                l=Line((valor1,valor2),(valor3,valor4))
                l.draw(v)
         
        #print (lista) 
    archivo.close()
main()