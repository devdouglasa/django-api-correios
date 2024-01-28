import requests

class Api:
    _cep = ''

    def receber_dados(self):
        url = f"https://cep.awesomeapi.com.br/json/{self._cep}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return "Not a found!"
        