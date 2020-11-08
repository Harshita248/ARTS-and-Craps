import mysql.connector


class db:
    def  __init__(self):

        self.mydb = mysql.connector.connect(
            host="35.222.183.17",
            user="root",
            password="password",
            auth_plugin='mysql_native_password',
            database="ArtsAndCraps",
            )


        self.cursor = self.mydb.cursor()

    def query(self,select, rmstr,params):
        query = "SELECT %s FROM %s %s" % (select,self.table,rmstr)
        self.cursor.execute(query,params)
        return self.cursor.fetchall()

    def insert(self,table,rmstr,params):
        query = "INSERT INTO %s VALUES %s" % (table, rmstr)
        self.cursor.execute(query,params)

    def hardinsert(self,query,params):
        self.cursor.executemany(query,params)



