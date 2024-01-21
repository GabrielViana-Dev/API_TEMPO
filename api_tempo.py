import requests

def query(city):
    API_KEY = "886705b4c1182eb1c69f28eb8c520e20"

    link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br'

    data = requests.get(link)

    data_dict = data.json()

    return data_dict
