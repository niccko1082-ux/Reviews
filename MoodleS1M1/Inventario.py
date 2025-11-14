
while True: #genera un bucle hasta cumplir la informacio.
    try: 
            #Ingresar datos  del producto. nombre, precio, cantidad
            nombre = str(input("Ingresa el mombre del producto: "))
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("ingresa la cantida del producto: "))
            break #Si los datos son correctos salta a la linea 12
    except ValueError:
        print("El tipo de dato ingresado es incorrecto")  #Este mensaje se muestra si el tipo de dato es incorrecto

costo_total = precio * cantidad #se calcula es el costo teniendo en cuenta el precio y la cantidad de producto

#Muestra en consola los datos ingresados nombre,precio, cantidad. Y muesta el costo total
print(f"Nombre del producto: {nombre}")
print(f"Precio por unidad: {precio}")
print(f"Cantidad del producto: {cantidad}")
print(f"Costo total: {costo_total}")
