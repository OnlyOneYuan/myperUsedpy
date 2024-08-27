from requests import get
from url_cookies import bUrl
from json import loads
from datetime import date,datetime, timedelta
from bs4 import BeautifulSoup as BS
from time import time
from url_cookies import ZTE
from sort import run
from sort import wms

jSESSION = "JSESSIONID=40710C1251CF25ED913B25D87E2C9B58.w851"
# w = wms("当日新装工单")
w = wms("当日受理新装工单")
# a = w.getIptvNum(jSESSION,None)
# v = w.changSht("当日受理改服务工单")
b = w.getIptvNum(jSESSION,None)
# u = w.changSht("当日受理新装工单")
# c = w.getIptvNum(jSESSION,None)


