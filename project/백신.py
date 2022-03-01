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

#json->dataframe
df = pd.DataFrame.from_dict(json.loads(contents)['data'])

#가져올 리스트 딕셔너리
convert_list = ['10월말(누적) 1차접종자','10월말(누적) 2차접종자','10월말(누적) 추가접종','2-6월 1차접종자','2-6월 2차접종자','7월말(누적) 1차접종자',
                '7월말(누적) 2차접종자','8월말(누적) 1차접종자','8월말(누적) 2차접종자','9월말(누적) 1차접종자','9월말(누적) 2차접종자']

#숫자형으로 전환
for col in convert_list:
    df[col] = df[col].apply(pd.to_numeric)

#오름차순정렬    
# df = df.sort_values(by=['stateDt'], axis=0)

mpl.rc('font',family = 'AppleGothic')

#그래프 격자가 위치할 기본 틀을 만들기
fig = plt.figure()
#그래프 격자 만들기 
ax1 = fig.add_subplot(111)   #1행1열의1번째 그래프
# ax2 = ax1.twinx()    #y축을 두 개 만들거라서
# p1, = ax1.plot(df['자치구'],df['2-6월 1차접종자'],'b', label='접종자')
p1, = ax1.plot(df[col],df['자치구'],'b', label='접종자')
ax1.set_title('서울 자치구별 백신 접종 현황')
ax1.set_xlabel('기준일')
ax1.set_ylabel('접종자수')
ax1.legend([p1],[p1.get_label()])
#
ax1.tick_params(axis='x', labelrotation=90) #x축 label 90도 표
ax1.grid(axis='y')
fig.tight_layout(pad=1)

plt.show()