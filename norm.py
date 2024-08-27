from selenium.webdriver import Edge,EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class norm:

   eoption = EdgeOptions()
   eoption.add_experimental_option("debuggerAddress","127.0.0.1:9222")
   driver  = Edge(executable_path=EdgeChromiumDriverManager().install(),options=eoption)
   
   def __init__(self):
      pass

   
   def getFtto(self,flist:list):
      if type(flist) != list:
         print('is not list input!')
         return ['errror']
      
      for i in flist:
         print(i.encode('unicode-escape').decode())