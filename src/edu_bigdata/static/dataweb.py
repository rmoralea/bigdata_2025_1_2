import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime



class DataWeb:
    def __init__(self):
        self.url = "https://es.finance.yahoo.com/quote/DOPUSD%3DX/history/?frequency=1mo"
    

    def obtener_datos(self):
        try:
            # url , cabeceras
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }
            respuesta = requests.get(self.url,headers=headers)
            if respuesta.status_code != 200:
                print("La url saco error, no respondio o no existe")
            #print(respuesta.text)
            soup = BeautifulSoup(respuesta.text,'html.parser')
            tabla = soup.select_one('div[data-testid="history-table"] table')
            nombre_columnas = [th.get_text(strip=True) for th in tabla.thead.find_all('th')]
            filas = []
            for tr in tabla.tbody.find_all('tr'):
                columnas = [ td.get_text(strip=True) for td in tr.find_all('td')]
                if len(columnas) == len(nombre_columnas):
                    filas.append(columnas)
            df = pd.DataFrame(filas,columns=nombre_columnas).rename(columns = {
                'Fecha': 'fecha',
                'Abrir': 'abrir',
                'Máx.': 'max',
                'Mín.': 'min',
                'CerrarPrecio de cierre ajustado para splits.': 'cerrar',
                'Cierre ajustadoPrecio de cierre ajustado para splits y distribuciones de dividendos o plusvalías.': 'cierre_ajustado',
                'Volumen':'volumen'
            })
            df = self.convertir_numericos(df)
            #df.to_excel("dataweb_limpio.xlsx")
            # print(nombre_columnas)
            # print(filas)
            # for th in tabla.thead.find_all('th'):
            #     th_data = th.get_text(strip=True)
# ['Fecha', 'Abrir', 'Máx.', 'Mín.', 'CerrarPrecio de cierre ajustado para splits.', 'Cierre ajustadoPrecio de cierre ajustado para splits y distribuciones de dividendos o plusvalías.', 'Volumen']

            return df
        except Exception as err:
            print("Error en la funcion obtener_datos")
            df = pd.DataFrame()
            return df


    def convertir_numericos(self,df=pd.DataFrame()):
        df= df.copy()
        if len(df)>0:
            #for col in (df.columns):
            for col in ('abrir',	'max',	'min',	'cerrar',	'cierre_ajustado',	'volumen'):
                df[col] = (df[col]
                           .str.replace(r"\.","",regex=True)
                           .str.replace(",",'.'))

        return df


# dw = DataWeb()
# dw.obtener_datos()
# #print(dw.url)

# nom_columas = ["kjakl","kjkhasd","jklhasd"]
# columna =     [4654,    6456,     465456]
# fila =       [[4654,    6456,     465456],[4654,    6456,     465456],[4654,    6456,     465456]]