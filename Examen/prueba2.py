# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:23:47 2020

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
        self.palabra.append("libros")
        self.palabra.append("apuntes")
        self.palabra.append("colores")
        self.palabra.append("pizarron")
        self.palabra.append("plumones")
        self.palabra.append("alumnos")
        self.palabra.append("profesores")
        self.palabra.append("salones")
        self.palabra.append("bancas")
        self.palabra.append("pizarron")
        #print(self.palabra)

def compruebaEspacios(palabra,matriz, ocupados, tamaño, x, y):
    posiblespos=[]
    ren=x
    col=y
    iguales=0
    seEscribio=False
    
    if x+tamaño<14:#para la validacion vertical se usa x porque son los renglones
        for k in palabra:
            for i in range(tamaño):
                posiblespos.append([ren,col])
                ren+=1
            for i in posiblespos:
                if i in ocupados:
                    iguales+=1
            if iguales>0:
                break
            matriz[x][y]=k
            ocupados.append([x,y])
            x+=1
        seEscribio=True
            
    if x-tamaño>0 and seEscribio==False:
        for k in palabra:
            for i in range(tamaño):
                posiblespos.append([ren,col])
                ren-=1
            for i in posiblespos:
                if i in ocupados:
                    iguales+=1
            if iguales>0:
                break
            matriz[x][y]=k
            x-=1
        seEscribio=True
    if y+tamaño<14 and seEscribio==False:
        for k in palabra:
            for i in range(tamaño):
                posiblespos.append([ren,col])
                col+=1
            for i in posiblespos:
                if i in ocupados:
                    iguales+=1
            if iguales>0:
                break
            matriz[x][y]=k
            y+=1
        seEscribio=True
    if y-tamaño>0 and seEscribio==False:
        for k in palabra:
            for i in range(tamaño):
                posiblespos.append([ren,col])
                ren+=1
            for i in posiblespos:
                if i in ocupados:
                    iguales+=1
            if iguales>0:
                break
            matriz[x][y]=k
            y-=1
        seEscribio=True
    print(seEscribio)
    return seEscribio,matriz
   
    
      
def mezclaPalabras(matriz, palabras):
    ocupados=[]
    seEscribio=False
    for i in palabras:
        while seEscribio==False:
            x=random.randint(0,14)
            y=random.randint(0,14)
            seEscribio, matriz=compruebaEspacios(i,matriz, ocupados,len(i),x,y)
            for i in range(15):
                print(matriz[i])
            print("\n\n")
    
    return matriz
        
            
            
            
        
def main():    
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
   
    dato=matriz.m
    dato2=palabras(random.randint(0,4));
    enviar2=dato2.palabra
    dato=mezclaPalabras(dato, enviar2)
    print(enviar2)
    dato=pickle.dumps(dato);
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
               
main()