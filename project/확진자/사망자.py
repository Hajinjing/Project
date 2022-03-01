from urllib.request import Request,urlopen
from urllib.parse import urlencode,unquote,quote_plus
import json
import xmltodict
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc

#호출 url주소

# url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19'#endpoint고 뒤에 json으로 받을거라
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
ServiceKey = 'XlIxr1CyGCs5BSRNmrg%2Bzz7qcLN02uchkN%2B98y2XKl5HeokzvNW3%2BbdKU3DQ%2FWs6ybm8bQm3CWeFSi3O6JyX5g%3D%3D'
startCreateDt='20201201'
endCreateDt = '20201229'
queryParms = '?'+urlencode({
    quote_plus('ServiceKey') : ServiceKey,
    quote_plus('startCreateDt') : startCreateDt,
    quote_plus('endCreateDt') : endCreateDt,
    
})

request = Request(url+unquote(queryParms))
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()

#xml -> json
json_string = json.dumps(xmltodict.parse(response_body), indent=4)

#json->dataframe
df = pd.DataFrame.from_dict(json.loads(json_string)['response']['body']['items']['item'])

convert_list = ['accDefRate','deathCnt',
                'decideCnt','seq']

for col in convert_list:
    df[col] = df[col].apply(pd.to_numeric)
    
df = df.sort_values(by=['stateDt'], axis=0)

mpl.rc('font',family = 'AppleGothic')

#그래프 격자가 위치할 기본 틀을 만들기
fig = plt.figure()
#그래프 격자 만들기 
ax1 = fig.add_subplot(111)   #1행1열의1번째 그래프
ax2 = ax1.twinx()    #y축을 두 개 만들거라서
p1, = ax1.plot(df.stateDt, df.decideCnt, 'b--', label='확진자')
p3, = ax2.plot(df.stateDt, df.deathCnt, 'r--', label='사망자')
ax1.set_title('국내 코로나19 발생 누적 현황')
ax1.set_xlabel('기준일')
ax1.set_ylabel('확진자')
ax1.legend([p1,p3],[p1.get_label(),p3.get_label()])
#
ax1.tick_params(axis='x', labelrotation=90) #x축 label 90도 표
ax1.grid(axis='y')
ax2.set_ylabel('사망자(명)')
fig.tight_layout(pad=1)

plt.show()