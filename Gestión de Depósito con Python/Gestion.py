'''
Gestión del Inventario de una Tienda
1-Crear un inventario inicial usando un diccionario
2-Actualizar el inventario cuando se venden un productos
3-Agregar nuevos productos al inventario
4-Mostrar un resumen del inventario
5-buscar un producto en el inventario y mostrar su cantidad disponible
6- Gestionar un ciclo de ventas, donde los clientes compran productos hasta que decidas cerrar la tienda

'''
# CREAR EL INVENTARIO INICIAL

inventario = {}

'''
"manzanas": 50, 
    "leche": 100, 
    "detergente": 30,
    "azucar": 20
'''
# CREAR FUNCIÓN PARA EL INVENTARIO

def mostrar_inventario(inventario):
    print("Inventario Actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad} unidades")
        
# LLAMAR A LA FUNCIÓN
#mostrar_inventario(inventario)

# FUNCIÓN VENDER PRODUCTO

def vender_producto(inventario):
    producto = input(f"¿Que producto quieres vender:").lower()
    cantidad = int(input(f"¿Cuantas unidades del {producto} quieres vender:"))
    
    if producto in inventario:
        if inventario[producto] >= cantidad:
            inventario[producto] -= cantidad
            print(f"Has vendido {cantidad} unidades de {producto}.")
        else:
            print(f"No hay suficientes unidades de {producto} en el inventario")
    else:
        print(f"{producto} no esta en el inventario")

# AGREGAR PRODUCTOS AL INVENTARIO

def agregar_producto(inventario):
    producto = input("Introduce el nuevo producto:").lower()
    cantidad = int(input(f"Introduce la cantidad inicial {producto}:"))
    
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print(f"Producto {producto} agregado al inventario con {cantidad} unidades.")

# BUSCAR PRODUCTO EN EL INVENTARIO
def buscar_producto(inventario):
    producto = input("Introduce el producto que deseas buscar:").lower()
    
    if producto in inventario:
        print(f"Hay {inventario[producto]} unidades de {producto}")
    else:
        print(f"{producto} no esta en el inventario")
        
# GESTION DE VENTAS

def gestion_tienda(inventario):
    while True:
        print("\n OPCIONES:")
        print("1- MOSTRAR INVENTARIO")
        print("2- VENDER PRODUCTO")
        print("3- AGREGAR PRODUCTO")
        print("4- BUSCAR PRODUCTO")
        print("5- CERRAR TIENDA\n")
    
        opcion = input("Elije una opción:")
        
        match opcion:
            case "1":
                mostrar_inventario(inventario)
            case "2":
                vender_producto(inventario)
            case "3":
                agregar_producto(inventario)
            case "4":
                buscar_producto(inventario)
            case "5":
                print("Cerrando tienda ...")
                break
            case _:
                print("Esta opción no esta en el menú")
                
gestion_tienda(inventario)                   
            