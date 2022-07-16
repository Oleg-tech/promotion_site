from apscheduler.schedulers.background import BackgroundScheduler

from shop.shop_scheduler.get_products_from_zakaz import main_parse


def start():
    scheduler = BackgroundScheduler(timezone="Europe/Berlin")
    scheduler.add_job(main_parse, 'cron', hour='12', minute='31')
    scheduler.start()
