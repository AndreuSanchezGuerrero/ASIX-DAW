CREATE DATABASE IF NOT EXISTS aplicacio;

USE aplicacio;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `records` (
  `usuari` varchar(32) NOT NULL,
  `record` INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `records`
  ADD UNIQUE (`usuari`);

COMMIT;