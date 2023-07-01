import requests
import pandas as pd

def geocode(address, api_key):
    url = 'https://geocode-maps.yandex.ru/1.x/'
    params = {
        'apikey': api_key,
        'geocode': address,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        json_data = response.json()
        coordinates_str = json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coordinates = tuple(map(float, coordinates_str.split()))
        return coordinates
    else:
        raise Exception('Ошибка при запросе к API Yandex Maps')

def geocode_for_pandas(row):
    api_key = '49044012-cd97-4353-88d8-e6e165f407ea'
    print(row["id"])
    return geocode(row["Адрес"], api_key)

df = pd.read_excel("musei.xlsx")

df["Координаты"] = df.apply(geocode_for_pandas, axis=1)
print((df.head()))
df.to_excel("new_musei_2.xlsx")

