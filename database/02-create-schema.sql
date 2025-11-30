
CREATE TABLE user {
    username VARCHAR(64) PRIMARY KEY;
    passwrd VARCHAR(64) NOT NULL;
}

CREATE TABLE conversation {
    convo_id SERIAL PRIMARY KEY;
}

CREATE TABLE conversation_recipients {
    username VARCHAR(64);
    convo_id INT;
    FOREIGN KEY username REFERENCES user (username);
    FOREIGN KEY convo_id REFERENCES conversation (convo_id);
    PRIMARY KEY (username, convo_id);
}

CREATE TABLE message {
    message_id SERIAL PRIMARY KEY;
    message_data TEXT NOT NULL;
    message_timestamp TIMESTAMP DEFAULT NOW();
    sender VARCHAR(64) NOT NULL;
    convo_id INT NOT NULL;
    FOREIGN KEY sender REFERENCES user (username);
    FOREIGN KEY convo_id REFERENCES conversation (convo_id);
}
