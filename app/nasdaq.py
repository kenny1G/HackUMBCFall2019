import requests
from bs4 import BeautifulSoup

class Nasdaq():
    nasdaq_page = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    companies = {}
    page = requests.get(nasdaq_page).text
    soup = BeautifulSoup(page,'lxml')
    listing_table = soup.find('table',attrs={'class':'wikitable sortable'})
    for row in listing_table.findAll('tr')[1:]:
        symbol = row.findAll('td')[0].text.lower().replace('\n','')
        name = row.findAll('td')[1].text.lower()
        companies.update({symbol : name})

#print(companies)
