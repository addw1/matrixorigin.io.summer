CREATE TABLE messages (
                          id BIGINT AUTO_INCREMENT PRIMARY KEY,
                          room_id VARCHAR(255) NOT NULL,
                          from_uid BIGINT NOT NULL,
                          content TEXT NOT NULL,
                          create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);