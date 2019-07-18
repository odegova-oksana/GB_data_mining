# задание 2:
# Ресурс https://5ka.ru/special_offers/  
# Необхоидмо выгрузить все товары по акции - каждый товар в отдельный файл (csv или json),
# имя файла id товара, выгрузить необходимо абсолютно все товары по акции которые есть в источнике.

import requests, json


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


five_url = 'https://5ka.ru/special_offers/'
five_data = requests.get(five_url)

api_five='https://5ka.ru/api/v2/special_offers/?categories=&ordering=&page=5&price_promo__gte=&price_promo__lte=&records_per_page=12&search=&store='

api_five_data = requests.get(api_five)
tmp_data = api_five_data.json()

while api_five != "":
    text_all = tmp_data.get('results')
    text = json.dumps(text_all[0])
    name = '{}.json'.format(text['id'])
    create_file(name,text)
    api_five = tmp_data.get("next")


