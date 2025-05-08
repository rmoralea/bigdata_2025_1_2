from dataweb import DataWeb
from database import DataBase
import pandas as pd



def main():
    df = pd.DataFrame()
    dataweb = DataWeb()
    database = DataBase()
    df = dataweb.obtener_datos()
    df = dataweb.convertir_numericos(df)
    print("*************** impresion de los datos obtenidos ************************")
    print(df.shape)
    print(df.head())
    df.to_csv("src/edu_bigdata/static/csv/data_web.csv", index=False) #/workspaces/bigdata_2025_1_2/src/edu_bigdata/static/csv
    database.close_database()


if __name__ == "__main__":
    main()