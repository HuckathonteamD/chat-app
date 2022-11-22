import pymysql
from util.crypto_dec import crypto_dec

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="localhost",
            db=crypto_dec.getdec()["DB"],
            user=crypto_dec.getdec()["DBU"],
            password=crypto_dec.getdec()["DBP"],
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()