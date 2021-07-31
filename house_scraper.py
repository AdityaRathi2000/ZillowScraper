import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as webInfo

def house_scraper(link):
    class AppURLopener(webInfo.FancyURLopener):
        version = "Mozilla/5.0"

    opener = AppURLopener()
    response = opener.open(link)

    read_data = response.read()
    soup_is = BeautifulSoup(read_data, 'lxml')

    pick = 0
    pick_1 = 0

    main_list = []
    for housing in soup_is.find_all('div', attrs={'class': 'ds-data-col ds-white-bg ds-data-col-data-forward'}):
        for children in housing.find_all('span', attrs={'class': 'Text-c11n-8-38-0__aiai24-0 sc-oTpqt ckYUVN'}):
            main_list.append(children.text)
            break
        for children in housing.find_all('span', attrs={'class': 'sc-pbKro bjcxym'}):
            if (pick == 0):
                pick = 1
                main_list.append(children.text)
            elif (pick == 1):
                pick = 2
                main_list.append(children.text)
            elif (pick == 2):
                pick = 3
                main_list.append(children.text)
        for children in housing.find_all('div', attrs={'class': 'Text-c11n-8-38-0__aiai24-0 jtMauM'}):
            if (pick_1 == 0):
                pick_1 = 1
            elif (pick_1 == 1):
                pick_1 = 2
                main_list.append(children.text)
                break
        for children in housing.find_all('ul', attrs={'class': 'ds-home-fact-list'}):
            for li in children.find_all('li', attrs={'class': 'ds-home-fact-list-item'}):
                for space in li.find_all('span', attrs={'class': 'Text-c11n-8-38-0__aiai24-0 sc-pbJYR koDnCt'}):
                    main_list.append(space.text)
                    break
        for children in housing.find_all('div', attrs={'class': 'Text-c11n-8-38-0__aiai24-0 kZlbSX'}):
            for spanned in children.find_all('span', attrs={'class': 'Text-c11n-8-38-0__aiai24-0 grZBWh'}):
                main_list.append(spanned.text)
                break

    return main_list