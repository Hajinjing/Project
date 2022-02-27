import csv
from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd



url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
day = datetime.datetime.now()  # 오늘날짜 저장
days = day.strftime('%Y-%m-%d')  #오늘 날짜 서식

filename = "{}_시가총액.csv".format(days)
f = open(filename,"w",encoding="utf-8-sig",newline="")  #newline 엔터
write = csv.writer(f)
title ="N   종목명   현재가   전일비   등락률   액면가   시가총액   상장주식수   외국인비율   거래량   PER   ROE".split("\t")
# print(type(title))
write.writerow(title)  #리스트 형태로만 저장 가능

data_rows = soup.find("table",{"class","type_2"}).tbody.find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    if(len(columns) <=1):
            continue
    
    data = [column.get_text().strip() for column in columns]
    write.writerow(data)
 
 

for i in range(2,37):    
        url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(i)
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
        res = requests.get(url,headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text,"lxml")
        
        f = open(filename,"a",encoding="utf-8-sig",newline="")  #newline 엔터
        data_rows = soup.find("table",{"class","type_2"}).tbody.find_all("tr")
        for row in data_rows:
                columns = row.find_all("td")
                if(len(columns) <=1):
                        continue
                
                data = [column.get_text().strip() for column in columns]
                write.writerow(data)


df = pd.read_csv( "{}_시가총액.csv".format(days),index_col=0)

df['PER'] = df['PER'].str.replace(',','').astype(float)
# df["PER"] = pd.to_numeric(df['PER'], errors = 'coerce')

df.info()
print(df[df["PER"]<5])