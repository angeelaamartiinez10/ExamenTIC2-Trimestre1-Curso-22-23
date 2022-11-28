'''
Crea una función que NO reciba ningún parámetro y que imprima por pantalla las opciones: 1-Sumar 2-Salir
'''


def menu():
    print ("Las opciones son: \n 1--> SUMAR \n 2--> SALIR")

menu()

'''
Crea una función que reciba dos números y devuelva la suma de estos números.
'''

def numeros(num1,num2):
    return(num1+num2)


opcion=0
opcion=(int)(input("Elige un opción"))

while opcion!=2:
    menu()
    opcion=(int)(input("Elige un opción"))
    
    if opcion==1:
        num1=(int)(input("dime el valor del numero 1:"))
        num2=(int)(input("dime el valor del numero 2:"))
        print("la suma es:",numeros(num1,num2))
        
    

    
