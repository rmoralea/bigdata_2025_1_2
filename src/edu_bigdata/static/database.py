import os
import datetime
import sqlite3
import pandas as pd


class DataBase:
    def __init__(self):
        self.db_name = "src/edu_bigdata/static/db/dolar_analisis.db" #/workspaces/bigdata_2025_1_2/src/edu_bigdata/static/db

        self.create_database()
    
    def create_database(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

        except Exception as err:
            print("error al crear la base de datos")
            # df.sql(self.conn,nom_table)

    def close_database(self):
        self.conn.close()