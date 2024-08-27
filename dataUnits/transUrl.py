#格式处理类

def urlOnSearch(id:int,sname:str) -> str:
    pass

def initHeaderFromTxt(hpath:str):
    hjson = []
    with open(hpath,'r',encoding='utf-8-sig') as f:
        head = f.readlines()
        for i in head:
            i = i.strip('\n')
            if i == "":
                continue
            line = i.split(":",1)
            line[0] = line[0].strip()
            line[1] = line[1].strip()
            hjson.append(line)
            header = {hed[0]:hed[1] for hed in hjson}

    return header
    pass
