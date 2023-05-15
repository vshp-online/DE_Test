CREATE SCHEMA IF NOT EXISTS `test_db` DEFAULT CHARACTER SET utf8 ;
USE `test_db` ;

CREATE TABLE IF NOT EXISTS `test_db`.`projects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
;

CREATE TABLE IF NOT EXISTS `test_db`.`people` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `projects_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_people_projects_idx` (`projects_id` ASC) VISIBLE,
  CONSTRAINT `fk_people_projects`
    FOREIGN KEY (`projects_id`)
    REFERENCES `test_db`.`projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;

INSERT INTO `test_db`.`projects` (`title`) VALUES ('First Project');
INSERT INTO `test_db`.`projects` (`title`) VALUES ('Second Project');

INSERT INTO `test_db`.`people` (`name`, `projects_id`) VALUES ('Ivan', '1');
INSERT INTO `test_db`.`people` (`name`, `projects_id`) VALUES ('Petya', '2');
INSERT INTO `test_db`.`people` (`name`, `projects_id`) VALUES ('Vasya', '2');
