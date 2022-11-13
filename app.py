import hashlib
import re
import uuid
from datetime import datetime, timedelta, timezone

from flask import Flask, flash, redirect, render_template, request, session

from models import dbConnect
from util.dateformat import dateFormat
from util.user import User

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
    else:
        uid = uuid.uuid4()
        password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
        user = User(uid, name, email, password)
        DBuser = dbConnect.getUser(email)
        DBusername = dbConnect.getUserName(name)
        current_date = datetime.now(timezone(timedelta(hours=9)))

        if DBuser != None or DBusername != None:
            flash('既に登録されているようです')
        else:
            dbConnect.createUser(user,current_date)
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
    return render_template('index.html', channels=channels, uid=uid)


@app.route('/', methods=['POST'])
def add_channel():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    channel_name = request.form.get('channel-title')
    channel = dbConnect.getChannelByName(channel_name)
    if channel == None:
        channel_description = request.form.get('channel-description')
        current_date = datetime.now(timezone(timedelta(hours=9)))
        dbConnect.addChannel(uid, channel_name, channel_description, current_date)
        return redirect('/')
    else:
        error = '既に同じチャンネルが存在しています'
        return render_template('error/error.html', error_message=error)


@app.route('/delete/<cid>')
def delete_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelById(cid)
        if channel["uid"] != uid:
            flash('チャンネルは作成者のみ削除可能です')
            return redirect ('/')
        else:
            dbConnect.deleteChannel(cid)
            channels = dbConnect.getChannelAll()
            return render_template('index.html', channels=channels, uid=uid)


# uidもmessageと一緒に返す
@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dateFormat.getMessages(dbConnect.getMessageAll(cid))
    follows = dbConnect.getFollowById(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows)


@app.route('/update_channel', methods=['POST'])
def update_channel():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = request.form.get('cid')
    channel_name = request.form.get('channel-title')
    channel_description = request.form.get('channel-description')
    current_date = datetime.now(timezone(timedelta(hours=9)))

    dbConnect.updateChannel(uid, channel_name, channel_description, current_date, cid)
    channel = dbConnect.getChannelById(cid)
    messages = dateFormat.getMessages(dbConnect.getMessageAll(cid))
    follows = dbConnect.getFollowById(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows)


@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    message = request.form.get('message')
    channel_id = request.form.get('channel_id')
    current_date = datetime.now(timezone(timedelta(hours=9)))

    if message:
        dbConnect.createMessage(uid, channel_id, message, current_date)

    channel = dbConnect.getChannelById(channel_id)
    messages = dateFormat.getMessages(dbConnect.getMessageAll(channel_id))
    follows = dbConnect.getFollowById(channel_id)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows)


@app.route('/delete_message', methods=['POST'])
def delete_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    mid = request.form.get('message_id')
    cid = request.form.get('channel_id')
    if mid:
        dbConnect.deleteMessage(mid)

    channel = dbConnect.getChannelById(cid)
    messages = dateFormat.getMessages(dbConnect.getMessageAll(cid))
    follows = dbConnect.getFollowById(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows)


@app.route('/update_message', methods=['POST'])
def update_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = request.form.get('cid')
    mid = request.form.get('mid')
    message = request.form.get('update-message')
    current_date = datetime.now(timezone(timedelta(hours=9)))

    message_uid = dbConnect.getUserIdByMessageId(mid)
    if message_uid["uid"] == uid:
        dbConnect.updateMessage(uid, cid, message, current_date, mid)
    channel = dbConnect.getChannelById(cid)
    messages = dateFormat.getMessages(dbConnect.getMessageAll(cid))
    follows = dbConnect.getFollowById(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows)


@app.route('/follow/<cid>')
def follow_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        follows = dbConnect.getFollowById(cid)
        for follow in follows:
            if follow["uid"] == uid:
                flash('既にフォロー済みです')
                return redirect ('/')
        
        dbConnect.followChannel(uid, cid)
        channel = dbConnect.getChannelById(cid)
        messages = dateFormat.getMessages(dbConnect.getMessageAll(cid))
        follows = dbConnect.getFollowById(cid)

        return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows)


@app.route('/unfollow_channel/<id>')
def unfollow_channel(id):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        dbConnect.unfollowChannel(id)
        name = dbConnect.getUserName(uid)
        email = dbConnect.getUserEmail(uid)
        follow_channels = dbConnect.getFollowChannelAll(uid)
        return render_template('my_page.html', name=name, email=email, follow_channels=follow_channels)


@app.route('/my_page')
def my_page():
    uid = session.get("uid")
    if uid is None:
        return redirect ('/login')
    else:
        name = dbConnect.getUserName(uid)
        if name is None:
            flash('ユーザー情報は本人のみ編集可能です')
            session.clear()
            return redirect ('/login')
        else:
            email = dbConnect.getUserEmail(uid)
            follow_channels = dbConnect.getFollowChannelAll(uid)
            return render_template('my_page.html', name=name, email=email, follow_channels=follow_channels)


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

        name_old = dbConnect.getUserName(uid)
        email_old = dbConnect.getUserEmail(uid)
        follow_channels = dbConnect.getFollowChannelNameAll(uid)

        if name == '' or email =='' or password1 == '':
            flash('変更できませんでした。空のフォームがあるようです。')
            return render_template('my_page.html', name=name_old, email=email_old, follow_channels=follow_channels)
        elif password1 != password2:
            flash('変更できませんでした。パスワードの値が違っています。')
            return render_template('my_page.html', name=name_old, email=email_old, follow_channels=follow_channels)
        elif re.match(pattern, email) is None:
            flash('変更できませんでした。正しいメールアドレスの形式ではありません。')
            return render_template('my_page.html', name=name_old, email=email_old, follow_channels=follow_channels)
        else:
            current_date = datetime.now(timezone(timedelta(hours=9)))
            dbConnect.updateNameEmail(name, email, current_date, uid)
            new_name = dbConnect.getUserName(uid)
            new_email = dbConnect.getUserEmail(uid)
            flash('更新しました')
            return render_template('my_page.html', name=new_name, email=new_email, follow_channels=follow_channels)


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

        name = dbConnect.getUserName(uid)
        email = dbConnect.getUserEmail(uid)
        follow_channels = dbConnect.getFollowChannelNameAll(uid)

        if old_password == '' or password1 == '' or password2 == '':
            flash('変更できませんでした。空のフォームがあるようです。')
            return render_template('my_page.html', name=name, email=email, follow_channels=follow_channels)

        elif old_password != password_confirmation:
            flash('変更できませんでした。現在のパスワードが間違っています。')
            return render_template('my_page.html', name=name, email=email, follow_channels=follow_channels)
        elif password1 != password2:
            flash('変更できませんでした。新しいパスワードの値が違っています。')
            return render_template('my_page.html', name=name, email=email, follow_channels=follow_channels)
        else:
            date = datetime.now(timezone(timedelta(hours=9)))
            password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
            dbConnect.updatePassword(password, date, uid)
            flash('パスワードを変更しました')
            return render_template('my_page.html', name=name, email=email, follow_channels=follow_channels)


@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')


@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')


if __name__ == '__main__':
    app.run(debug=True)