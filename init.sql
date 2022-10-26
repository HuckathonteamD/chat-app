
DROP DATABASE hackathon_chatapp;
DROP USER 'hackathon_chatapp_user'@'localhost';

CREATE USER 'hackathon_chatapp_user'@'localhost' IDENTIFIED BY 'chatapp_user';
CREATE DATABASE hackathon_chatapp;
USE hackathon_chatapp
GRANT ALL PRIVILEGES ON hackathon_chatapp.* TO 'hackathon_chatapp_user'@'localhost';

CREATE TABLE users (
    uid varchar(50) PRIMARY KEY,
    user_name nvarchar(100) UNIQUE NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    created_at datetime NOT NULL,
    updated_at datetime NOT NULL
);

CREATE TABLE channels (
    id serial PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    name nvarchar(100) UNIQUE NOT NULL,
    abstract nvarchar(255),
    created_at datetime NOT NULL,
    updated_at datetime NOT NULL
);

CREATE TABLE messages (
    id serial PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at datetime NOT NULL,
    updated_at datetime NOT NULL
);

CREATE TABLE channel_users(
    id serial PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE
);

CREATE TABLE user_follow_channel(
    id serial PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE
);

CREATE TABLE master_reaction(
    id serial PRIMARY KEY,
    reaction_name varchar(100) UNIQUE NOT NULL,
    icon_pass varchar(255) UNIQUE NOT NULL,
    created_at datetime NOT NULL,
    updated_at datetime NOT NULL
);

CREATE TABLE message_reaction(
    id serial PRIMARY KEY,
    mid integer REFERENCES messages(id) ON DELETE CASCADE,
    uid varchar(50) REFERENCES users(uid),
    mrid integer REFERENCES master_reaction(id),
    created_at datetime NOT NULL,
    updated_at datetime NOT NULL
);

-- INSERT INTO users(uid, user_name, email, password)VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578');
-- INSERT INTO channels(id, uid, name, abstract)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','ぼっち部屋','テストさんの孤独な部屋です');
-- INSERT INTO messages(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', '誰かかまってください、、')