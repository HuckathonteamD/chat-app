import pymysql
from util.DB import DB

class dbConnect:
    def createUser(user, uiid, date):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email, password, uiid, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cur.execute(sql, (user.uid, user.name, user.email, user.password, uiid, date, date))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


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


    def getUserName(user_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE user_name=%s;"
            cur.execute(sql, (user_name))
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
            sql = "SELECT m.id, u.uid, user_name, user_icon_path, message, m.created_at, m.updated_at FROM messages AS m \
                INNER JOIN users AS u ON m.uid = u.uid INNER JOIN user_icon AS i ON u.uiid = i.id WHERE cid = %s ORDER BY m.id;"
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


    def updateMessage(uid, cid, newMessage, date, mid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE messages SET uid=%s, cid=%s, message=%s, updated_at=%s WHERE id=%s;"
            cur.execute(sql, (uid, cid, newMessage, date, mid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getUserIdByMessageId(mid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT uid FROM messages WHERE id=%s;"
            cur.execute(sql, (mid))
            uid = cur.fetchone()
            return uid
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


    def getFollowerByCid(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT u.user_name, user_icon_path FROM user_follow_channel as f INNER JOIN users as u ON u.uid=f.uid \
                INNER JOIN user_icon as i ON u.uiid=i.id WHERE f.cid=%s;"
            cur.execute(sql, (cid))
            follower = cur.fetchall()
            return follower
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
    

    def getFollowChannelIdByUid(uid):
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


    def unfollowChannel(id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM user_follow_channel WHERE id=%s;"
            cur.execute(sql, (id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def unfollowChannel_i(cid, uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM user_follow_channel WHERE cid=%s and uid=%s;"
            cur.execute(sql, (cid, uid))
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
            sql = "SELECT c.name, c.abstract, u.id, u.cid FROM user_follow_channel AS u INNER JOIN channels AS c ON u.cid=c.id WHERE u.uid=%s;"
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


    def getPassword(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT password FROM users WHERE uid=%s"
            cur.execute(sql, (uid))
            password = cur.fetchone()
            return password
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close


    def getUserIcon(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT i.user_icon_path FROM users as u INNER JOIN user_icon as i ON u.uiid=i.id WHERE uid=%s"
            cur.execute(sql, (uid))
            icon = cur.fetchone()
            return icon
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close


    def getIconAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM user_icon;"
            cur.execute(sql)
            user_icons = cur.fetchall()
            return user_icons
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def updateNameEmail(new_name, new_email, date, uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET user_name=%s, email=%s, updated_at=%s WHERE uid=%s;"
            cur.execute(sql, (new_name, new_email, date, uid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def updatePassword(password, date, uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET password=%s, updated_at=%s WHERE uid=%s;"
            cur.execute(sql, (password, date, uid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def updateIcon(icon_id, date, uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET uiid=%s, updated_at=%s WHERE uid=%s;"
            cur.execute(sql, (icon_id, date, uid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getReactionAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM master_reaction;"
            cur.execute(sql)
            reactions = cur.fetchall()
            return reactions
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def createMessageReaction(mid, uid, mrid, date):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO message_reaction(mid, uid, mrid, created_at) VALUES(%s, %s, %s, %s)"
            cur.execute(sql, (mid, uid, mrid, date))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getMessageReactionAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT r.id, r.mid, m.cid, r.uid, s.reaction_name, s.icon_path FROM message_reaction AS r \
                INNER JOIN messages AS m ON r.mid = m.id INNER JOIN master_reaction AS s ON r.mrid = s.id WHERE m.cid = %s ORDER BY id;"
            cur.execute(sql, (cid))
            messages_reaction = cur.fetchall()
            return messages_reaction
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def deleteMessageReaction(rid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM message_reaction WHERE id=%s;"
            cur.execute(sql, (rid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def serchReaction(mid, uid, mrid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM message_reaction WHERE mid=%s and uid=%s and mrid=%s;"
            cur.execute(sql, (mid, uid, mrid))
            reaction = cur.fetchone()
            return reaction
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
