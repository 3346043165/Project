import pymysql
class shujukucun():
    def __init__(self,user,password,database,host,port):
        self.con=pymysql.connect(user=user,password=password,database=database,host=host,port=port)
        self.cur=self.con.cursor()
    def db_shuju(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()
    def close(self):
        self.cur.close()
        self.con.close()