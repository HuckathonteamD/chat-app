import pymysql
from util.crypto_dec import crypto_dec

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host=crypto_dec.getdec()["DBH"],
            db=crypto_dec.getdec()["DB"],
            user=crypto_dec.getdec()["DBU"],
            password=crypto_dec.getdec()["DBP"],
            charset=crypto_dec.getdec()["DBC"],
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()