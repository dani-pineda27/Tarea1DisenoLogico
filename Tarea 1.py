# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:24:42 2023

@author: dapif
"""
#-------Funciones--------------
def Decimal_a_base(num,base):
    lista_enteros=[]
    entera=int(num-(num%1))
    fracc=float(num%1)
    while entera!=0:       
        lista_enteros.append(entera%base)
        entera=entera//base
    lista_enteros.reverse()
    lista_enteros=Base_a_hexadecimal(lista_enteros)
    
    conversion=str("")
    for i in lista_enteros:
        conversion=conversion+str(i)
    
    lista_fraccion=[]
    for y in range(8):
        num2=float(fracc*base)
        entera2=int(num2-(num2%1))
        fracc=float(num2%1)
        lista_fraccion.append(entera2)
        
    lista_fraccion=Base_a_hexadecimal(lista_fraccion)    
    conversion=conversion+str(".")
    for i in lista_fraccion:
        conversion=conversion+str(i)
        
    return conversion
    

def Base_a_hexadecimal(lista_enteros):
    array_letras=["A","B","C","D","E","F","G"]
    n=int(10)
    while n<17:
        for i in range (len(lista_enteros)):
            if lista_enteros[i]==n:
                lista_enteros[i]=array_letras[n-10]
                
        n=n+1
    return lista_enteros
    
    
def Base_a_decimal(num,base):
    lista_separada=[]
    lista_separada=num.split(".")
    
    lista_enteros=[]
    lista_enteros=list(lista_separada[0])

    lista_fraccion=[]
    lista_fraccion=list(lista_separada[1])    

    numero=int(0)
    potencia=len(lista_enteros)
    
    for i in range(len(lista_enteros)):
        numero=numero+(int(lista_enteros[i])*(base**(potencia-1)))
        potencia-=1

    for y in range(len(lista_fraccion)):
        numero=numero+(int(lista_fraccion[y])*(base**(potencia-1)))
        potencia -= 1
        
    return numero
    
#--------Main------------------

while True:
    print("\n-------------------")
    print("Presione 1 para convertir de decimal a base r.")
    print("Presione 2 para convertir de base r a decimal.")
    print("Presione 0 para terminar el programa.")
    
    try:
        opcion=int(input())
           
        if opcion==0:
            break
        
        elif opcion==1:
            num=float(input("\nIngrese un número con parte fraccionaria: "))
            base=int(input("\nIngrese la base: " ))
    
    
            print("\n")
            print(Decimal_a_base(num,base))
            
        elif opcion==2:
            num=str(input("\nIngrese un número con parte fraccionaria: "))        
            base=int(input("\nIngrese la base: " ))
            print("\n")
            print(Base_a_decimal(num,base))
            
        else:
            print("\nERROR: escriba una opción válida.")
            
    except ValueError:
        print("\nERROR: Debes ingresar un número.")
    except:
        print("\nERROR: Error desconocido.")
 

    
    

