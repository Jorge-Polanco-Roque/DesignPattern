# ✅ *args (argumentos posicionales variables): Se usa para pasar una cantidad indefinida de argumentos posicionales, que se reciben como una tupla.
def sumar(*args):
    print(args)  # muestra los valores como tupla
    return sum(args)

print(sumar(1, 2, 3))         # 6
print(sumar(5, 10, 15, 20))   # 50


# ✅ **kwargs (argumentos nombrados variables): Se usa para pasar una cantidad indefinida de argumentos con nombre (keyword arguments), que se reciben como un diccionario.
def saludar(**kwargs):
    print(kwargs)  # muestra los pares clave-valor
    for clave, valor in kwargs.items():
        print(f"{clave} => {valor}")

saludar(nombre="Ana", edad=30, ciudad="Madrid")


# ✅ Combinando *args y **kwargs
def ejemplo(a, *args, **kwargs):
    print(f"a = {a}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

ejemplo(1, 2, 3, x=10, y=20)
