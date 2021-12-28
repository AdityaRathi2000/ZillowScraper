import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import json
import time
import urllib.request as webInfo

def link_scraper(link):
    headers = {
        'authority': 'scrapeme.live',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    list_of_url = []
    for timing in range(1,15):
        new_link = '{}/{}_p/'.format(link, timing)
        response = requests.get(new_link, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        for i in soup.find_all('li'):
            for script in i.find_all('script', text = re.compile('url')):
                if script:
                    json1 = json.loads(script.string)["url"]
                    list_of_url.append(json1)

    return set(list_of_url)

def house_scraper(zipcode, link):
    headers = {
        'authority': 'scrapeme.live',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    response = requests.get(link, headers=headers)
    soup_is = BeautifulSoup(response.content, "html.parser")

    houseprice = ""
    for fullprice in soup_is.find_all('div', attrs={'class': 'hdp__sc-7rrrvq-1 gIiYBD'}):
        houseprice = fullprice.text.split(" ")[0]



    main_list = []
    for housing in soup_is.find('ul', attrs={'class': 'zsg-tooltip-viewport'}).find_all('li'):
        for pp in housing.find_all('div', attrs={'class': 'Spacer-c11n-8-53-2__sc-17suqs2-0 dQahPh'}):
            for pg in pp.find_all('div', attrs={'class': 'dpf__sc-1qwb4yr-1 hxsvBX'}):
                for ps in pg.find_all('ul', attrs={'class': 'List-c11n-8-53-2__sc-1smrmqp-0 dpf__sc-1j9xcg4-1 dXzEiO bNyGAI'}):
                    for sp in pg.find_all('span', attrs={'class': 'Text-c11n-8-53-2__sc-aiai24-0 cvftlt'}):
                        main_list.append(sp.text)
                        #print(sp.text)
                        #print("~~")

    new_ml = list(set(sorted(main_list)))

    column_ls = []
    value_ls = []

    address_name = link.split('/homedetails/')[1].split('/')[0].replace("-", " ")

    column_ls.append('House Link')
    column_ls.append('House Address')
    column_ls.append('Price')
    column_ls.append('Zip')

    value_ls.append(link)
    value_ls.append(address_name)
    value_ls.append(houseprice)
    value_ls.append(zipcode)

    for i in new_ml:
        column_ls.append(i.split(':')[0])
        value_ls.append(i.split(':')[1].replace(" ", ""))
    #print(column_ls)
    #print(value_ls, len(value_ls))
    df_main = pd.DataFrame([value_ls], columns=column_ls)

    return df_main








