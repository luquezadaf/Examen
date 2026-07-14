import validaciones as vld
def main():
    diccionario_arreglo = []
    diccionario_bodega = []

    while True:
        vld.leer_opcion()
        opcion = vld.solicitar_opcion()

    if opcion == 1:
        vld.solicitar_arreglo()
    elif opcion == 2:
        minimo = float("Ingrese precio minimo")
        maximo = float("Ingrese precio máximo")
        vld.busqueda_arreglos(diccionario_arreglo)
        if posicion != -1:
    elif opcion == 3:
        codigoo = input("Ingrese el codigo del arreglo")
        vld.actualizar_precios(diccionario_arreglo)
        if codigoo != -1:
            respuesta = input("¿Desea actualizar otro precio (s/n)").lower()
                if respuesta == "s":
                    return
                else:
                    return -1
    elif opcion == 4:
        vld.agregar_arreglo(diccionario_arreglo)
    elif opcion == 5:
        vld.eliminar_arreglo(diccionario_arreglo)
    else:
        print("Programa finalizado")
        break
if __name__ = "__main__":
    main()