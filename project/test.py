from urllib.request import Request,urlopen
from urllib.parse import urlencode,unquote,quote_plus
import json
import xmltodict
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc
import requests

#호출 url주소

# url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19'#endpoint고 뒤에 json으로 받을거라
ServiceKey = 'XlIxr1CyGCs5BSRNmrg%2Bzz7qcLN02uchkN%2B98y2XKl5HeokzvNW3%2BbdKU3DQ%2FWs6ybm8bQm3CWeFSi3O6JyX5g%3D%3D'
url = 'https://api.odcloud.kr/api/15094083/v1/uddi:c56fbd05-7fc0-42de-86f6-d9334784049a?page=3&perPage=10&serviceKey={}'.format(ServiceKey)


response = requests.get(url)
# response의 내용을 text변환
contents = response.text
# text를 json 타입으로 변경
# json_ob = json.loads(contents)
# json데이터 중 필요한 데이터 가져오기
# publicData = json_ob['response']['body']['items']['item']

#xml -> json

#json->dataframe
df = pd.DataFrame.from_dict(json.loads(contents)['data'])

#가져올 리스트 딕셔너리
convert_list = ['2-6월 1차접종자','2-6월 2차접종자','7월말(누적) 1차접종자','7월말(누적) 2차접종자','8월말(누적) 1차접종자','8월말(누적) 2차접종자',
                '9월말(누적) 1차접종자','9월말(누적) 2차접종자','10월말(누적) 1차접종자','10월말(누적) 2차접종자','10월말(누적) 추가접종']

#숫자형으로 전환
for col in convert_list:
    df[col] = df[col].apply(pd.to_numeric)
    print(df[col])
    
    # print(df[col])  #col[0] = 9월말(누적) 2차접종자 
    
# print(df.columns[:-1])
print('*'*50)
# print(df[df.columns[0]])
print('*'*50)
# print(df.iloc[0]) #종로구 데이터
# print(df.iloc[1]) #중구
# print(df.iloc[9]) #도봉구 데이터
print(df.iloc[1][0]) #종로구 데이터     총3페이지까지 있음
print(df.iloc[2][3]) #종로구 데이터     총3페이지까지 있음
# print(df.columns[:-1])
# df['10월'] = df[0]+df[1]
# print(df['10월'])

