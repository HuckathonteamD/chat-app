
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
    uiid BIGINT UNSIGNED,
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
    cid BIGINT UNSIGNED ,
    message text,
    created_at datetime NOT NULL,
    updated_at datetime NOT NULL,
    FOREIGN KEY (cid) REFERENCES channels(id) ON DELETE CASCADE
);

CREATE TABLE channel_users(
    id serial PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid BIGINT UNSIGNED,
    FOREIGN KEY (cid) REFERENCES channels(id) ON DELETE CASCADE
);

CREATE TABLE user_follow_channel(
    id serial PRIMARY KEY,
    uid varchar(50) REFERENCES users(uid),
    cid BIGINT UNSIGNED,
    FOREIGN KEY (cid) REFERENCES channels(id) ON DELETE CASCADE
);

CREATE TABLE master_reaction(
    id serial PRIMARY KEY,
    reaction_name nvarchar(100) UNIQUE NOT NULL,
    icon_path varchar(255) UNIQUE NOT NULL
);

CREATE TABLE message_reaction(
    id serial PRIMARY KEY,
    mid BIGINT UNSIGNED,
    uid varchar(50) REFERENCES users(uid),
    mrid BIGINT UNSIGNED,
    created_at datetime NOT NULL,
    FOREIGN KEY (mid) REFERENCES messages(id) ON DELETE CASCADE,
    FOREIGN KEY (mrid) REFERENCES master_reaction(id) ON DELETE CASCADE
);

CREATE TABLE user_icon(
    id serial PRIMARY KEY,
    user_icon_name nvarchar(100) UNIQUE NOT NULL,
    user_icon_path varchar(255) UNIQUE NOT NULL
);

INSERT INTO master_reaction(reaction_name, icon_path) VALUES('iine','img/reaction/iine.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('arigatougozaimasu','img/reaction/arigatougozaimasu.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('otsukaresamadesu','img/reaction/otukaresamadesu.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('shouchishimashita','img/reaction/shoutishimashita.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('yoroshikuonegaishimasu','img/reaction/yoroshikuonegaishimasu.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('subarashiidesu','img/reaction/subarashiidesu.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('sutekidesu','img/reaction/sutekidesu.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('mondainashi','img/reaction/mondainasi.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('shiranakatta','img/reaction/siranakatta.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('douidesu','img/reaction/douidesu.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('kanzendoui','img/reaction/kanzendoui.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('kanzenrikai','img/reaction/kanzenrikai.png');
INSERT INTO master_reaction(reaction_name, icon_path) VALUES('kami','img/reaction/kami.png');

INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('userIcon','img/user-icon/userIcon.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('apple','img/user-icon/apple.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('chinese-cabbage','img/user-icon/chinese-cabbage.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('corn','img/user-icon/corn.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('lemon','img/user-icon/lemon.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('orange','img/user-icon/orange.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('peach','img/user-icon/peach.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('pineapple','img/user-icon/pineapple.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('pumpkin','img/user-icon/pumpkin.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('spinach','img/user-icon/spinach.png');
INSERT INTO user_icon(user_icon_name, user_icon_path) VALUES('straberry','img/user-icon/straberry.png');