CREATE DATABASE IF NOT EXISTS escuela;

USE escuela;

CREATE TABLE if not exists alumnos(
    id_persona int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(100) NOT NULL,
    ap_uno varchar(100) NOT NULL,
    ap_dos varchar(100) NOT NULL,
    matricula char(10) NOT NULL,
    edad tinyint(3) NOT NULL,
    genero varchar(9) NOT NULL,
    estado_civil varchar(11) NOT NULL,
    fec_nac varchar(10) NOT NULL
) ENGINE= InnoDB DEFAULT CHARSET=latin1;

INSERT INTO alumnos(nombre,ap_uno,ap_dos,matricula,edad,genero,estado_civil,fec_nac)
VALUES
('Arturo', 'Juarez', 'Sanchez', "1718110001",'18', "masculino","soltero","1999-05-05"),
('Juan', 'Perez', 'Hernandez', "1718110002",'18', "masculino","soltero","1999-05-06");

CREATE USER 'user_alumnos'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON escuela.* TO 'user_alumnos'@'localhost';
FLUSH PRIVILEGES;