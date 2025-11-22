"""""Se itera la lista para comparar el nombre que se ingresa, saber si esta en lista o no
si no se encuentra en la lista, se gurda con los datos sugeridos"""

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto si no existe.
    Retorna: (éxito: bool, mensaje: str)
    """
    # Validación
    if not nombre or precio < 0 or cantidad < 0:
        return False, " Datos inválidos"
    
    # Buscar duplicado
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return False, f"  El producto '{nombre}' ya existe. Use actualizar."
    
    # Agregar
    inventario.append({
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    })
    return True, f" Producto '{nombre}' agregado."

""""Se itera la lista para imprimir cada producto de la lista"""
def mostrar_inventario(inventario):
    """Retorna string formateado para imprimir"""
    if not inventario:
        return " Inventario vacío"
    
    texto = "\n" + "="*50 + "\nINVENTARIO\n" + "="*50 + "\n"
    for i, productos in enumerate(inventario, 1):
        # CORRECCIÓN: usa comillas simples dentro de f-string
        texto += f"{i}. {productos['nombre']:<20} | ${productos['precio']:>7.2f} | Cant: {productos['cantidad']}\n"
    return texto


""""S itera la lista, para encontrar en nombre del produnto"""
def buscar_producto(inventario, nombre):
    """
    Retorna el producto (dict) o None
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            #  CORRECCIÓN: RETORNA EL PRODUCTO, NO PRINT()
            return producto
    return None


"""primero se pregunta por el producto, si se encuentra, mostrar un submenu,
 donde le muestre que es lo que quiere modificar del producto"""
def actualizar_producto(inventario, nombre):
    """
    Actualiza un producto con submenú interactivo.
    Retorna: (hubo_cambios: bool, mensaje: str)
    """
    #  CORRECCIÓN: Llama a buscar_producto correctamente
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        return False, f" Producto '{nombre}' no encontrado."
    
    print("="*50)
    print("Producto encontrado")
    print("="*50)
    print(f"Producto: {producto['nombre']} | ${producto['precio']} | Cant: {producto['cantidad']}")

    cambios = False

    while True:
        print("\n--- Menú de Actualización ---")
        print("1. Cambiar Nombre")
        print("2. Cambiar Precio")
        print("3. Cambiar Cantidad")
        print("4. Guardar y Salir")
        print("5. Cancelar")

        try:
            opcion = int(input("\nIngresa una opción: "))
        except:
            print(" Opción inválida")
            continue

        if opcion == 1:
            nuevo_nombre = input("Ingresa un nuevo nombre: ").strip()
            if not nuevo_nombre:
                print(" Error, nombre no puede estar vacio")
                continue

            # Verificar que no exista otro producto con ese nombre
            for p in inventario:
                if p["nombre"].lower() == nuevo_nombre.lower() and p != producto:
                    print(f"  Ya existe un producto llamado {nuevo_nombre}")
                    break
            else:
                producto["nombre"] = nuevo_nombre
                cambios = True
                print(f" Nombre actualizado a: {nuevo_nombre}")

        elif opcion == 2:
            try:
                nuevo_precio = float(input("Ingresa el nuevo precio: "))
                if nuevo_precio < 0:
                    print(" Error, el precio no puede ser menor a 0")
                    continue
                producto["precio"] = nuevo_precio
                cambios = True
                print(f" Precio actualizado a: {nuevo_precio}")
            except ValueError:
                print(" Error, debe ingresar un numero valido")

        elif opcion == 3:
            try:
                nueva_cantidad = int(input("Ingresa nueva cantidad: "))
                if nueva_cantidad < 0:
                    print(" Error, ingresa una cantidad valida")
                    continue
                producto["cantidad"] = nueva_cantidad
                cambios = True
                print(f"✅ Cantidad actualizada a: {nueva_cantidad}")
            except ValueError:
                print(" Ingresa un numero valido")

        elif opcion == 4:
            if cambios:
                return True, " Cambios guardados en memoria. Volviendo al menú principal..."
            else:
                return False, " No se realizaron cambios. Volviendo al menú principal..."
        
        elif opcion == 5:
            if cambios:
                respuesta = input("Hay cambios sin guardar. ¿Descartar cambios? (s/n): ").lower()
                if respuesta == 's':
                    return False, "  Cambios descartados. Volviendo al menú principal..."
                else:
                    print(" Volviendo al submenú...")
                    continue
            else:
                return False, "  Operación cancelada."
        
        else:
            print(" Opción inválida. Por favor elija 1-5.")

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto por nombre.
    Retorna: (éxito: bool, mensaje: str)
    """
    for i, producto in enumerate(inventario):
        if producto["nombre"].lower() == nombre.lower():
            inventario.pop(i)
            return True, f" Producto '{nombre}' eliminado."
    return False, f" Producto '{nombre}' no encontrado."

def calcular_estadisticas(inventario):
    """
    Retorna estadísticas con formato:
    - unidades_totales
    - valor_total
    - producto_mas_caro (dict con nombre y precio)
    - producto_mayor_stock (dict con nombre y cantidad)
    - Usa lambda opcional para subtotal
    """
    if not inventario:
        return None
    
    #  Lambda opcional para calcular subtotal de cada producto
    subtotal = lambda p: p["precio"] * p["cantidad"]
    
    # 1. Unidades totales
    unidades_totales = sum(p["cantidad"] for p in inventario)
    
    # 2. Valor total del inventario (usando la lambda)
    valor_total = sum(subtotal(p) for p in inventario)
    
    # 3. Producto más caro (nombre y precio)
    producto_caro = max(inventario, key=lambda p: p["precio"])
    producto_mas_caro = {
        "nombre": producto_caro["nombre"],
        "precio": producto_caro["precio"]
    }
    
    # 4. Producto con mayor stock (nombre y cantidad)
    producto_stock = max(inventario, key=lambda p: p["cantidad"])
    producto_mayor_stock = {
        "nombre": producto_stock["nombre"],
        "cantidad": producto_stock["cantidad"]
    }
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }