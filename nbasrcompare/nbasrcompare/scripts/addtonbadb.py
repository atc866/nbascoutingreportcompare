#class will allow for interaction with mysql database/table
#main functions will be get and set
import mysql.connector
class srdb:
    def __init__(self,hosti,useri,passwordi,databasei):
        self.dbconnect = mysql.connector.connect(
            host=hosti,
            user=useri,
            password=passwordi,
            database=databasei
        )
        self.cursor=self.dbconnect.cursor()
    def set(self,playername,s,w,n):
        add_sr=("INSERT INTO players"
                "(name, strengths, weaknesses, other)"
                "VALUES (%s, %s, %s, %s)")
        info_sr=(playername,s,w,n)
        self.cursor.execute(add_sr,info_sr)
        print(playername+" successfully inserted")
    def get(self,playername):
        query=("SELECT * FROM players WHERE name = %s")
        self.cursor.execute(query,(playername,))
        rvdict={}
        for (name, strengths, weaknesses, other) in self.cursor:
            rvdict['name']=name
            rvdict['strengths']=strengths
            rvdict['weaknesses']=weaknesses
            rvdict['other notes']=other
        return rvdict
    def commit(self):
        self.dbconnect.commit()
    def close(self):
        self.cursor.close()
        self.dbconnect.close()

        

    
