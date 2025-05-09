from dataweb import DataWeb
from database import DataBase
import pandas as pd



def main():
    df = pd.DataFrame()
    dataweb = DataWeb()
    database = DataBase()
    df = dataweb.obtener_datos()
    df = dataweb.convertir_numericos(df)
    print("*************** imprecion de los datos obtenidos ************************")
    print(df.shape)
    print(df.head())
    df.to_csv("src/edu_bigdata/static/csv/data_web.csv", index=False) #/workspaces/bigdata_2025_1_2/src/edu_bigdata/static/csv
    nombre_tabla = "dolar_analisis"
    database.insert_data(df,nombre_tabla)
    print("*************** Insertar los datos obtenidos en la base datos tabla: {}*********".format(nombre_tabla))
    print(df.shape)
    print(df.head())
    df_2 = database.read_data(nombre_tabla)
    print(df_2.shape)
    print(df_2.head())


if __name__ == "__main__":
    main()