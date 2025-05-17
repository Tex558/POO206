
#1. comentarios

# comentarios de una sola linea

""" aqui va un comentario
de varias lineas
en python """ 


#2. strings
print('yo soy otra')

variable1= "hola soy una cadena"

print(len(variable1)) #len = length (cuenta la longitu de la candena)
print (variable1[2:5]) #print por partes (del 2ndo al 5nto)
print (variable1[2:])
print (variable1[:5])

#3. variables

x= "Emiliano Jimenez"
x= 4
x= 5.76
print (x) #toma el ultimo valor

x= int(3) #guardar un TIPO de dato especifico
y= float (3)
z= str (3)

print(x,y,z)
print(type (x)) #type = ultimo tipo de la cadena
print(type (y))
print(type (z))

#4. solicitud de datos 

a= input("introduce cualquier dato: ")
b= int(input("introduce un numero entero: "))
c= float(input("introduce un numero decimal: "))

print(a,b,c)

#5. boolean, comparacion y logicos

print(10 > 9) # mayor que
print(10 < 9) # menor que
print(10 == 9) # igual a
print(10 >= 9) # mayor o igual
print(10 <= 9) # menor o igual
print(10 != 9) # diferente de

x= 1
print(x<5 and x<10) #comparacion and
print(x<5 or x<10) #comparacion or
print(not(x<5 and x<10)) #comparacion not (and invertida)