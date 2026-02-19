import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, limite):
    cliente = Socrata("www.datos.gov.co", None)

    resultados = cliente.get(
        "gt2j-8ykr",
        departamento_nom=departamento.upper(),
        limit=limite
    )

    df = pd.DataFrame.from_records(resultados)

    if df.empty:
        return df

    columnas = [
        "ciudad_municipio_nom",
        "departamento_nom",
        "edad",
        "tipo",
        "estado",
        "pais_viajo_1_nom"
    ]

    for col in columnas:
        if col not in df.columns:
            df[col] = "N/A"

    df = df[columnas]
    df = df.fillna("N/A")

    return df





