from bs4 import BeautifulSoup
import requests
requests.packages.urllib3.disable_warnings()

def _ensure_200_response(url: str) -> requests.Response:
    response = requests.get(url, verify=False)
    response.raise_for_status()

    return response


class ExtraerTasaBCV:
    def __init__(self):
        pass
    
    def hoy(self):
        try:
            response = _ensure_200_response('https://www.bcv.org.ve/')
            soup = BeautifulSoup(response.content, "html.parser")

            forma_tipo_de_cambio = soup.find("div", "view-tipo-de-cambio-oficial-del-bcv")
            
            self.apartado = forma_tipo_de_cambio.find(id='dolar').find("strong")
            
            valor = (str(self.apartado)).split(' ')
            return f'{valor[1][:-9]}.{valor[1][3:-4]}' 
        except:
            return "Ocurrio un error con la web del bcv"

        