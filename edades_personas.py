# Lista de nombres
personas = ["Ana", "Luis", "Carlos", "Maria", "Pedro"]

# Diccionario con edades
edades = {
    "Ana": 30,
    "Luis": 25,
    "Carlos": 40,
    "Maria": 28,
    "Pedro": 35
}
# Diccionario con profesiones de cada persona 
profesiones = {
    "Ana": "ingeniera",
    "Luis": "médico",
    "Carlos": "profesor",
    "Maria": "diseñadora",
    "Pedro": "abogado"
}

# Solicitar nombre al usuario
nombre = input("Ingresa un nombre: ")

# Mostrar informacion extendida si el nombre existe
if nombre in edades:
    print(nombre, "tiene", edades[nombre], "años y trabaja como", profesiones[nombre] + ".")
else:
    print("La persona no fue encontrada.")
    
    
