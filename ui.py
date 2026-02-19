def pedir_datos():
    print("=== CONSULTA DE CASOS COVID-19 EN COLOMBIA ===")

    departamento = input("Ingrese el nombre del departamento: ").strip()

    if departamento == "":
        print("El departamento no puede estar vacío")
        return None, None

    try:
        limite = int(input("Ingrese el número de registros: "))
        if limite <= 0:
            print("El número de registros debe ser mayor que cero")
            return None, None
    except ValueError:
        print("Debe ingresar un número válido")
        return None, None

    return departamento, limite


def mostrar_datos(df):
    if df is None:
        return

    if df.empty:
        print("\nNo se encontraron datos para la consulta\n")
        return

    print("\nRESULTADOS:\n")

    encabezado = "{:<25} {:<15} {:<5} {:<15} {:<12} {:<15}".format(
        "CIUDAD", "DEPARTAMENTO", "EDAD", "TIPO", "ESTADO", "PAIS"
    )

    print(encabezado)
    print("-" * len(encabezado))

    for _, fila in df.iterrows():
        print("{:<25} {:<15} {:<5} {:<15} {:<12} {:<15}".format(
            str(fila["ciudad_municipio_nom"]),
            str(fila["departamento_nom"]),
            str(fila["edad"]),
            str(fila["tipo"]),
            str(fila["estado"]),
            str(fila["pais_viajo_1_nom"])
        ))

    print("\nTotal de registros mostrados:", len(df), "\n")

