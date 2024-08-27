
print(bin(int('E8A1F8C34EF9',16)))
s = "681AA4:01FFFFFFFF01:0FFF34:681AA4BC91D3:FF"
sNum = s.split(':')
for i in sNum:
    print(i,":",bin(int(i,16)))
res = int(sNum[2],16)&int(sNum[3],16)

print(hex(res))