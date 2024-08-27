# 
#@auther 1yuan
#模拟登录
# 

from datetime import date, timedelta
from email import header
import json
from os import name
import time
from turtle import pos
from typing import overload
from requests import head, post,get, put
from dataUnits import transUrl
from dataUnits.query import getODN_UrlInfo, getONU_UrlInfo,getUlenJsonData,getDIA_UrlInfo,getDIAName_UrlInfo
class Ucookies:

    flag = 0

    def __init__(self,sCookies=None) -> None:
        if sCookies == None:
            with open('heads\cookies','r') as f:
                self.cook = f.read()
        #时间戳精确到后四位（不带小树）
        self.stamp = str(round(time.time(),4)).replace(".","")
        return
        

#标头通用处理方法
    def __inithead__(self,hfile):
        hdict = transUrl.initHeaderFromTxt(hfile)
        hdict['Cookie'] = self.cook
        return hdict

#获取ftto局站名称    
    def getFttoName(self):
        '''读取局站名称'''

        url = 'unkown'
        headerDict = transUrl.initHeaderFromTxt(r'heads\vlan')
        headerDict['Cookie'] = self.cook
        vlan = post(url=url,headers=headerDict)
        return vlan

#获取单号——服保
    def getFttoColum(self,PageNum:int=1,Sname:str=None):
        if Sname:
            return
        url = 'unkown'
        headerDict = transUrl.initHeaderFromTxt(r'heads\ftto')
        fid = post(url,headers=headerDict)
        return fid

#获取电路编码对应系统标识符号(多编路)
    def getEntryOfEid(self,eid:str):
        '''获取电路编码对应系统标识符号(多编路)'''
        url = 'unkown'
        headerDict = transUrl.initHeaderFromTxt(r'heads\eids')
        headerDict['Cookie'] = self.cook
        with open('json\eid.json','r',encoding='utf-8-sig') as fp:
            ejson = json.load(fp)
        ejson['localCirNo'] = eid
        entry = post(url=url,headers=headerDict,data={'json':json.dumps(ejson)})
        return entry

    def getInfoByEids():
        pass
#电路编码获取电路信息(多编码)--路由不全--
    @overload
    def getInfoByEids(self,eid:list):
        '''电路编码获取电路信息(多编码)--路由不全--'''
        pass

#电路编码获取电路信息(单编码)--路由不全--
    @overload
    def getInfoByEids(self,eid:str):
        '''电路编码获取电路信息(单编码)--路由不全--'''
        pass
    
    def getRouterByEids(self,eid:list):
        '''电路标识获取路由'''
        url = r'unkown'
        cirNo = ",".join(eid)
        data = {"json":'{"circuitIds":"%s"}'%cirNo,"randomSeq":self.stamp}
        headerDict = self.__inithead__(r'heads\router')
        route = post(url=url,headers=headerDict,data=data)
        return route

#一级分光器 
    def getODN(self,aimRoom:str):
        url = 'unkown'
        headerDict = transUrl.initHeaderFromTxt(r'heads\ODN')
        headerDict['Cookie'] = self.cook
        html = getODN_UrlInfo(aimRoom)
        residJson = post(url=url,headers=headerDict,data=html)
        return residJson

#二级分光器
    def getODNnd(self,ODNid):
        url = 'unkown'+ODNid    
        headerDict = transUrl.initHeaderFromTxt(r'heads\ODNnd')
        headerDict['Cookie'] = self.cook
        idndJson = post(url=url,headers=headerDict)
        return idndJson

#获取一级分光器设备信息（疑似需要权限）
    # def getODN1stEqinfor(self,resid):
    #     url = 'unkown'
    #     headerDict = transUrl.initHeaderFromTxt(r'heads\odn1stRes')
    #     # headerDict['Cookie'] = self.cook
    #     print(headerDict)
    #     Eqinfor = post(url=url,headers=headerDict)
    #     return Eqinfor

#分光器上联
    def getOLTofONU(self,ODNid):
        url = 'unkown'
        headerDict = transUrl.initHeaderFromTxt(r'heads\OLTofONU')
        headerDict['Cookie'] = self.cook
        params = {'eqpId':ODNid,'method':'queryOltAndPort'}
        json = get(url=url,headers=headerDict,params=params)
        return json
    
#ONU id
    def getONUid(self,uname):
        url = 'unkown'
        headerDict = transUrl.initHeaderFromTxt(r'heads\ONU')
        headerDict['Cookie'] = self.cook
        html = getONU_UrlInfo(uname)
        idJson = post(url=url,headers=headerDict,data=html)
        return idJson
    
#ONU RESid
    def getONURes(self,id):
        url = 'unkown'
        headerDict = transUrl.initHeaderFromTxt(r'heads\ONUResid')
        headerDict['Cookie'] = self.cook
        headerDict['Referer'] = unkown
        print(headerDict)
        residJson = post(url=url,headers=headerDict,data=None)
        return residJson

#获取工单信息
#json\orderinfo.json
    def getOrder(self,id:str):
        url = 'unkown'
        head = transUrl.initHeaderFromTxt(r'heads\order')
        head['Cookie'] = self.cook
        with open("json\order.json","r",encoding="utf-8-sig") as fp:
            a = json.load(fp)
            a["para"][0]["crmOrderCode"] = id
        timestamp = int(time.time())
        b = "_callFunParams="+json.dumps(a)+"&_timeStamp="+str(timestamp)
        status = post(url=url,headers=head,data=b)
        return status
    
    def getEidOfDiaName(self,name:str):
        url = 'unkown'
        params = {'method':'doDyncQryData','resTypeId':'9281','dt':int(time.time())}
        html = getDIA_UrlInfo(name)
        head = transUrl.initHeaderFromTxt(r'heads\diaStation')
        head['Cookie'] = self.cook
        diaStation = post(url,headers=head,params=params,data="queryCondition="+html)
        return diaStation
    
    def getNameofEid(self,name:str):
        url = 'unkown'
        params = {'method':'doDyncQryData','resTypeId':'9281','dt':int(time.time())}
        html = getDIAName_UrlInfo(name)
        head = transUrl.initHeaderFromTxt(r'heads\diaStation')
        head['Cookie'] = self.cook
        diaStation = post(url,headers=head,params=params,data="queryCondition="+html)
        return diaStation


class bUrl:
    '''客服支撑系统'''

    blist = []

    def __init__(self,cookies) -> None:
        self.cookies = cookies
        pass
    #获取业务号码信息
    def __getBusNumberInfor__(self,aims:dict):
        url = 'unkown'
        # params = {'woId':woid,'hisFlag':hisFlag,'shardingId':shardingId}
        head = transUrl.initHeaderFromTxt(r'heads\Business Number')
        head['Cookie'] = self.cookies
        infor = get(url,headers=head,params=aims)
        # print(infor.text)
        return infor
    
    #获取业务号码列表
    def __getBusNumberList__(self,bnum:str,flag=1,endTime=None):
        if endTime == None:
            endTime = date.today()-timedelta(days=1)
        '''bnum业务号码，flag运行模式'''
        url = 'unkown'
        head = transUrl.initHeaderFromTxt(r'heads\BnumberList')
        if flag == 2:
            with open(r"json\bulisted.json","r",encoding='utf-8-sig') as f:
                bjson = json.load(f)
                bjson['archTimeStart'] = endTime.strftime("%Y-%m-%d %H:%M:%S")
        else :
            if flag == 1:
                with open(r"json\bulisting.json","r",encoding='utf-8-sig') as f:
                    bjson = json.load(f)
            else:
                return 
        bjson['busiNo'] = bnum
        head['Cookie'] = self.cookies
        list = post(url=url,headers=head,data=bjson)
        # print(list.json())
        return list
    
    #服务开通综合处理
    def __getTwohrefCurrInfor__(pname=None):
        url = 'unkown'
        head = transUrl.initHeaderFromTxt(r"json\twohrefCurr.json")
        kljson = json.load(r"json\twohrefCurr.json")
        if pname:
            kljson["dealMan"] = pname
        klist = post(url,headers=head)
        return klist

    def getBinfor(self,bnum:str,flag=2,endTime=None,fullmatch=False):
        list = self.__getBusNumberList__(bnum,flag,endTime).json()['list']
        aims = {"woId":"","hisFlag":str(flag),"shardingId":"31"}
        params = []
        infor = []
        for i in list:
            aims["woId"] = i["WO_ID"]
            params.append(aims)
        if fullmatch == True:
            for j in params:
                j["hisFlag"] = "1"
                result = self.__getBusNumberInfor__(j)
                infor.append(result.text)
                j["hisFlag"] = "2"
                result = self.__getBusNumberInfor__(j)
                infor.append(result.text)
        else:
            for j in params:
                result = self.__getBusNumberInfor__(j)
                # print(result.text)
                infor.append(result.text)
        # print(infor)
        return infor
    
class ZTE:
    '''中兴网关'''
    def getExitCatAndLastime(self,sid):
        url = 'unkown'
        params = {"deviceID":"SID="+sid,"PanelID":"2"}
        head = transUrl.initHeaderFromTxt(r'heads\cat')
        head["Cookie"] = "JSESSIONID=9q2uuw6rcierlrgevzvzo3gl"
        head["Referer"] = "unkwon"
        data = {
                "itemMap":[
                    {
                        "key":"deviceID", 
                        "value":params["deviceID"]
                    }, 
                    {
                        "key":"tabName", 
                        "value":""
                    }
                ]
            }
        result = put(url=url,params=params,headers = head,json=data)
        return result
    
    def getReFresh(self,sid,id):
        print(sid,"  ",id)
        url = 'unkown'
        params = {"deviceID":sid,"PanelID":"2"}
        head = transUrl.initHeaderFromTxt(r"heads\catrefrash")
        head["Referer"] = "unkown"
        head["Cookie"] = "JSESSIONID=1vur0dmq2s8dp1h5ut20z33fd9"
        url = url+'data={"deviceID":"'+id+'","deviceType":"HGW"}&isc_dataFormat=json'
        print(url)
        res = get(url=url,headers=head)
        return res
    
    def checkBidByMac(self,mac):
        url = 'unkown'
        params = {
                "data": {"deviceType":"HGW","ruleType":"Mac","ruleValue":mac},
                "isc_dataFormat": "json",
                "pageSize": 100,
                "pageNo": 1,
                "isc_flag": "smartClient",
                "_operationType": "fetch",
                "_startRow": 0,
                "_endRow": 75,
                "_sortBy": "lastModifyTime",
                "_textMatchStyle": "exact",
                "_componentId": "isc_PageListTable_0",
                "_dataSource": "cpehg_neal_general_CpeDataSource",
                "isc_metaDataPrefix": "_"
                }
        head = transUrl.initHeaderFromTxt(r"heads\macToBid")
        res = get(url,headers=head,params=params)
        
        return res
