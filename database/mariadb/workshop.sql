CREATE DATABASE IF NOT EXISTS workshop;

CREATE TABLE `users` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(50) UNIQUE NOT NULL,
  `password` varchar(36) NOT NULL,
  `created_at` timestamp DEFAULT (now())
);

CREATE TABLE `conversation` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `status` ENUM ('online', 'deleted'),
  `user_id` integer NOT NULL,
  `created_at` timestamp DEFAULT (now())
);

CREATE TABLE `posts` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `prompt` text NOT NULL COMMENT 'Content of the user prompt',
  `body` text NOT NULL COMMENT 'Answer of the LLM',
  `conversation_id` integer NOT NULL,
  `created_at` timestamp DEFAULT (now())
);

ALTER TABLE `conversation` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

ALTER TABLE `posts` ADD FOREIGN KEY (`conversation_id`) REFERENCES `conversation` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;
  

INSERT INTO `users` (`username`, `password`) VALUES ('admin', 'password');