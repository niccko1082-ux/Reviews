# Se crea una lista vacia
inventario = []

# Se define una variable para mostrar el menu
def menu():

    
    print("1. Agregar productos")
    print("2. Motrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")

# se define una variable logica, donde se desarrollara el codigo y se agregaran otras funciones.
def logica():
    while True:
        try:
            menu = int(input("\n Ingresa una opcion "))
        except ValueError:
                print("ingresa una opcion valida")
                continue

        if menu == 1:
            nombre = input("Ingresa el nombre del producto: ")
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa cantidad de producto: "))
            agregar_productos(nombre, precio, cantidad)
        elif menu == 2:
            mostrar_inventario()
        elif menu == 3:
            estadisticas()
        elif menu == 4:
            print("Gracias por visitarnos")
            break 
        else:
            print("Nuemro no valido")
            
# Esta funcion se llama en la funcion logica, para que se ingresen los datos nombre,precio y cantidad y se guarden como diccionario dentro de la lista
# Tambien se calcula y agrega el total para utilizarlo mas adelante
def agregar_productos(producto, precio, cantidad):
        total = precio*cantidad
        inventario.append({"producto":producto, "precio":precio, "cantidad":cantidad, "total":total})
        return print("Se agrego con exito!")

# Se definen otras variables para llamar para asignarles como valor un item del diccionario
# y usarlos para mostrarlos de manera organizada
def mostrar_inventario():
    for diccionario in inventario:
        nombre = diccionario["producto"]
        precio = diccionario["precio"]
        cantidad = diccionario["cantidad"]

        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

# En estadisticas se crea un contador para que sumen los totales para luego imprimir un total general
# tambien se una len() para que cuente la cantidad de diccionarios que estan dentro de la lista inventario
def estadisticas():
    total_inventario = 0
    for diccionario in inventario:
     total_inventario += diccionario["total"]
     cantidad_total = len(inventario)
    print(f"Total de inventario: ${total_inventario:.0f}\nCantidad de productos totales: {cantidad_total} ")
    return

# Esta es la funcion que ejecuta el programa
if __name__=="__main__":
    menu()
    logica()
    
