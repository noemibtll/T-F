# Retorna el encabezado de la lista, primera posicion
# manejar el error con instrucciones
def head(lst):
    if not lst:
        raise ValueError("head: empty list")
    return lst[0]

# Test 1 -
# Resultado: 10
print(head([10, 20, 30, 40]))

# Test 2 - Error
# Raises ValueError: head: lista vacia
# print(head([]))


# Retorna el primero de la lista
-def maybe_head(lst):
    if not lst:
        return None
    return lst[0]

# Test 1 - 
# Resultado: 10
print(maybe_head([10, 20, 30, 40]))

# Test 2 - 
# Resultado: Ninguno
print(maybe_head([]))


# Division
# Maybe: representa el calculo que puede fallar en caso de que sea ninguno
def divide(x, y):
    if y == 0:
        return None
    return x // y

# Test 1 -
# Result: 2
print(divide(10, 5))

# Test 2 - 
# Result: Ninguno
print(divide(10, 0))
