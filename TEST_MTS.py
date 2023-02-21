from bs4 import BeautifulSoup 
from googletrans import Translator
translator = Translator()
import re
import time
import requests
import pandas as pd
from fake_useragent import UserAgent
ua= UserAgent(use_external_data=True)
ua.update()
dict={"Number": [],
    "Name in Russian": [],
    "Name in English": [],
    "Year of release": [],
    "Kinopoisk rating": []
    }

for page in range(1,21):
    url ="https://www.kinopoisk.ru/lists/movies/popular/?page="+str(page)
    print("Страница "+page)
    response = requests.get(url,headers={'User-Agent': ua.chrome})
    bs = BeautifulSoup(response.text,"lxml")
    time.sleep(60)
    row_bs=bs.find_all(class_='styles_root__ti07r')
    for element in row_bs:
        dict['Number'].append(element.find('span', class_= 'styles_position__TDe4E').text)
        print(element.find('span', class_= 'styles_position__TDe4E').text)
        name_rus=element.find('span', class_= 'styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
        dict['Name in Russian'].append(name_rus)
        name_en=element.find('span', class_='desktop-list-main-info_secondaryTitle__ighTt')
        if name_en:
            dict['Name in English'].append(name_en.text)
        else:
            name_tr=translator.translate(name_rus, dest='en')
            dict['Name in English'].append(name_tr.text)
        year_list=element.find('span',class_='desktop-list-main-info_secondaryText__M_aus').text
        year_release=re.search('\d\d\d\d', year_list)
        dict['Year of release'].append(year_release[0])
        year=element.find('span',class_='desktop-list-main-info_secondaryText__M_aus')
        element1=element.find('span', class_=re.compile('^styles_kinopoiskValue')) 
        if element1:
            dict['Kinopoisk rating'].append(element1.text)
        else:
            dict['Kinopoisk rating'].append('без рейтинга')
        
df = pd.DataFrame(dict)
df.to_markdown('./readme.md',index=False)





