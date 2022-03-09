#Per la realització d’alguns d’aquests exercicis implementa en el MySQL la base de dades biblioteca.
CREATE SCHEMA IF NOT EXISTS biblioteca;
USE biblioteca;
CREATE TABLE IF NOT EXISTS llibres(
codi_llibre INT PRIMARY KEY,
titol VARCHAR(30),
codi_autor INT,
codi_editorial VARCHAR(30),
codi_tema VARCHAR(30),
lloc_edicio VARCHAR(30),
data_edicio DATETIME,
codi_idioma VARCHAR(15),
codi_cicle VARCHAR(15),
comentari VARCHAR(200),
num_pag INT,
foto_portada BLOB
);
CREATE TABLE IF NOT EXISTS log_llibres(
id INT PRIMARY KEY AUTO_INCREMENT,
titol VARCHAR (30),
operacio VARCHAR (30),
usuari VARCHAR (30),
data_operacio DATETIME
);
#1
