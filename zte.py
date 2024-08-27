from url_cookies import ZTE

z = ZTE()
s = "E8A1F8:01FFFFFFFF01:1FFF23:E8A1F8C34EF9:06"
sNum = s.split(':')
print(sNum)
check = ["74694A034CBA"]
mac = []
for i in check:
    ma = z.checkBidByMac(i)
    print(ma.text)
    mac.append(ma)
