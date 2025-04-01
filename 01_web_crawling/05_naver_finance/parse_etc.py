import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

# print(pd.__version__)

def crawl(code):
    url = f'https://finance.naver.com/item/main.naver?code={code}'
    res = requests.get(url)
    bs_obj = BeautifulSoup(res.text, "html.parser")

    # print(res.text)
    # print(bs_obj)

    div_today = bs_obj.find("div", {"class":"today"})
    # print(div_today)

    em = div_today.find("em")
    # print(em)
    price = em.find("span").text
    # print(price)

    h_company = bs_obj.find("div", {"class": "h_company"})
    # print(h_company)
    ''' step by step '''
    h2_tag = h_company.find("h2")
    # print(h2_tag)
    ''' strip=True는 앞뒤 공백을 제거합니다. '''
    company_name = h2_tag.get_text(strip=True)
    # print(company_name)

    ''' simple way '''
    name = h_company.a.text


    ''' 종목 코드 '''
    code = bs_obj.find("div", {"class":"description"}).span.text
    # print(code)

    ''' 거래량 '''
    table_no_info = bs_obj.find("table", {"class":"no_info"})
    tds = table_no_info.tr.find_all("td")
    # print(tds[2])
    volume = tds[2].find("span", {"class":"blind"}).text
    # print(volume)

    dict = {"price": price, "name": name, "code":code, "volume":volume}
    # print(dict)
    return dict

# kakao = crawl("035720")
# print(kakao)

codes = ["035720", "005930", "051910", "000660"]
res = []

for code in codes:
    dict = crawl(code)
    # print(dict)
    res.append(dict)

# print(res)
''' make DF by using pandas '''
df = pd.DataFrame(res)
# print(df)

''' store in the exel'''
df.to_excel("prices.xlsx")
