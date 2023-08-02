
CREATE DATABASE IF NOT EXISTS `Django_community`;
USE `Django_community`;

CREATE TABLE IF NOT EXISTS `Post` (
  `no` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` varchar(50) NOT NULL,
  `created_at` date NOT NULL,
  `update_at` date NOT NULL,
  `author` varchar(50) NOT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
