# primera prueba


# cadena1="soy la primera cadena"
# print(cadena1)
# cadena1_matuscula=cadena1.upper()
# print(cadena1_matuscula)
# cadena1_minuscula=cadena1.lower()
# print(cadena1_minuscula)
# cadena1_titulo=cadena1.title()
# print(cadena1_titulo)
# cadena1_PARRAFO=cadena1.capitalize()
# print(cadena1_PARRAFO)
#========================================================
#=========================================================
# cadena1="soy la primera cadena"
# print(cadena1.count("a")) #cuantas a hay en el stream
# print(cadena1.find("a")) #busca la pocisión del a
# print(cadena1.rfind("a")) #busca la pocisión del a de derecha a izquierda
#========================================================
#=========================================================
# cadena2="segunda cadena al rescate"
# lista=cadena2.split()# hace esta lista ['segunda', 'cadena', 'al', 'rescate']
# print(lista)
# lista2=cadena2.split("a")#  separa por "a" ['segund', ' c', 'den', ' ', 'l resc', 'te']
# print(lista2)
# lista3=cadena2.split("a ")#  separa por "a " ['segund', 'caden', 'al rescate']
# print(lista3)

#========================================================
#=========================================================
# lista=['segunda', 'cadena', 'al', 'rescate']
# cadena=" ".join(lista)# me genera un arreglo uniendo los elementos de la lista con " ": segunda cadena al rescate
# print(cadena)
# cadena1="----???===== ".join(lista)# me genera un arreglo uniendo los elementos de la lista con "----???===== ": segunda----???===== cadena----???===== al----???===== rescate
# print(cadena1)

# password=input("ingrese pw")
# print(password.strip())
# print(password)


# repetida="cadena pepito cadena cadena cadena"
# modificada=repetida.replace("cadena","otra")
# print(modificada)
# lista=['segunda', 'cadena', 'al', 'rescate']

# lista2=lista+[1,2,3]
# print(lista2)

# lista.extend([2,3,4])
# print(lista)

# lista=['segunda', 'cadena', 'al', 'rescate']
# lista.insert(0,"pepito") #en la poscicon 0 inserte pepito
# print(lista)

# lista=['segunda', 'cadena', 'al', 'rescate']
# lista.reverse() #reversa de lista
# print(lista)

# lista=[5,1,2,8,5,3,9,7,1]
# lista.sort(reverse=True) # ordena la lista
# print(lista)

### Funciones diccionarios

# auto={"motor":"v8","color":"negro","vidrios":(6,'blidados'),"pasajeros":4}
# print(auto.keys())
# print(auto.values())
# print(auto.items())





### funciones conjuntos

# conjunto1={1,"valor1",(1,True)}
# iterable1=(1,"valor1",(1,True),45)
# print(conjunto1.issubset(iterable1))
# print(conjunto1.issuperset(iterable1))

# print(conjunto1.union(iterable1))

# print(conjunto1.difference(iterable1))
# print(conjunto1.intersection(iterable1))
conjunto1={1,"valor1",(1,True)}
iterable1=(1,"valor2",(1,True),45)
conjunto1.intersection_update(iterable1)
print(conjunto1)
