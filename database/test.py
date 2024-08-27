import mariadb

con = mariadb.connect(user=r"viewer",password=r"Aa@123456789",
                      host=r"112.64.177.53",port=3307,database=r"EndLevel")
print(con)
cur = con.cursor()    
cur.execute(r'select * from olt where 电路编码 in ("21D383414", "21D342439", "21D325164", "21D310393", "21D285675")')
result = cur.fetchall()
print(cur)
for row in result:
    print(row)
