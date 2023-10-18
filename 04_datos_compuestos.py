# =========== Listas ===========
lista = ["pan", "azucar", "té", "café", 1.73, True]
print(lista)    # ['pan', 'azucar', 'té', 'café', 1.73, True]
print(lista[1]) # azucar

# =========== Tuplas ===========
tupla = ("pan", "azucar", "té", "café", 1.73, True)
print(tupla)    # ('pan', 'azucar', 'té', 'café', 1.73, True)
print(tupla[1]) # azucar

# La diferencia entre listas y tuplas esta en que la tupla no se puede modificar
lista[1] = "sal"
print(lista)        # ['pan', 'sal', 'té', 'café', 1.73, True]
# tupla[1] = "sal"    # Error

# =========== Conjunto set ===========
# No se pueden modificar conjunto[1] = "sal" ¡No!
# No se puede acceder mediante índice conjunto[1] ¡No!
# No me permite tener elementos repetidos
conjunto = {"pan", "azucar", "té"}
print(conjunto)     # {'azucar', 'té', 'pan'}
conjunto = {"pan", "azucar", "té", "azucar"}
print(conjunto)     # {'azucar', 'té', 'pan'}

# =========== Diccionario ===========
# Su estructura es key : value y separado con comas
diccionario = {
    "nombre": "Marco",
    "apellido": "Valencia",
    "altura": 1.73, 
    "dato_duplicado": "Marco"
}

print(diccionario["nombre"])    # Marco