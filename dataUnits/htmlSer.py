from bs4 import BeautifulSoup as BS
import json as j

class rhtml:
    
    def __init__(self,xml:str,feat="xml") -> None:
        self.html = BS(xml,features=feat)
        # print(self.html)
        pass

#获取安装地址 
    def fdLocalabl(self):
        ht = BS(self.html.find(r"spropertiesHTML").get_text(),features="xml")
        tr = ht.find(attrs={'id':'tr_RME_EQP_POSIT_ID'})
        loc = tr.find(attrs={'id':'td_RME_EQP_POSIT_ID'})
        return loc.get_text()

    # def input(self)->None:
    #     print(self.html.prettify())
    def getJsonofDia(self,i=2):
        def getEidofDia(json):
            dia = j.loads(str(json))
            row = dia["rows"][0]
            return row["data"][i]
        try:
            json = self.html.squeryresult.text
            res = getEidofDia(json)
        except:
            res = "err"
        
        
        return res