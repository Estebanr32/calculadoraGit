print ("Hola, bienvenido a Calculator.git")

operacion = int(input("Ingrese la operación que desea usar:\n1.Suma\n2.Resta\n3.Multiplicación\n4.División"))

def suma (a,b):
    result = a + b
    return result

def resta (a,b):
    result = a - b
    return result

def multiplicacion (a,b):
    result = a*b
    return result 

def division (numerador, denominador):
    if(denominador == 0):
        print("Resultado indeterminado")
    result = numerador / denominador
    
num1 = int(input("Ingrese el número 1"))    
num2 = int(input("Ingrese el número 2"))        
    
match operacion:
    case 1:
        suma(num1, num2)
    case 2:
        resta(num1, num2)
    case 3:
        multiplicacion(num1, num2)
    case 4:
        division(num1, num2)     
                   