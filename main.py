from api import obtener_datos
from ui import pedir_datos, mostrar_datos

def main():
    departamento, limite = pedir_datos()

    if departamento is None:
        return

    df = obtener_datos(departamento, limite)

    mostrar_datos(df)

if __name__ == "__main__":
    main()


