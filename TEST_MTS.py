from bs4 import BeautifulSoup 
from googletrans import Translator
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import re
import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r'./chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument("window-size=1400,800")
driver = webdriver.Chrome(service=service, options=options)

# Конект селениумом
# def connect(url="URL"):
#     try:
#         driver.get(url)
#         time.sleep(random.randint(1,15))
#     except TimeoutException:
#         print('new connection try')
#         driver.get(url)
#         time.sleep(5)
#     print(driver)
#     return driver

# # Нажатие каптчи    
# def click_and_release():
#     element = driver.find_element(By.XPATH,'//*[@id="checkbox-captcha-form"]/div[3]/div/div/div[1]')
#     actions = ActionChains(driver)
#     actions.move_to_element(element).perform()
#     actions.click_and_hold().release().perform()

# # Перевод названия    
# def translete(word_rus,word_en=""):
#     translator = Translator()
#     try:
#         if word_en:
#             return word_en.text
#         else:
#             name_tr=translator.translate(word_rus, dest='en')
#             return name_tr.text
#     except:
#         translete(word_rus,word_en)

# # Парсинг страницы и занисение в словарь
# table={}        
# def parsing(page):

#     # for page in range(start,end):
#     url ="https://www.kinopoisk.ru/lists/movies/popular/?page="+str(page)
#     print("Страница "+ str(page))
#     response = connect(url)
#     bs = BeautifulSoup(response.page_source,"html.parser")
#     if bs.find_all(class_="CheckboxCaptcha"):
#         click_and_release()
#         time.sleep(2)
#         parsing(page)
#     else:
#         row_bs=bs.find_all(class_='styles_root__ti07r')
#         for element in row_bs:
#             number=(element.find('span', class_= 'styles_position__TDe4E').text)
#             table[number]={}
#             print(element.find('span', class_= 'styles_position__TDe4E').text)
#             name_rus=element.find('span', class_= 'styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
#             table[number]['Name in Russian']=name_rus
#             name_en=element.find('span', class_='desktop-list-main-info_secondaryTitle__ighTt')
#             table[number]['Name in English']=translete(name_rus,name_en)
#             year_list=element.find('span',class_='desktop-list-main-info_secondaryText__M_aus')
#             if year_list:
#                 year_release=re.search('\d\d\d\d', year_list.text)
#                 if year_release:
#                     table[number]['Year of release']=year_release[0]
#             else:
#                 table[number]['Year of release']="Не известно"
#             element1=element.find('span', class_=re.compile('^styles_kinopoiskValue')) 
#             if element1:
#                 table[number]['Kinopoisk rating']=element1.text
#             else:
#                 table[number]['Kinopoisk rating']='без рейтинга'

# # Проход по страницам             
# for i in range(1,21):
#     parsing(i)

# # Запись в таблицу
# sorted_dict = dict(sorted(table.items(), key=lambda x: int(x[0])))
# df = pd.DataFrame.from_dict(sorted_dict, orient='index')
# df = df.reset_index()
# df = df.rename(columns={'index': 'Number'})
# df.to_markdown(r'C:\Users\tolok\Desktop\тест\mts\tabl_rating_kp.md', index=False)

help('modules')




