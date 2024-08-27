#表单
#废弃
class formUntils:

    def __init__(self) -> None:
        pass
    #去除文本中的换行符
    def keyValueChange(self,key:str,value:str):
        with open('json/url.html','r',encoding='utf8') as form:

            stringSource = form.readlines()
            #传输的首行有回车'/n'
            zeroSring = stringSource[0]
            stringSource[0] = ''

            for i,stringLine in enumerate(stringSource):
                if i == 0:
                    continue
                # stringLine = stringLine.replace(key,value)
                # 没有变化，疑似是底层问题
                # stringLine = stringTemp也不行
                stringTemp = stringLine.replace(key,value)
                stringSource[i] = stringTemp

        a = zeroSring+''.join(stringSource).replace('\n','')
        return a 


