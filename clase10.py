# def dividir(a,b):
#     try:
#         return a/b
#     except:
#         return "no se puede dividir pq el divisor no es correcto"
    
# print(dividir(5,0))


def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "no se puede dividir por cero"
    except: 
        return "pase por except"
    
print(dividir(5,'a'))    
print(dividir(5,0))

