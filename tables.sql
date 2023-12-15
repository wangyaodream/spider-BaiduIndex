CREATE DATABASE IF NOT EXISTS baidu_index_db 
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE baidu_index_db;

CREATE TABLE IF NOT EXISTS base (
    id INT AUTO_INCREMENT PRIMARY KEY,
    key_id varchar(20),
    key_field text,
    status_code varchar(10),
    remark text
);

