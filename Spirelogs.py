import requests
from bs4 import BeautifulSoup
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["proxies"]

mycol.drop()

mycol = mydb["proxies"]


r = requests.get('https://free-proxy-list.net/')

soup = BeautifulSoup(r.text, 'lxml')

rows = soup.find_all('tr')

proxy_list = []
for row in rows[1:]:
    proxy_dict = {'IP_Address': '',
                  'Port': '',
                  'Country_Code': '',
                  'Country': '',
                  'Anonymity': '',
                  'Google': '',
                  'Https': '',
                  'Last_Checked': ''}
    td = row.find_all('td')
    try:
        proxy_dict['IP_Address'] = td[0].text
        proxy_dict['Port'] = td[1].text
        proxy_dict['Country_Code'] = td[2].text
        proxy_dict['Country'] = td[3].text
        proxy_dict['Anonymity'] = td[4].text
        proxy_dict['Google'] = td[5].text
        proxy_dict['Https'] = td[6].text
        proxy_dict['Last_Checked'] = td[7].text

        x = mycol.insert_one(proxy_dict)
        print(x.inserted_id)
    except IndexError:
        print("{} failed".format(row.text))







