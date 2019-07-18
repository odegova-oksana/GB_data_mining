# задание 1:
# Ресурс https://icobench.com/icos 
# Необходимо выгрузить в отдельные файлы html код каждой страницы каталога ICO проектов.
# Шаблон имени файла icobench_ico_page_{номер страницы}.html

import requests

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

site_url = 'https://icobench.com/icos'

for i in range(1, 469):
    params = {"filterBonus":'on',"filterBounty":'on',"page":i}
    site_data = requests.get(site_url, params=params)
    text = site_data.text
    name = 'icobench_ico_page_{}.html'.format(i)
    create_file(name,text)