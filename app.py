from flask import Flask, request, redirect, render_template, session, flash
from models import dbConnect
from util.user import User
from util.dateformat import dateFormat
from datetime import timedelta, datetime, timezone
import hashlib
import uuid
import re


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
    reactions = dbConnect.getReactionAll()
    messages_reaction = dbConnect.getMessageReactionAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows, reactions=reactions, messages_reaction=messages_reaction)


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
    reactions = dbConnect.getReactionAll()
    messages_reaction = dbConnect.getMessageReactionAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows, reactions=reactions, messages_reaction=messages_reaction)


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
    reactions = dbConnect.getReactionAll()
    messages_reaction = dbConnect.getMessageReactionAll(channel_id)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows, reactions=reactions, messages_reaction=messages_reaction)


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
    reactions = dbConnect.getReactionAll()
    messages_reaction = dbConnect.getMessageReactionAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows, reactions=reactions, messages_reaction=messages_reaction)


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
    reactions = dbConnect.getReactionAll()
    messages_reaction = dbConnect.getMessageReactionAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows, reactions=reactions, messages_reaction=messages_reaction)


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
        reactions = dbConnect.getReactionAll()
        messages_reaction = dbConnect.getMessageReactionAll(cid)
        return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows, reactions=reactions, messages_reaction=messages_reaction)


@app.route('/my_page')
def my_page():
    uid = session.get("uid")
    if uid is None:
        return redirect ('/login')
    else:
        user_name = dbConnect.getUserName(uid)
        if user_name is None:
            flash('ユーザー情報は本人のみ編集可能です')
            return redirect ('/')
        else:
            email = dbConnect.getUserEmail(uid)
            follow_channels = dbConnect.getFollowChannelNameAll(uid)
    return render_template('my_page.html', user_name=user_name, email=email, follow_channels=follow_channels)


@app.route('/update_mypage', methods=['POST'])
def update_userInfo():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
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
            password = hashlib.sha256(password1.encode('utf-8')).hexdigest()
            user = User(uid, name, email, password)
            # DBuser = dbConnect.getUser(email)
            # DBusername = dbConnect.getUserName(uid)
            current_date = datetime.now(timezone(timedelta(hours=9)))
            
            dbConnect.updateUserInfo(user, current_date)
            name = dbConnect.getUserName(uid)
            email = dbConnect.getUserEmail(uid)
            follow_channels = dbConnect.getFollowChannelNameAll(uid)
        return render_template('my_page.html', user_name=name, email=email, follow_channels=follow_channels)


@app.route('/reaction/<mrid>', methods=['POST'])
def add_message_reaction(mrid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    cid = request.form.get('channel_id')
    mid = request.form.get('message_id')
    current_date = datetime.now(timezone(timedelta(hours=9)))

    channel = dbConnect.getChannelById(cid)
    messages = dateFormat.getMessages(dbConnect.getMessageAll(cid))
    follows = dbConnect.getFollowById(cid)
    reactions = dbConnect.getReactionAll()

    if dbConnect.serchReaction(mid, uid, mrid):
        messages_reaction = dbConnect.getMessageReactionAll(cid)
        return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows, reactions=reactions, messages_reaction=messages_reaction)
    else:
        if mrid:
            dbConnect.createMessageReaction(mid, uid, mrid, current_date)

        messages_reaction = dbConnect.getMessageReactionAll(cid)
        return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows, reactions=reactions, messages_reaction=messages_reaction)


@app.route('/delete_reaction/<cid>/<rid>')
def delete_message_reaction(cid,rid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    if rid:
        dbConnect.deleteMessageReaction(rid)

    channel = dbConnect.getChannelById(cid)
    messages = dateFormat.getMessages(dbConnect.getMessageAll(cid))
    follows = dbConnect.getFollowById(cid)
    reactions = dbConnect.getReactionAll()
    messages_reaction = dbConnect.getMessageReactionAll(cid)
    return render_template('detail.html', messages=messages, channel=channel, uid=uid, follows=follows, reactions=reactions, messages_reaction=messages_reaction)


@app.errorhandler(404)
def show_error404(error):
    return render_template('error/404.html')


@app.errorhandler(500)
def show_error500(error):
    return render_template('error/500.html')


if __name__ == '__main__':
    app.run(debug=True)