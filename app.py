from flask import Flask, flash, redirect, render_template, url_for, request, session
from models import dbConnect
from util.user import User
from util.crypto_dec import crypto_dec
from datetime import datetime, timedelta, timezone
import hashlib
import uuid
import re
import random


app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.permanent_session_lifetime = timedelta(days=3)


@app.route('/signup')
def signup():
    return render_template('registration/signup.html')


@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if name == '' or email =='' or password1 == '' or password2 == '':
        flash('空のフォームがあるようです')
    elif password1 != password2:
        flash('二つのパスワードの値が違っています')
    elif re.match(pattern, email) is None:
        flash('正しいメールアドレスの形式ではありません')
    elif len(name)>100 or len(email)>255 or len(password1)>255:
        flash('入力値の文字数制限を超えています')
    else:
        uid = uuid.uuid4()
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        user = User(uid, name, email, password)
        DBuser = dbConnect.getUser(email)
        DBusername = dbConnect.getUserName(name)
        current_date = datetime.now(timezone(timedelta(hours=9)))
        uiid = random.randrange(2,11)

        if DBuser != None or DBusername != None:
            flash('既に登録されているようです')
        else:
            dbConnect.createUser(user, uiid, current_date)
            UserId = str(uid)
            session['uid'] = UserId
            return redirect('/')
    return redirect('/signup')


@app.route('/login')
def login():
    return render_template('registration/login.html')


@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email =='' or password == '':
        flash('空のフォームがあるようです')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            hashPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashPassword != user["password"]:
                flash('パスワードが間違っています！')
            else:
                session['uid'] = user["uid"]
                return redirect('/')
    return redirect('/login')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/')
def index():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channels = dbConnect.getChannelAll()
        follow_channels = dbConnect.getFollowChannelIdByUid(uid)
        return render_template('index.html', channels=channels, uid=uid, follow_channels=follow_channels)


@app.route('/', methods=['POST'])
def add_channel():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    channel_name = request.form.get('channel-title')
    channel_description = request.form.get('channel-description')
    channel = dbConnect.getChannelByName(channel_name)
    if channel_name == "":
        error = 'チャンネル名が空白です'
        return render_template('error/error.html', error_message=error)
    if len(channel_name)>100 or len(channel_description)>255:
        error = '入力値の文字数制限を超えています'
        return render_template('error/error.html', error_message=error)
    elif channel == None and channel_name:
        current_date = datetime.now(timezone(timedelta(hours=9)))
        dbConnect.addChannel(uid, channel_name, channel_description, current_date)
        return redirect('/')
    else:
        error = '既に同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error)


@app.route('/delete/<int:cid>')
def delete_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelById(cid)
        if channel["uid"] != uid:
            error = 'チャンネルは作成者のみ削除可能です'
            return render_template('error/error.html', error_message=error)
        else:
            dbConnect.deleteChannel(cid)
            return redirect ('/')


# uidもmessageと一緒に返す
@app.route('/detail/<int:cid>')
def detail(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    # follows = dbConnect.getFollowById(cid) 
    reactions = dbConnect.getReactionAll()
    messages_reaction = dbConnect.getMessageReactionAll(cid)
    followers = dbConnect.getFollowerByCid(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, reactions=reactions, messages_reaction=messages_reaction, followers=followers)


@app.route('/update_channel', methods=['POST'])
def update_channel():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = request.form.get('cid')
    channel_name = request.form.get('channel-title')
    channel_description = request.form.get('channel-description')
    current_date = datetime.now(timezone(timedelta(hours=9)))

    if channel_name == "":
        flash('空のフォームがあるようです')
        return redirect(url_for('detail',cid=cid))
    elif len(channel_name)>100 or len(channel_description)>255:
        flash('入力値の文字数制限を超えています')
        return redirect(url_for('detail',cid=cid))
    elif channel_name != "" and request.method == 'POST':
        dbConnect.updateChannel(uid, channel_name, channel_description, current_date, cid)

    return redirect(url_for('detail',cid=cid))


@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    message = request.form.get('message')
    cid = request.form.get('channel_id')
    current_date = datetime.now(timezone(timedelta(hours=9)))

    if len(message)>30000:
        flash('入力値の文字数制限を超えています')
        return redirect(url_for('detail',cid=cid))
    if message and request.method == 'POST':
        dbConnect.createMessage(uid, cid, message, current_date)

    return redirect(url_for('detail',cid=cid))


@app.route('/delete_message', methods=['POST'])
def delete_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    mid = request.form.get('message_id')
    cid = request.form.get('channel_id')
    if mid and request.method == 'POST':
        dbConnect.deleteMessage(mid)

    return redirect(url_for('detail',cid=cid))


@app.route('/update_message', methods=['POST'])
def update_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = request.form.get('cid')
    mid = request.form.get('mid')
    message = request.form.get('update-message')
    current_date = datetime.now(timezone(timedelta(hours=9)))

    if len(message)>30000:
        flash('入力値の文字数制限を超えています')
        return redirect(url_for('detail',cid=cid))
    message_uid = dbConnect.getUserIdByMessageId(mid)
    if message_uid["uid"] == uid and message and request.method == 'POST':
        dbConnect.updateMessage(uid, cid, message, current_date, mid)

    return redirect(url_for('detail',cid=cid))


# ホーム画面でチャンネルフォロー
@app.route('/follow_channel_i/<int:cid>')
def follow_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        follows = dbConnect.getFollowById(cid)
        for follow in follows:
            if follow["uid"] == uid:
                error = '既にフォロー済みです'
                return render_template('error/error.html', error_message=error)
        if cid:
            dbConnect.followChannel(uid, cid)

        return redirect ('/')   


# マイページでチャンネルフォロー解除
@app.route('/unfollow_channel/<int:id>')
def unfollow_channel(id):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        if id:
            dbConnect.unfollowChannel(id)
        return redirect('/my_page')


# ホーム画面でチャンネルフォロー解除
@app.route('/unfollow_channel_i/<int:cid>')
def unfollow_channel_i(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        if cid:
            dbConnect.unfollowChannel_i(cid, uid)
        return redirect ('/')


@app.route('/my_page')
def my_page():
    uid = session.get("uid")
    if uid is None:
        return redirect ('/login')
    else:
        name = dbConnect.getUserName(uid)
        if name is None:
            flash('マイページは本人のみ閲覧可能です')
            session.clear()
            return redirect ('/login')
        else:
            email = dbConnect.getUserEmail(uid)
            icon = dbConnect.getUserIcon(uid)
            icon_all = dbConnect.getIconAll()
            follow_channels = dbConnect.getFollowChannelAll(uid)
            return render_template('my_page.html', name=name, email=email, icon=icon, icon_all=icon_all, follow_channels=follow_channels)


@app.route('/update_name_email')
def get_update_name_email():
    return redirect('/my_page')


@app.route('/update_name_email', methods=['POST'])
def update_name_email():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        password1 = request.form.get('password')
        password1 = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        password2 = dbConnect.getPassword(uid)['password']

        pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if name == '' or email =='' or password1 == '':
            flash('変更できませんでした。空のフォームがあるようです。')
            return redirect('/my_page')
        elif password1 != password2:
            flash('変更できませんでした。パスワードの値が違っています。')
            return redirect('/my_page')
        elif re.match(pattern, email) is None:
            flash('変更できませんでした。正しいメールアドレスの形式ではありません。')
            return redirect('/my_page')
        elif len(name)>100 or len(email)>255 or len(password1)>255:
            flash('入力値の文字数制限を超えています')
            return redirect('/my_page')
        else:
            current_date = datetime.now(timezone(timedelta(hours=9)))
            dbConnect.updateNameEmail(name, email, current_date, uid)
            flash('更新しました')
            return redirect('/my_page')


@app.route('/update_password')
def get_update_password():
    return redirect('/my_page')


@app.route('/update_password', methods=['POST'])
def update_password():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        old_password = hashlib.sha256((request.form.get('old_password')).encode('utf-8')).hexdigest()
        password_confirmation = dbConnect.getPassword(uid)['password']
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if old_password == '' or password1 == '' or password2 == '':
            flash('変更できませんでした。空のフォームがあるようです。')
            return redirect('/my_page')
        elif old_password != password_confirmation:
            flash('変更できませんでした。現在のパスワードが間違っています。')
            return redirect('/my_page')
        elif password1 != password2:
            flash('変更できませんでした。新しいパスワードの値が違っています。')
            return redirect('/my_page')
        elif len(password1)>255:
            flash('入力値の文字数制限を超えています')
            return redirect('/my_page')
        else:
            current_date = datetime.now(timezone(timedelta(hours=9)))
            password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
            dbConnect.updatePassword(password, current_date, uid)
            flash('パスワードを変更しました')
            return redirect('/my_page')


@app.route('/update_icon')
def get_update_icon():
    return redirect('/my_page')


@app.route('/update_icon', methods=['POST'])
def update_icon():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        icon_id = request.form.get('icon_id')
        if int(icon_id)<2 or 11<int(icon_id):
            flash('アイコンを変更できませんでした')
            return redirect('/my_page')
        current_date = datetime.now(timezone(timedelta(hours=9)))
        if icon_id and request.method == 'POST':
            dbConnect.updateIcon(icon_id, current_date, uid)
            flash('アイコンを変更しました')
        return redirect('/my_page')


@app.route('/reaction', methods=['POST'])
def add_message_reaction():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = request.form.get('channel_id')
    mid = request.form.get('message_id')
    mrid = request.form.get('reaction_id')
    current_date = datetime.now(timezone(timedelta(hours=9)))

    if dbConnect.serchReaction(mid, uid, mrid):
        return redirect(url_for('detail',cid=cid))
    elif int(mrid)<1 or 13<int(mrid):
        return redirect(url_for('detail',cid=cid))
    else:
        if mrid and request.method == 'POST':
            dbConnect.createMessageReaction(mid, uid, mrid, current_date)

        channel = dbConnect.getChannelById(cid)
        messages = dbConnect.getMessageAll(cid)
        reactions = dbConnect.getReactionAll()
        messages_reaction = dbConnect.getMessageReactionAll(cid)
        followers = dbConnect.getFollowerByCid(cid)
        return render_template('detail.html', messages=messages, channel=channel, uid=uid, reactions=reactions, messages_reaction=messages_reaction, followers=followers)


@app.route('/delete_reaction/<int:cid>/<int:rid>')
def delete_message_reaction(cid,rid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    if cid and rid:
        dbConnect.deleteMessageReaction(rid)

    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)
    reactions = dbConnect.getReactionAll()
    messages_reaction = dbConnect.getMessageReactionAll(cid)
    followers = dbConnect.getFollowerByCid(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, reactions=reactions, messages_reaction=messages_reaction, followers=followers)


@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')


@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')


@app.route('/google_login')
def google_login():
    return render_template('registration/google-login.html')


# @app.before_request
# def before_request():
#     if not request.is_secure:
#         url = request.url.replace('http://', 'https://', 1)
#         code = 301
#         return redirect(url, code=code)


if __name__ == '__main__':

    # import ssl
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # ssl_context.load_cert_chain(
    # crypto_dec.getdec()["SSLFULL"], crypto_dec.getdec()["SSLPRI"]
    # )
    # app.run(debug=False,host='0.0.0.0',port=443 ,threaded='True' ,ssl_context=ssl_context)

    app.run(debug=True)