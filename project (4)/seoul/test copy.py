from urllib.request import Request,urlopen
from urllib.parse import urlencode,unquote,quote_plus
import json
import xmltodict
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import requests
matplotlib.rcParams["font.family"] = "malgun Gothic"
matplotlib.rcParams["axes.unicode_minus"] = False
#호출 url주소

# url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19'#endpoint고 뒤에 json으로 받을거라
ServiceKey = 'XlIxr1CyGCs5BSRNmrg%2Bzz7qcLN02uchkN%2B98y2XKl5HeokzvNW3%2BbdKU3DQ%2FWs6ybm8bQm3CWeFSi3O6JyX5g%3D%3D'
url = 'https://api.odcloud.kr/api/15094083/v1/uddi:c56fbd05-7fc0-42de-86f6-d9334784049a?page=1&perPage=30&serviceKey={}'.format(ServiceKey)


response = requests.get(url)
# response의 내용을 text변환
contents = response.text

#json->dataframe
df = pd.DataFrame.from_dict(json.loads(contents)['data'])

#가져올 리스트 딕셔너리
convert_list = ['2-6월 1차접종자','2-6월 2차접종자','7월말(누적) 1차접종자','7월말(누적) 2차접종자','8월말(누적) 1차접종자','8월말(누적) 2차접종자',
                '9월말(누적) 1차접종자','9월말(누적) 2차접종자','10월말(누적) 1차접종자','10월말(누적) 2차접종자','10월말(누적) 추가접종']
rows = []
for x in df.values:
    row = [str(x[-1]),int(x[3]),int(x[5]),int(x[7]),int(x[9]),int(x[0])]
    rows.append(row)
print(rows)

#숫자형으로 전환
# for col in convert_list:
#     df[col] = df[col].apply(pd.to_numeric)
#     # print(df[col])
#     print(df[col][0])    
#     print(df[col])    
#     # print(df[col])  #col[0] = 9월말(누적) 2차접종자 
# for i in range(25):
#     location= df.iloc[i][-1]
#     month= df.iloc[i][3] #2-6월
#     month7= df.iloc[i][5] #7월
#     month8= df.iloc[i][7] #8월
#     month9= df.iloc[i][9] #9월
#     month10= df.iloc[i][0] #10월 
#     # print(month)
    
# print(df.columns[:-1])
# print('*'*50)
# print(df[df.columns[0]])
# print('*'*50)
# print(df.iloc[0][:-1].values) #관악구 value만 뽑음
# print('*'*50)
# print(df.iloc[0]) #종로구 데이터
# print(df.iloc[1]) #중구
# print(df.iloc[9]) #도봉구 데이터
# print(df.iloc[1][0]) #종로구 데이터     총3페이지까지 있음
# print(df.iloc[2][3]) #종로구 데이터     총3페이지까지 있음
# print('*'*50)
# print(df.columns[:-1])
# # df['10월'] = df[0]+df[1]
# # print(df['10월'])
# print(df)


#오름차순정렬    
# df = df.sort_values(by=['stateDt'], axis=0)

# # mpl.rc('font',family = 'AppleGothic')


# #그래프 격자가 위치할 기본 틀을 만들기
# fig = plt.figure()
# #그래프 격자 만들기 
# ax1 = fig.add_subplot(111)   #1행1열의1번째 그래프
# # ax2 = ax1.twinx()    #y축을 두 개 만들거라서
# # p1, = ax1.plot(df['자치구'],df['2-6월 1차접종자'],'b', label='접종자')
# p1, = ax1.plot(df.columns[:-1],df.iloc[0][:-1].values,'b', label='관악구')
# # print(df.iloc[0].values) #관악구 value만 뽑음

# ax1.set_title('서울 자치구별 백신 접종 현황')
# ax1.set_xlabel('기준일')
# ax1.set_ylabel('접종자수')
# ax1.legend([p1],[p1.get_label()])
# #
# ax1.tick_params(axis='x', labelrotation=90) #x축 label 90도 표
# ax1.grid(axis='y')
# fig.tight_layout(pad=1)

# plt.show()