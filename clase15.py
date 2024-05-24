# from collections import namedtuple, Counter
# instancia_de_counter=Counter("abcabdbabsbabcbaebe")
# print(instancia_de_counter)
# Pescado=namedtuple('Pescado',['b','4','7'])


#####-------------manejo de archivos--------------------
# nombre=input('nombre')

# print(nombre)
# archivo_abierto= open('archivo de prueba.txt','w')
# archivo_abierto.write(nombre)
# archivo_abierto.close
# archivo_abierto= open('archivo de prueba.txt','r')
# valor_archivo=archivo_abierto.read()
# print(valor_archivo)
# archivo_abierto.close

###############

# archivo_abierto= open('archivo de prueba.txt','r')
# valor_archivo=archivo_abierto.read()
# print(valor_archivo)
# archivo_abierto.close

#########

# archivo_abierto= open('archivo de prueba.txt','r')


# lineas=archivo_abierto.readlines()
# print(lineas)
# archivo_abierto.close

#########

# archivo_abierto= open('archivo de prueba.txt','r')
# valor_archivo=archivo_abierto.read()
# print(valor_archivo)
# archivo_abierto.close


#############Json
import json

diccionario={'a':1,'b':2,'c':True,'d':("valor",3)}
with open('archivo de no json.json','w') as archivo_abierto:
    json.dump(diccionario,archivo_abierto,indent=4)

with open('archivo de no json.json','r') as archivo_abierto:
    datos=json.load(archivo_abierto)
    print(datos)
print("###########################################")    
print(datos)