import os
import requests

class Gestion_data():
    def __init__(self):
        self.carpeta = 'recursos/'
        
    def descargar_archivo(self):
        """Descarga el archivo del bcv"""
        
        url = 'https://www.bcv.org.ve/sites/default/files/indicadores_sector_externo/2_1_1_tdc.xlsx'
        
        respuesta = requests.get(url, verify=False)
        if respuesta.status_code == 200:
            with open(os.path.join(self.carpeta, 'valores.xlsx'), 'wb') as f:
                f.write(respuesta.content)
        else:
            print(f'Error al descargar el archivo: {respuesta.status_code}')


Gestion_data().descargar_archivo()

