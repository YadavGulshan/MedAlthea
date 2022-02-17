import sqlite3


class LocalDB:
    def __init__(self):
        self.con = sqlite3.connect("token.sqlite3")
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
            "INSERT INTO tokens VALUES (?,datetime('now'), ?, datetime('now'))",
            (refresh, access),
        )
        self.con.commit()
        print("Token Added! ✅")
        return 200

    def getAccessToken(self):
        response = self.cur.execute("""SELECT accesstoken, Alastused FROM tokens""")
        self.con.commit()
        return response.fetchall()[0]

    def updateAccessToken(self, access):
        self.cur.execute(
            """UPDATE tokens SET accesstoken = ?, Alastused=datetime('now')""", access
        )
        self.con.commit()

    def getRefreshToken(self):
        response = self.cur.execute("""SELECT refresh, Rlastused FROM tokens""")
        self.con.commit()
        return response.fetchall()[0]

    def getTokens(self):
        response = self.cur.execute('''SELECT * FROM tokens''')
        self.con.commit()
        return response.fetchall()


