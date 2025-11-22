from persistencia import crear_csv_si_no_existe, cargar_inventario, guardar_inventario
from servicios import *

# Esta es la variable GLOBAL
inventario = []

def menu():
    #  DECLARAR GLOBAL PARA PODER MODIFICARLA DENTRO DE LA FUNCIÓN
    global inventario
    
    # Cargar al inicio
    crear_csv_si_no_existe()
    inventario = cargar_inventario()
    
    while True:
        print("\n---------------MENU------------")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar datos")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV (recargar)")
        print("9. Salir")

        try:
            option = int(input("Ingresa una opción: "))
        except:
            print(" Opción inválida")
            continue

        #  USAR ELIF EN LUGAR DE IF para no evaluar todas
        if option == 1:
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print(" Nombre no puede estar vacío")
                continue
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                exito, msg = agregar_producto(inventario, nombre, precio, cantidad)
                print(msg)
            except ValueError:
                print(" Precio y cantidad deben ser números válidos")
        
        elif option == 2:
            print(mostrar_inventario(inventario))
        
        elif option == 3:
            nombre = input("Nombre del producto a buscar: ").strip()
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(f"\n✓ {producto['nombre']} | ${producto['precio']} | Cant: {producto['cantidad']}")
            else:
                print(f" Producto '{nombre}' no encontrado")
        
        elif option == 4:
            nombre = input("Nombre del producto a actualizar: ").strip()
            hubo_cambios, msg = actualizar_producto(inventario, nombre)
            print(msg)
            if hubo_cambios:
                guardar_inventario(inventario)
        
        elif option == 5:
            nombre = input("Nombre del producto a eliminar: ").strip()
            exito, msg = eliminar_producto(inventario, nombre)
            print(msg)
            if exito:
                guardar_inventario(inventario)
        
        elif option == 6:
            stats = calcular_estadisticas(inventario)
            if stats:
                print("\n" + "="*50)
                print(" ESTADÍSTICAS DEL INVENTARIO")
                print("="*50)
                print(f"Unidades totales: {stats['unidades_totales']} productos")
                print(f"Valor total: ${stats['valor_total']:,.2f}")
                print("\n Producto más caro:")
                print(f"   Nombre: {stats['producto_mas_caro']['nombre']}")
                print(f"   Precio: ${stats['producto_mas_caro']['precio']:,.2f}")
                print("\n Producto con mayor stock:")
                print(f"   Nombre: {stats['producto_mayor_stock']['nombre']}")
                print(f"   Cantidad: {stats['producto_mayor_stock']['cantidad']} unidades")
                print("="*50)
            else:
                print("\n📦 Inventario vacío")
        
        elif option == 7:
            guardar_inventario(inventario)
            print(" Inventario guardado manualmente")
        
        elif option == 8:
            print("  Recargando inventario desde CSV...")
            inventario = cargar_inventario()  #  GRACIAS A 'global', esto funciona
        
        elif option == 9:
            guardar_inventario(inventario)
            print(" ¡Hasta luego!")
            break
        
        else:
            print(" Opción inválida (1-9)")

if __name__ == "__main__":
    menu()