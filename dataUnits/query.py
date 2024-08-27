#use re to search key in string

import json
import re

from urllib.parse import quote
from os import popen
from bs4 import BeautifulSoup

#获取ODN表单格式
def getODN_UrlInfo(keywords:str):
    with open("dataUnits\html\ODN.txt","r",encoding='utf-8-sig') as f:
        odn_query = f.read()
    urlcode = quote(keywords)
    result = odn_query.replace("(10101)",urlcode)
    print(urlcode)
    # result = result.encode('utf-8')
    # result_url = quote(result)
    return 'queryCondition='+result

#获取局站编码
def getDIA_UrlInfo(keywords:str):
    with open("dataUnits\html\diaStation.txt","r",encoding='utf-8-sig') as f:
        odn_query = f.read()
    urlcode = quote(keywords)
    result = odn_query.replace("(replace)",urlcode)
    # print(urlcode)
    # result = result.encode('utf-8')
    # result_url = quote(result)
    return result

#获取局站名称
def getDIAName_UrlInfo(keywords:str):
    with open("dataUnits\html\diaStationid.txt","r",encoding='utf-8-sig') as f:
        odn_query = f.read()
    urlcode = quote(keywords)
    result = odn_query.replace("(replace)",urlcode)
    return result

#获取全程路由(基于正则表达式)
def getROute(route:str):
    if route != None:
        return re.findall("</cell><cell></cell><cell></cell><cell></cell><cell></cell><cell>.*?</cell><cell></cell><cell></cell><cell>(.*?)[^>]</cell><cell></cell><cell>[^<]",route,0)[0]

#加密json
def getUlenJsonData(djson:json):
    return quote(djson)

#获取ODNid
def getODNid(ODN:str):
    if ODN != '':
        return re.findall('id":"(.*?)"',ODN,flags=0)
    return 0

#获取电路标识符
def getEidSign(text:str):
    if text!= None:
        return re.search(r'id=\\"(.*?)\\"',text,flags=0).group(1)
    return 0

#获取ONU表单数据
def getONU_UrlInfo(keywords:str):
    with open('dataUnits\html\ONU.txt','r',encoding='utf-8-sig') as f:
        onu_query = f.read()
    urlcode = quote(keywords)
    result = onu_query.replace("(10101)",urlcode)
    return 'queryCondition='+result

def get1stAnd2st(jdatas:list):
    pass

#获取工单信息
def getorderStatue(ijson):
    pass

def getJsonofDia(html):
    bs = BeautifulSoup(html)
    json = bs.find_all('squeryResult')
    print(json)
    def getEidofDia(Json):
        pass

class Splitter:
    #Splitter name
    sp1st = []
    sp2nd = []
    olt   = []
    station = ""
    sid   = "" 
    
    def __init__(self,s1And2,oltUp):
        flag2nd = 1
        #sign second Splitter whether exiting
        self.json1A2 = s1And2
        self.jsonOlt = oltUp

        mergSplit = []
        station = self.station
        sid     = self.sid

        splitJson = json.loads(s1And2)
        oltJson   = json.loads(oltUp)

        try:
            split2nd = splitJson[0]['TWOEQP']
        except KeyError:
            flag2nd = 0#确认有无二级分光器
            print('no sercond onu exit!')
        
        for i,data in enumerate(s1And2):
            if i == 0:
                split1st = data['ONEEQP']

            if flag2nd == 1:
                split2nd = data['TWOEQP']
                mergSplit.append(split2nd)
                print("{:20}".format(" "),"分光器2:",data['TWOEQP'])
             
        return {"oneeqp":split1st,"twoeqp":mergSplit,"olt":""}
    
class wms:

    def getVaroF():
        pass   

