# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from django.shortcuts import render,redirect
from urllib.request import Request,urlopen
from urllib.parse import urlencode,unquote,quote_plus
import json
import matplotlib
import xmltodict
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc
import requests
from seoul.models import Vaccine
matplotlib.rcParams["font.family"] = "malgun Gothic"
matplotlib.rcParams["axes.unicode_minus"] = False
import cx_Oracle as ora  #오라클 연동

# Create your views here.

def connections():
    try:
        conn=ora.connect('ora_user/1234@localhost:1521/orcl')
    except Exception as e:
        print('예외 발생')
    return conn

def chart(request):
    conn=ora.connect('ora_user/1234@localhost:1521/orcl')
    vaccineData()
    # query = 'select * from vaccine'
    # qs=pd.read_sql_query(query,connections())
    # print(df)
    qs = Vaccine.objects.all()

    object_df3 = pd.DataFrame.from_records(qs.values())
    print("object.all() : ",object_df3)
    context = {'chart':qs}
    print(context)
    chartshow()
    
    data = []
    for x in object_df3.values:
        row = [int(x[3]),int(x[5]),int(x[7]),int(x[9]),int(x[0])]
        data.append(row)
        
    
    
    return render(request,'chart.html',{
        'data' : data
    })

def vaccineData():
    ServiceKey = 'XlIxr1CyGCs5BSRNmrg%2Bzz7qcLN02uchkN%2B98y2XKl5HeokzvNW3%2BbdKU3DQ%2FWs6ybm8bQm3CWeFSi3O6JyX5g%3D%3D'
    url = 'https://api.odcloud.kr/api/15094083/v1/uddi:c56fbd05-7fc0-42de-86f6-d9334784049a?page=1&perPage=30&serviceKey={}'.format(ServiceKey)
    response = requests.get(url)
    # response의 내용을 text변환
    contents = response.text
    #json->dataframe
    df = pd.DataFrame.from_dict(json.loads(contents)['data'])
    # print(df)
    #가져올 리스트 딕셔너리
    # convert_list = ['10월말(누적) 1차접종자','10월말(누적) 2차접종자','10월말(누적) 추가접종','2-6월 1차접종자','2-6월 2차접종자','7월말(누적) 1차접종자',
    #                 '7월말(누적) 2차접종자','8월말(누적) 1차접종자','8월말(누적) 2차접종자','9월말(누적) 1차접종자','9월말(누적) 2차접종자']
    rows = []
    for x in df.values:
        row = [str(x[-1]),int(x[3]),int(x[5]),int(x[7]),int(x[9]),int(x[0])]
        rows.append(row)
        location = row[0]
        month = row[1]
        month7 = row[2]
        month8 = row[3]
        month9 = row[4]
        month10 = row[5]
        qs = Vaccine(location=location, month=month, month7=month7, month8=month8,month9=month9,month10=month10)
        qs.save()

def chartshow():
    qs = Vaccine.objects.all()
    vData = pd.DataFrame.from_records(qs.values())
    #그래프 격자가 위치할 기본 틀을 만들기
    fig = plt.figure()
    #그래프 격자 만들기 
    ax1 = fig.add_subplot(111)   #1행1열의1번째 그래프
    # ax2 = ax1.twinx()    #y축을 두 개 만들거라서
    # p1, = ax1.plot(df['자치구'],df['2-6월 1차접종자'],'b', label='접종자')
    p1, = ax1.plot(vData.columns[1:],vData.iloc[0][1:],'b', label=vData.iloc[0][0])
    p2, = ax1.plot(vData.columns[1:],vData.iloc[1][1:],'r', label=vData.iloc[1][0])
    
    # for i in range(25):
        # p1, = ax1.plot(vData.columns[1:],vData.iloc[i][1:],'b', label=vData.iloc[i][0])
    ax1.legend([p1,p2],[p1.get_label(),p2.get_label()])
    # print(df.iloc[0].values) #관악구 value만 뽑음

    ax1.set_title('서울 자치구별 백신 접종 현황')
    ax1.set_xlabel('기준일')
    ax1.set_ylabel('접종자수')
    
    #
    ax1.tick_params(axis='x', labelrotation=90) #x축 label 90도 표
    ax1.grid(axis='y')
    fig.tight_layout(pad=1)

    plt.show()
    
#오름차순정렬    
# df = df.sort_values(by=['stateDt'], axis=0)

# mpl.rc('font',family = 'AppleGothic')


#그래프 격자가 위치할 기본 틀을 만들기
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