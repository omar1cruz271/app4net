# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:49:26 2020

@author: omar-
"""


import socket
import random
import pickle


class matriz:
    #def __init__(self):    
    m=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    sopa=[]
    def __init__(self):
        for i in range(15):
           self.sopa.append(self.m[0][0])
        for i in range(15):
            print(self.sopa[i])
            
class palabras:
    
    def __init__(self, rand):
        self.palabra=[]#crea una lista vacia para cada clase palabras
        n=rand
        print(n)
        if n==0:
            self.escuela()
        elif n==1:
            self.escuela()
        elif n==2:
            self.escuela()
        elif n==3:
            self.escuela()
        elif n==4:
            self.escuela()
    def escuela(self):
        print("me meti")
        self.palabra.append("LIBROS")
        self.palabra.append("APUNTES")
        self.palabra.append("COLORES")
        self.palabra.append("PIZARRON")
        self.palabra.append("PLUMONES")
        self.palabra.append("ALUMNOS")
        self.palabra.append("PROFESORES")
        self.palabra.append("SALONES")
        self.palabra.append("BANCAS")
        self.palabra.append("CUADERNO")
        #print(self.palabra)


def compruebaEspacios(palabra,matriz, ocupados, tamaño, x, y):
    seEscribio=False
    deshacer=1
    pos=1
    inifin=[]
    if x+tamaño<14:#para la validacion vertical se usa x porque son los renglones
        for i in palabra:
            if [x,y] in ocupados and matriz[x][y]!=i:
                for m in range(deshacer):
                    ocupados.pop(len(ocupados)-1)
                return False, matriz,ocupados,None
            matriz[x][y]=i
            if pos==1:
                inifin.append(x)
                inifin.append(y)
                
            ocupados.append([x,y])
            deshacer+=1
            pos+=1
            x+=1
        inifin.append(x-1)
        inifin.append(y)
        seEscribio=True
            
    elif x-tamaño>0:
        for i in palabra:
            if [x,y] in ocupados and matriz[x][y]!=i:
                for m in range(deshacer):
                    ocupados.pop(len(ocupados)-1)
                return False, matriz,ocupados,None
            matriz[x][y]=i
            if pos==1:
                inifin.append(x)
                inifin.append(y)
            ocupados.append([x,y])
            deshacer+=1
            pos+=1
            x-=1
        inifin.append(x+1)
        inifin.append(y)
        seEscribio=True
    elif y+tamaño<14:
        for i in palabra:
            if [x,y] in ocupados and matriz[x][y]!=i:
                for m in range(deshacer):
                    ocupados.pop(len(ocupados)-1)
                return False, matriz,ocupados,None
            matriz[x][y]=i
            if pos==1:
                inifin.append(x)
                inifin.append(y)
            ocupados.append([x,y])
            deshacer+=1
            pos+=1
            y+=1
        inifin.append(x)
        inifin.append(y-1)
        seEscribio=True
    elif y-tamaño>0:
        for i in palabra:
            if [x,y] in ocupados and matriz[x][y]!=i:
                for m in range(deshacer):
                    ocupados.pop(len(ocupados)-1)
                return False, matriz,ocupados,None
            matriz[x][y]=i
            if pos==1:
                inifin.append(x)
                inifin.append(y)
            ocupados.append([x,y])
            deshacer+=1
            pos+=1
            y-=1
        inifin.append(x)
        inifin.append(y+1)
        seEscribio=True
    print("inifin",inifin)
    return seEscribio, matriz, ocupados, inifin
   
    
      
def mezclaPalabras(matriz, palabras):
    ocupados=[]
    posiciones=[]
    seEscribio=False
    for i in range(len(palabras)):
        while seEscribio==False:
            x=random.randint(0,14)
            y=random.randint(0,14)
            seEscribio,matriz, ocupados,inifin=compruebaEspacios(palabras[i],matriz, ocupados,len(palabras[i]),x,y)
            posiciones.append(inifin)
        if i!= len(palabras)-1:
            seEscribio=False
    for i in range(15):
        print(matriz[i])
    print("\n\n")
    print(posiciones)
    return matriz, posiciones
        
            
            
            
        
def main():    
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
   
    dato=matriz.m
    dato2=palabras(random.randint(0,4));
    enviar2=dato2.palabra
    dato,posiciones=mezclaPalabras(dato, enviar2)
    print(enviar2)
    dato=pickle.dumps(dato)
    posiciones=pickle.dumps(posiciones)
    enviar2=pickle.dumps(enviar2)
    for i in range(15):
        print(matriz.m[i])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                conn.sendall(dato)
                conn.sendall(posiciones)
                conn.sendall(pickle.dumps(dato2.palabra))
main()