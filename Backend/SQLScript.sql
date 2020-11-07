/*

*/

CREATE USER IF NOT EXISTS 'ACadmin'@'localhost' IDENTIFIED BY 'acadmin';

DROP DATABASE IF EXISTS `ArtsAndCraps`;
CREATE DATABASE IF NOT EXISTS `ArtsAndCraps`;
GRANT ALL PRIVILEGES ON `ArtsAndCraps`.* TO 'ACadmin'@'localhost';
Use `ArtsAndCraps`;

CREATE TABLE IF NOT EXISTS Arts (
    Name VARCHAR(45) NOT NULL PRIMARY KEY,
    Img LONGBLOB
);
CREATE TABLE IF NOT EXISTS Material(
   Name VARCHAR(45) NOT NULL,
   Material VARCHAR (200) NOT NULL,

  CONSTRAINT PK_Material PRIMARY KEY (Name,Material),
  FOREIGN KEY (Name) REFERENCES Arts(Name)
);

Create Table if not exists Instruction(
    Name VARCHAR(45) NOT NULL,
    Instruction VARCHAR (500) NOT NULL,
    StepNumber int NOT NULL,

    FOREIGN KEY (Name) REFERENCES Arts(Name),
    CONSTRAINT PK_Instructions PRIMARY KEY (Name,StepNumber)
);

CREATE TABLE IF NOT EXISTS Review(
    Name VARCHAR(45) NOT NULL,
    Rating int NOT NULL,
    FOREIGN KEY (Name) REFERENCES Arts(Name)
);



