gastos = []

def agregar_gasto():
    nombre = input("Nombre del gasto: ")
    monto = float(input("Monto del gasto: "))
    categoria = input("Categoría: ")
    gastos.append({"nombre": nombre, "monto": monto, "categoria": categoria})
    print("Gasto agregado.")


def mostrar_total():
    total = sum(gasto["monto"] for gasto in gastos)
    print(f"Total gastado: ${total:.2f}")

def categoria_mayor_gasto():
    if not gastos:
        print("No hay gastos registrados.")
        return

    categorias = {}
    for gasto in gastos:
        categoria = gasto["categoria"]
        categorias[categoria] = categorias.get(categoria, 0) + gasto["monto"]

    mayor_categoria = max(categorias, key=categorias.get)
    print(f"Categoría con mayor gasto: {mayor_categoria} (${categorias[mayor_categoria]:.2f})")



def menu():
    while True:
        print("\n--- Calculadora de Gastos ---")
        print("1. Agregar gasto")
        print("2. Ver total de gastos")
        print("3. Categoría con mayor gasto")
        print("4. Eliminar gasto")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_gasto()
        elif opcion == "2":
            mostrar_total()
        elif opcion == "3":
            categoria_mayor_gasto()
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida.")

# Ejecutar menú
menu()
