import requests
import json
from bs4 import BeautifulSoup

from shop.models import Product
from shop.shop_scheduler.config import *
from shop.shop_scheduler.get_json import get_file


def insert_into_table(name, old_price, new_price, picture, discount, date, category, country, shop_name):
    product = Product.objects.create(
        name=name, old_price=old_price, new_price=new_price, picture=picture, percent_of_sale=discount,
        date_of_end=date, category=category, country=country, shop_name=shop_name)
    product.save()


def split_json():
    get_file()
    with open('shop/static/json/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    items = data['items']

    for item in items:
        if not item['storeQuantity']:
            continue
        # print(item['slug'])
        discount = None
        slug = item['slug']

        if item['promoId'] == 'melkoopt':
            old_price = item['price']
            new_price = list(filter(lambda item: item['Type'] == 'specialPrice', item['prices']))[0]['Value']
            discount = item['promotions'][0]['description']
        else:
            new_price = item['price']
            old_price = item['oldPrice']
            discount = round((old_price - new_price) * (100.0 / old_price))

        country = list(filter(lambda item: item['key'] == 'country', item['parameters']))[0]['value']

        insert_into_table(
            item['name'], old_price, new_price, item['mainImage'], discount,
            item['promotion']['stopAfter'], 'None', country, 'silpo'
        )


def parse_zakaz(url, name_of_shop, cat):
    page_count = 1
    while True:
        request = requests.get(url+str(page_count))
        print(url + str(page_count))
        page_count += 1
        if BeautifulSoup(request.text, 'html.parser').find("div", class_="ProductsBox") != None:    # check if link is actual
            try:
                soup = BeautifulSoup(request.text, 'html.parser')
                new_url = soup.find_all('a', class_="ProductTile", href=True)                       # find all products
                for i in new_url:

                    # with open(f'media/images/{str(get_photo_id())}.jpg', 'wb') as file:        # save image
                    #     res = requests.get(i.find('img', {'loading': 'lazy'})['src'])               # find image
                    #     file.write(res.content)
                    # set_photo_id()

                    # for checking every product in detail
                    new_request = requests.get('https://'+name_of_shop+'.zakaz.ua/'+i['href'])
                    new_soup = BeautifulSoup(new_request.text, 'html.parser')

                    def get_country():
                        if new_soup.find('li', {'data-marker': 'Taxon country'}):                   # find country
                            return new_soup.find('li', {'data-marker': 'Taxon country'}).text.replace("Країна", "")
                        else:
                            return ''

                    insert_into_table(
                        new_soup.find('h1', class_="BigProductCardTopInfo__title").text,
                        i.find('span', class_='Price__value_minor').text,
                        i.find('span', class_='Price__value_discount').text,
                        # f'images/{str(get_photo_id()-1)}.jpg',
                        i.find('img', {'loading': 'lazy'})['src'],
                        i.find('div', class_='ProductTile__badges').text,
                        i.find('span', class_='DiscountDisclaimer').text, cat, get_country(), name_of_shop)
            except Exception as ex:
                collect_errors(url, ex)
                print('Error')
        else:
            break


@time_counter
def main_parse():
    # set_null_photo_id()
    Product.objects.all().delete()  # clear table
    remove_from_folder()    # delete all product photos

    # Silpo
    split_json()

    # Zakaz
    for cat in categories.keys():
        for shop in range(len(categories[cat])):
            parse_zakaz(categories[cat][shop][1], categories[cat][shop][0], cat)
