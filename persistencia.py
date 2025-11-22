import csv
import os

ARCHIVO_CSV = "inventario.csv"

def crear_csv_si_no_existe():
    """Crea el archivo vacío con encabezados si no existe"""
    if not os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
            writer.writeheader()
        print(f" Archivo {ARCHIVO_CSV} creado.")

def cargar_inventario():
    """Lee CSV y retorna lista de diccionarios"""
    inventario = []
    try:
        with open(ARCHIVO_CSV, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["precio"] = float(row["precio"])
                row["cantidad"] = int(row["cantidad"])
                inventario.append(row)
        print(f"📂 Cargados {len(inventario)} productos")
    except FileNotFoundError:
        print(f" Archivo no existe. Se creará al guardar.")
    return inventario

def guardar_inventario(inventario):
    """SOBRESCRIBE el CSV con la lista actual"""
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
        writer.writeheader()
        writer.writerows(inventario)  #  Escribe todas las filas
    print(f" Guardados {len(inventario)} productos")