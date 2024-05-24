# def resta(num1,num2):
#     return num1-num2

# print(resta(1,2))
# print(resta(num2=1,num1=2))
# def saludo():
#     print(variable_prueba)
    
# variable_prueba="pepe"
# saludo()



# def saludo():
#     variable_prueba="otro gato"
#     print(variable_prueba)
    
# variable_prueba="pepe"
# print(variable_prueba)
# saludo()
# print(variable_prueba)
# def suma(*args):
#     suma=0
#     for valor in args:
#         suma+=valor
#     return suma
# print(suma(1,2,3,4))
        
def mostrar(**kargs):
    print(kargs)
    for llave, valor in kargs.items():
        print(f'Llave: {llave}   Valor:  {valor}')
        
mostrar(nombre="juan",apellido="perez")
        