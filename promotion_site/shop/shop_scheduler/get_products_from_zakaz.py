from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from shop.models import Product

links = [
    'https://.zakaz.ua/uk/promotions/?category_id=drinks',
    'https://.zakaz.ua/uk/promotions/?category_id=eighteen-plus',
    'https://.zakaz.ua/uk/promotions/?category_id=meat-fish-poultry',
    'https://.zakaz.ua/uk/promotions/?category_id=dairy-and-eggs',
    'https://.zakaz.ua/uk/promotions/?category_id=fruits-and-vegetables'
]
categories = ['drinks', 'alcohol', 'meat', 'milk', 'fruits']

shops = ["novus", "megamarket", 'varus', 'auchan', 'eko']

SILPO = {
    'https://shop.silpo.ua/all-offers?filter_CATEGORY=(22)': 'alcohol',
    # 'https://shop.silpo.ua/all-offers?filter_CATEGORY=(316__277)': 'meat',
    # 'https://shop.silpo.ua/all-offers?filter_CATEGORY=(130)': 'sauce'
}


def parse_zakaz(url):
    names, new_prices, old_prices, discount, weight, date = list(), list(), list(), list(), list(), list()
    count = 2
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(1)
        while True:
            time.sleep(0.5)
            try:
                driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div[1]/div/div/button[2]').click()
                time.sleep(0.5)
            except:
                print('Button not found')
            find_names = driver.find_elements(By.CLASS_NAME, "ProductTile__title")
            find_old_price = driver.find_elements(By.CLASS_NAME, "ProductTile__oldPrice")
            find_new_price = driver.find_elements(By.CLASS_NAME, "Price__value_discount")
            find_discount = driver.find_elements(By.CLASS_NAME, "Badge__text")
            find_weight = driver.find_elements(By.CLASS_NAME, "ProductTile__weight")
            find_date = driver.find_elements(By.CLASS_NAME, "DiscountDisclaimer_productTile")
            time.sleep(0.5)
            for i in range(len(find_names)):
                names.append(find_names[i].text)
                new_prices.append(find_new_price[i].text)
                old_prices.append(find_old_price[i].text)
                discount.append(find_discount[i].text)
                weight.append(find_weight[i].text)
                date.append(find_date[i].text)

            find_button = driver.find_element(By.LINK_TEXT, f'{str(count)}')
            find_button.click()
            time.sleep(1)
            count += 1
            if find_button:
                continue
            if not find_button:
                break

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        return names, new_prices, old_prices, discount, weight, date


def main_parse():
    Product.objects.all().delete()  # clear table

    # Zakaz
    for shop in range(len(shops)):  # insert new data into table
        for j in range(len(links)):
            link = links[j][:8] + shops[shop] + links[j][8:]
            product_data = parse_zakaz(link)
            for i in range(len(product_data[0])):
                product = Product.objects.create(
                    name=product_data[0][i],
                    old_price=product_data[2][i],
                    new_price=product_data[1][i],
                    percent_of_sale=product_data[3][i],
                    date_of_end=product_data[5][i],
                    category=categories[j],
                    shop_name=shops[shop])
                product.save()
