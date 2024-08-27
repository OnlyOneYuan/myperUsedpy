import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge,EdgeOptions as Option
from selenium.webdriver.edge.service import Service
from webdriver_manager import microsoft

dOption = Option()
dService = Service(microsoft.EdgeChromiumDriverManager().install())
dOption.debugger_address = '127.0.0.1:9223'
dr = Edge(service=dService,options=dOption)
print(dr.window_handles)
com = input(r"choose which handle?:")
main = dr.window_handles[int(com)]
dr.switch_to.window(main)

list1 = dr.find_elements(By.XPATH,".//a[contains(text(),'SHGJ')]")
for i in list1:
    print(i.text,end=" ")