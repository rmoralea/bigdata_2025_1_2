import os
import datetime
import sqlite3
import pandas as pd


class DataBase:
    def __init__(self):
        self.db_name = "src/edu_bigdata/static/db/dolar_analisis.sqlite" #/workspaces/bigdata_2025_1_2/src/edu_bigdata/static/db


    # CRUD C = create(insert) R= read U = update DF= Delete
    def insert_data(self,df = pd.DataFrame(),nom_table="dolar_analisis"):
        try:
            df = df.copy()
            conn = sqlite3.connect(self.db_name)
            df.to_sql(name=nom_table,con=conn,if_exists='replace') # sobreescriba , inserte al final, actualizacion datos
            conn.close()
        except Exception as errores:
            print("error al guradar los datos")
    
    def read_data(self,nom_table=""):
        df=pd.DataFrame()
        try:
            if len(nom_table)>0:
                conn = sqlite3.connect(self.db_name)
                query= "select * from {}".format(nom_table)
                df = pd.read_sql_query(sql=query,con=conn)
                print("*************** consulta base datos tabla: {}*********".format(query))
                conn.close
                return df
        except Exception as errores:
            print("error al obtener los datos")
            return df