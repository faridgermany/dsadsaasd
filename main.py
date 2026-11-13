carta = {
    "1" {"completo italiano", 2500},
    "2" {"cazuela de puerco", 3500},
}

def formatear_precio(monto):
    return f"${monto:}".replace(",", ".")

def  mostrar_menu() :
    print("\n===================================")
    print("    RESTAURANTE EL BUEN SABOR")
    print("===================================")
    print("1. Ver carta")
    print("2. Agregar producto al pedido")
    print("3. Ver pedido")
    print("4. Calcular cuenta")
    print("5. Ver producto más caro y más barato")
    print("6. Salir")
    print("===================================")

def mostrar_carta(diccionario_dato):
    print("*****carta*****")
    for codigo, (nombre, precio) in diccionario_dato.items():
        print(f"{codigo}, {nombre} - {formatear_precio(precio)}")
        
def pedir_cantidad():
    while True:
        try:
            texto = input("ingrese cantidad\n")
        except:
            print("debes ingresar un numero entero")

def agregar_producto(diccionario,lista):
    mostrar_carta()
    codigo = input("ingrese codigo\n")
    if codigo not in diccionario:
        print("este codigo no existe en la carta")
        return
    nombre, precio = diccionario[codigo]
    cantidad=pedir_cantidad
