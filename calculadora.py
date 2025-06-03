gastos = []

def agregar_gasto():
    nombre = input("Nombre del gasto: ")
    monto = float(input("Monto del gasto: "))
    categoria = input("Categoría: ")
    gastos.append({"nombre": nombre, "monto": monto, "categoria": categoria})
    print("Gasto agregado.")


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
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Opción no válida.")

# Ejecutar menú
menu()
