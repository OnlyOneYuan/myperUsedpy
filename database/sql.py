import sqlite3 as sq
import mariadb

class lite:

    #根据站点机房编码查询
    def selectOltByRID(PortN:str):
        
        db = sq.connect('database\data.db')
        result = db.execute("select CIRCUIT_NO_PON from house where STATION_NO = \""+PortN+"\"")
        id = result.fetchall()
        db.commit()
        db.close()
        
        return id[0][0]
    
    #根据olt上联名称和端口查询
    def selectOltByPort(oname,oport):
        print(oname,oport)
        db = sq.connect('database\data.db')
        result = db.execute("select a.CIRCUIT_NO_PON from house a,dict b where (a.olt = ? and a.olt_PON_PORT = ?) or (b.olt = ? and b.olt_PON_PORT = ?)",(oname,oport,oname,oport))
        res = [i for i in result]
        print(res,result)
        db.close()
        return res[0]


class mdb:

    def __init__(self) -> None:
        self.host = '112.64.177.53'
        self.port = 3307
        self.user = 'root'
        self.password = 'Aa@123456789'
        self.db = 'EndLevel'
    #查询
    def __select__(self,saims:list):
        eid = "(%s)"%",".join([f'"{item}"' for item in saims])
        print(eid)
        conn = mariadb.Connection(
            host = self.host,
            user = self.user,
            password = self.password,
            port = self.port,
            database = self.db)
        try:
            cur = conn.cursor()    
            cur.execute(r'select * from olt where 电路编码 in %s'%eid)
            result = cur.fetchall()
            for row in result:
                print(row)
        except mariadb.err as e:
            print(e)
        finally:
            conn.close()
    #更新商客总表    
    def updateDict():
        pass


