import os
import sqlite3
from datetime import datetime


class LocalDB:
    def __init__(self, name):
        pathToHome = os.path.expanduser('~')
        self.con = sqlite3.connect(pathToHome+"/{}.sqlite3".format(name))
        self.cur = self.con.cursor()
        self.cur.execute(
            """
        CREATE TABLE IF NOT EXISTS tokens 
        (refresh text, Rlastused text, accesstoken text, Alastused text )
        """
        )

    def addNewToken(self, access, refresh):
        self.cur.execute("""DELETE FROM tokens""")
        self.cur.execute(
            "INSERT INTO tokens VALUES (?,?, ?, ?)",
            (refresh, datetime.now(), access, datetime.now()),
        )
        self.con.commit()
        return 200

    def getAccessToken(self):
        response = self.cur.execute("""SELECT accesstoken, Alastused FROM tokens""")
        self.con.commit()
        return response.fetchall()

    def getRefreshToken(self):
        response = self.cur.execute("""SELECT refresh, Rlastused FROM tokens""")
        self.con.commit()
        return response.fetchall()

    def getTokens(self):
        response = self.cur.execute('''SELECT * FROM tokens''')
        self.con.commit()
        return response.fetchall()

    def getLogout(self):
        self.cur.execute('''DROP table tokens''')
        self.con.commit()
        print("LOG OUT!!")
