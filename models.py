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


    # 最終的に使用されていなければ削除
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


    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def addChannel(uid, newChannelName, newChannelDescription, date):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels (uid, name, abstract, created_at, updated_at) VALUES (%s, %s, %s, %s, %s);"
            cur.execute(sql, (uid, newChannelName, newChannelDescription, date, date))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def deleteChannel(cid):
        try: 
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getMessageAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT id, u.uid, user_name, message, m.updated_at FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def updateChannel(uid, newChannelName, newChannelDescription, date, cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s, updated_at=%s WHERE id=%s;"
            cur.execute(sql, (uid, newChannelName, newChannelDescription, date , cid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def createMessage(uid, cid, message, date):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, message, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)"
            cur.execute(sql, (uid, cid, message, date, date))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def deleteMessage(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM messages WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getFollowById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM user_follow_channel WHERE cid=%s;"
            cur.execute(sql, (cid))
            follows = cur.fetchall()
            return follows
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
    

    def followChannel(uid, cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO user_follow_channel(uid, cid) VALUES(%s, %s)"
            cur.execute(sql, (uid, cid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
    

    def getFollowChannelAll(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT cid FROM user_follow_channel WHERE uid=%s;"
            cur.execute(sql, (uid))
            follow_channels = cur.fetchall()
            return follow_channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getUserName(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT user_name FROM users WHERE uid=%s;"
            cur.execute(sql,(uid))
            user_name = cur.fetchone()
            return user_name
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getUserEmail(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT email FROM users WHERE uid=%s;"
            cur.execute(sql,(uid))
            email = cur.fetchone()
            return email
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()