import time
from selenium.webdriver import Chrome

# Создать заявку на присвоение бизнес-кода по ссылке
# http://msk-ltstst-162.msk.evraz.com/Referent/br_zayavki.nsf/CreateDocument?OpenAgent&type=3&confid=7FDD5EF49327174D43258998004ACF63
# и подставить адрес своей заявки в переменную url_invest

url_invest = "http://msk-ltstst-162.msk.evraz.com/br_x_zayavki.nsf/Document.xsp?id=7E46BFD0B83111D8432589F900276F84"

browser = Chrome()
browser.get(url_invest)
time.sleep(3)

