def leer_opcion():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

def solicitar_opcion():
    try:
        opcion = int(input("Ingrese una opción para continuar"))
        if 1 <= opcion <= 6
            return opcion
        else:
            print("Debe seleccionar una opción válida")
            return -1

def solicitar_codigo(codigo):
    return len(codigo.strip()) > 0
def solicitar_nombre(nombre):
    return len(nombre.strip()) > 0
def solicitar_tipo(tipo):
    return len(tipo.strip()) > 0
def solicitar_color_principal(color):
    return len(color.strip()) > 0
def solicitar_tamaño(tamano):
    try:
        valor = int(tamano)
        return tamano == "S" or tamano == "M" or tamano == "L"
    except ValueError:
        print("Error") 
def solicitar_tarjeta(tarjeta):
    try:
        valor = int(tarjeta)
        return tarjeta == "s" or tarjeta == "n"
    except ValueError:
        print("Error") 

def solicitar_temporada(temporada):
    return len(temporada.strip()) > 0
    
def solicitar_precio(precio):
        try:
            valor = int(precio)
            return 0 <= valor
        except ValueError:
            return False
def solicitar_unidades(unidades):
    try:
        valor = int(unidades)
        return 0 <= valor
    except ValueError:
        return False


def agregar_arreglo(lista_arreglo):
    cod = input("Ingrese el codigo del arreglo")
    nom = input("Ingrese el nombre del arreglo")
    tip = input("Ingrese el tipo del arreglo")
    col = input("Ingrese el color del arreglo")
    tam = input("Ingrese el tamaño del arreglo (Debe ser (S) (M) o (L))")
    tar = input("Ingrese si incluye tarjeta el arreglo (Debe ser (S) o (N))")
    temp = input("Ingrese temporada del arreglo")
    pre = input("Ingrese precio del arreglo")
    uni = input("Ingrese unidades a arreglar")

    if not solicitar_codigo(cod)
        print("Error. No vacío ni solo espacios en blanco, y que no exista ya en los diccionarios")
        return
    if not solicitar_nombre(nom)
        print("Error. No vacío ni solo espacios en blanco")
        return
    if not solicitar_tipo(tip)
        print("Error. No vacío ni solo espacios en blanco")
        return
    if not solicitar_color_principal(col)
        print("Error. No vacío ni solo espacios en blanco")
        return
    if not solicitar_tamaño(tam)
        print("Error. Debe ser exactamente 'S', 'M' o 'L'")
        return
    if not solicitar_tarjeta(tar)
        print("Error. Debe ser exactamente 'S' o 'N'")
        return
    if not solicitar_temporada(temp)
        print("Error. No vacío ni solo espacios en blanco")
        return    
    if not solicitar_precio(pre)
        print("Error. Debe ser un número mayor que cero")
        return
    if not solicitar_unidades(uni)
        print("Error. Debe ser un número entero mayor o igual a cero")
    nuevo_arreglo = {
        "codigo": cod.strip(),
        "nombre": nom.strip(),
        "tipo": tip.strip(),
        "color principal":col.strip(),
        "tamaño":input(tam),
        "incluye_tarjeta":input(tar),
        "temporada": tem.strip(),
        "precio": int(pre),
        "unidades": int(uni),
    }
    lista_arreglo.append(nuevo_arreglo)
    print("Arreglo agregado")

def solicitar_arreglo(arreglo)
    try:
        ingrese_arreglo = input("Ingrese el arreglo que desea")
        retun len(arreglo.strip()) > 0

def busqueda_arreglos(lista_arreglo,nombre_buscar)
    for i in range(len(lista_arreglo)):
        if lista_arreglo[i]["codigo"].lower() ==nombre_buscar.strip().lower()
        return i
    return -1


def actualizar_precios(lista_arreglo)
    if len(lista_arreglo) == 0:
        print("No hay precios registrados")

def eliminar_arreglo(lista_arreglo)
    eliminar = input("Ingrese el codigo a eliminar")
    posicion = localizar_arreglo(localizar_arreglo,eliminar)
    if posicion != -1:
        lista_arreglo.pop(posicion)
        print("Arreglo eliminado")
    else:
        print("El codigo no se registra")