from datetime import date, datetime, timedelta
from os import mkdir,listdir
import re

import bs4
from numpy import info
from re import findall
import dataUnits.query as query
import dataUnits.excel as excel
from url_cookies import Ucookies, bUrl
from dataUnits.excel import dia
from dataUnits.htmlSer import rhtml
import pandas as pd
from bs4 import BeautifulSoup as BS
from lxml import etree
from url_cookies import ZTE
class run:
    u = Ucookies()
    # __sname__ = 'Sort Name'#目前无实际作用（本意为给每个方法设计不同的查询种类的）
    # __aim__   = 'Aim Name'
    # __now__   = datetime.now().strftime("%Y-%m-%d %Hh%Mm%Ss")
    # __dname__ = 'dir path or name'#文件夹目录名称—可以更改
    # __cook__  = 'cookies'
    # __eid__   = {}
    # __id__    = 0

    
    def __init__(self,sname,saim,i=None) -> None:
        """
        sname no meaning,saim filename
        """
        self.__sname__ = sname
        self.__aim__   = saim
        # self.__id__    = i
        nowT = datetime.now().strftime("%Y-%m-%d %Hh%Mm%Ss")
        if i!=None:
            dir  = "xlsx\\"+str(nowT)+'-'+str(i)
        else:
            dir  = "xlsx\\"+str(nowT)
        self.__dname__ = dir+"\\"
        mkdir(dir)
        try:
            with open('heads\cookies','r') as fp:
                self.__cook__ = fp.read()
        except TypeError:
            print('cookies no or wrong')
        file = open(self.__dname__+self.__aim__,'w')
        file.close()

#查询1、2级分光器并输出xlsx
    def ODNcheck_1stAn2ndONU(self):
        uc    = Ucookies()
        odn   = uc.getODN(self.__aim__)
        print("the reply is:\n\n",odn.text)
        id    = query.getODNid(odn.text)
        self.__eid__ = id
        print(id)
       
        for i in id:
            id2nd = uc.getODNnd(i).text
            filenameODN = '\\'.join([self.__dname__,i])
            excel.getODNupANDdown(id2nd,filenameODN)      
        # return sheets

#查询onu的上联olt并输出xlsx
    def ODNcheck_OLTofONU(self):
        uc  = Ucookies()
        odn = uc.getODN(self.__aim__)#获取站点下ONU的所有分光器的唯一标识
        id  = query.getODNid(odn.text)#json数据处理为list
        self.__eid__ = id
        sheets = []
        print(id)
        for i in id:
            oltUpPort = uc.getOLTofONU(i).text
            print('upPortofOlt:',oltUpPort)
            filenameOLTPort = ''.join([self.__dname__,i])
            print(filenameOLTPort)
            try:
                excel.getOltUpofOnu(oltUpPort,filenameOLTPort)#输出表格
            except IndexError:
                print('the eid %s Out of Index:May be no olt exit'%(i))
            finally:
                continue

#合并目录下的ONU xlsx文件解耦       
    def getMergeOnu(self):
        edir = self.__dname__     
        elist = listdir(edir)
        slist = []
        for i in elist:
            slist.append("\\".join([edir,i]))
        slist.remove(self.__dname__+'\\'+self.__aim__)
        print(slist)
        excel.mergeONU(slist,self.__dname__+"udofOnu.xlsx")

#获取全程路由并输出excel(未完成)
    def getRoute(self,zid:list):
        zRoute = ""
        eRoute = []
        for i in zid:
            print("id: ",i)
            # zRoute = self.u.getEntryOfEid(i).text
            # print("like 21z num:")
            # print(zRoute,end="\n\neid=")
            # eid = query.getEidSign(zRoute)
            # print(eid,end="\n\n")
            # print(self.u.getRouteByEider(eid))
            # eRoute.append(self.u.getRouteByEider(eid).text)
            eRoute.append(self.u.getEntryOfEid(i))
        print(eRoute,sep='\n')
        excel.totalRoute(eRoute,self.__dname__)

#获取局站业务
    def getFttoBus(self,fname:str):
        dxlsx = dia()
        dxlsx.fNameOfEid(fname)
        return None

#根据名称获取局站编码
    def geteidofStation(self,fname:list,col:int=2):
        coldict = {1:1,2:2}
        u = Ucookies()
        name = []
        j = 0
        for i in fname:
            print(i,"%2dindex：",j)
            j = j+1
            try:
                if col == 2:
                    r = rhtml(u.getEidOfDiaName(i).text,"html")
                else: 
                    if col == 1:
                        r = rhtml(u.getNameofEid(i).text,"html")
            except:
                r = "err"
            finally:
                name.append(r.getJsonofDia())
        leng = len(fname)
        with open("result.txt","a+") as f:
            for i in range(leng):
                f.writelines(fname[i]+","+str(name[i])+"\n")

#根据局站编码获取名称(合并到geteidofStation)
    def getNameofStation(self,fname:list):
        u = Ucookies()
        name = []
        j = 0
        for i in fname:
            print(i," index：",j)
            j = j+1
            try:
                r = rhtml(u.getNameofEid(i).text,"html")
            except:
                r = "err"
            finally:
                name.append(r.getJsonofDia(i=1))
        leng = len(fname)
        with open("result.txt","a+") as f:
            for i in range(leng):
                f.writelines(fname[i]+","+str(name[i])+"\n")
            
#获取可用iptv数量
    def getIptvNum(self,cookies,bums=None,flag=1):
        def getContent():
            daily = pd.read_excel("每日通报.xlsx","当日受理新装工单")
            north = daily[daily["网格"].isin(["朱泾","枫泾","亭林"])]
            return north["业务号码"].values
        if bums == None:
            bums = getContent()
        b = bUrl(cookies)
        infors = []
        for bum in bums:
            num = str(bum)
            infor =b.getBinfor(num,flag)
            if infor == []:
                if flag == 1:
                    infor = b.getBinfor(num,2)
                else:
                    infor = b.getBinfor(num,1)
            infors.append(infor)
        return infors
        
    def getLastTime(filepath="金山.xlsx"):
        zte = ZTE()
        j = 0
        excl = pd.read_excel(filepath)
        valOfExcel = excl["宽带账号"]
        print(valOfExcel)
        sid = []      
        time = []
        su = []
        def check():
            pass
        
        def getExcelvalue():
            pass

        for i in valOfExcel:
            if j>10000:break
            j = j+1
            try:
                json = zte.getExitCatAndLastime("0"+str(i)).json()
                ltime = json["generalMsg"]["hg"]["sysupTime"]
                id = json["generalMsg"]["hgServiceParam"][0]["deviceID"]
                try:
                    status = zte.getReFresh("0"+str(i),id).json()["response"]["data"][0]["statusInfo"]
                    print(status)
                    # ["response"]["data"][0]["statusInfo"]
                    # print(status)
                    time.append(ltime)
                    su.append(status)
                except:
                    time.append(ltime)
                    su.append("None")
            except:
                time.append("None")
                su.append("None")
            # print(ltime,status)
        excl.insert(12,"上电时间",time)
        excl.insert(13,"状态",su)
        excl.to_excel("cat.xlsx")
        
        return sid
    
class wms():

    daily = None
    blist = {
        "外线处理人":"",
        "定单主题":"",
    }

    def __init__(self,sht:str) -> None:
        '''sht:工作表名称'''
        self.sht = sht
        self.daily = pd.read_excel("每日通报.xlsx",sht) 

    def changSht(self,sht:str) -> None:
        self.sht = sht
        self.daily = pd.read_excel("每日通报.xlsx",sht) 

    def getExcel(self,head:str,ctent:list):
        daily = self.daily
        lines = daily[daily[head].isin(ctent)]
        list_lines = lines["业务号码"].values
        list_ta = []
        for i in list_lines:
            if type(i) != str:
                temp = '0'+str(int(i))
            else:
                temp = i
            list_ta.append(temp)
        
        return list_ta

    # def addCol(head,cten):
    #     daily[daily[head]==cten].add()

    def getIptvNum(self,cookies,bums=None,flag=1):
        ''' get information of bums '''
        el = {"Bno":[],"iptv":[],"ires":[],"fttr":[],"lres":[],"saleman":[],"sort":[],"stats":[]}

        def saveHtml(blist:list):
            '''blist是业务信息列表，为数组'''
            print("\n工单数量:",len(blist))
            # stat = {"good":{"iptv":False,"fttr":False}}
            iptv = 0
            iptv1 = 0
            iptv2 = 0
            fttr = 0
            stat = 0
            lres = 0
            ires = 0
            ires1 = ""
            ires2 = ""
            for i,html in enumerate(blist):
                strHtml = etree.HTML(html)
                js = strHtml.xpath("//*[@type='text/javascript']")[19].text
                # print(js)
                result_Bno = "NaN"
                #业务号码
                result = strHtml.xpath('//*[@title="CPN小区宽带上网帐号"]')
                if result != []:
                    result = result[0].xpath('following-sibling::td[1]')[0]
                    result_Bno = result.text
                else:
                    result_Bno = "Error"
                print(result_Bno," index:",i,end=" ")
                #附属产品
                result = []
                result_Good = []
                #全屋光
                result = strHtml.xpath('//*[contains(@title,"全屋光")]')
                if result != []:
                    fttr = 1
                    lres = result[0].xpath('following-sibling::td[1]')[0].text
                    print(result_Bno,end=" ")
                #iptv
                result1 = strHtml.xpath('//*[contains(@title,"iptv1")]')
                result2 = strHtml.xpath('//*[contains(@title,"iptv2")]')
                if result1 != []:
                    iptv1 = 1 
                    ires1 = result1[0].xpath('following-sibling::td[1]')[0].text
                if result2 != []:
                    iptv2 = 1
                    ires2 = result2[0].xpath('following-sibling::td[1]')[0].text
                iptv = iptv1 + iptv2
                if ires1 == "ADD" or ires2 == "ADD":
                    ires = "ADD"
                #发展人
                try:
                    result = []
                    result = strHtml.xpath('//*[contains(@title,"发展人")]')
                    person = result[0].xpath('following-sibling::td[1]')[0].text
                    print(person,end=" ")
                except:
                    print("no saleman")
                    person = ""
                #工单状态
                result = []
                result = strHtml.xpath('//*[contains(text(),"归档")]')
                if result != []:
                    stat = 1
                    print("归档")
                print("\n")
            return {
                "Bno":result_Bno,
                "iptv":iptv,
                "ires":ires,
                "fttr":fttr,
                "lres":lres,
                "saleman":person,
                "sort":"",
                "stats":stat
            }
        if self.sht == "当日新装工单" or self.sht == "当日受理改服务工单":
            bums = self.getExcel("网格",["金北"])
        if self.sht == "当日受理新装工单": 
            bums = self.getExcel("网格",["朱泾","亭林","枫泾"])

        print(bums)
        b = bUrl(cookies)
        infors = []
        
        i = 0
        for bum in bums:
            num = str(bum)
            infor = b.getBinfor(num,flag)
            if infor == []:
                if flag == 3:
                    infor = b.getBinfor(num,1,fullmatch=True)
                else:
                    if flag == 1:
                        infor = b.getBinfor(num,2)
                    else:
                        if flag == 2:
                            infor = b.getBinfor(num,1)#这段代码无意义
                
            infors.append(infor)

            gNum = saveHtml(infor)
            
            e = el
            for name in el:#debug
                e[name].append(gNum[name])
            i = i + 1
        df = pd.DataFrame(e)
        print(self.sht)
        with pd.ExcelWriter("data.xlsx",mode="a",engine="openpyxl",if_sheet_exists="replace") as writer:
            print("ok")
            df.to_excel(writer,sheet_name=self.sht)
        print(e)
        return e,i

