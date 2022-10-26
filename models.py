import pymysql
from util.DB import DB

class dbConnect:
    def createUser(user,date):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email, password, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s);"
            cur.execute(sql, (user.uid, user.name, user.email, user.password, date, date))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getUserId(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT uid FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            id = cur.fetchone()
            return id
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close


    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close


    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
