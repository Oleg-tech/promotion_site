import os
import shutil
from time import time

categories = {
    'drinks': [
        ['varus', 'https://varus.zakaz.ua/uk/promotions/?category_id=drinks-varus&page='],
        ['novus', 'https://novus.zakaz.ua/uk/promotions/?category_id=drinks&page='],
        ['megamarket', 'https://megamarket.zakaz.ua/uk/promotions/?category_id=drinks-megamarket&page='],
        ['eko', 'https://eko.zakaz.ua/uk/promotions/?category_id=drinks-ekomarket&page='],
        ['auchan', 'https://auchan.zakaz.ua/uk/promotions/?category_id=drinks-auchan']
    ],
    'alcohol': [
        ['varus', 'https://varus.zakaz.ua/uk/promotions/?category_id=alcohol-varus&page='],
        ['novus', 'https://novus.zakaz.ua/uk/promotions/?category_id=eighteen-plus&page='],
        ['megamarket', 'https://megamarket.zakaz.ua/uk/promotions/?category_id=alcohol-megamarket&page='],
        ['eko', 'https://eko.zakaz.ua/uk/promotions/?category_id=alcohol-ekomarket&page='],
        ['auchan', 'https://auchan.zakaz.ua/uk/promotions/?category_id=eighteen-plus-auchan&page=']
    ]
}

# photo_id = 0
errors = list()


def time_counter(func):
    def wrapper():
        start = time()
        func()
        send_report(time() - start)
    return wrapper


# def get_photo_id():
#     return photo_id
#
#
# def set_photo_id():
#     global photo_id
#     photo_id += 1
#
#
# def set_null_photo_id():
#     global photo_id
#     photo_id = 0


def remove_from_folder():   # clear folder with images
    folder = 'shop/static/products'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as ex:
            print('Failed to delete %s. Reason: %s' % (file_path, ex))


def collect_errors(url, ex):
    global errors
    buf = url[8:]
    errors.append(buf[:buf.find('.zakaz')])
    print(url, ex)


def send_report(time_of_work):
    global errors
    if len(errors) == 0:
        print(time_of_work)
    else:
        pass
