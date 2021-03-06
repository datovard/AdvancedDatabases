-- MySQL Script generated by MySQL Workbench
-- Wed Sep  9 00:29:42 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema target
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `target` ;

-- -----------------------------------------------------
-- Schema target
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `target` DEFAULT CHARACTER SET utf8 ;
USE `target` ;

-- -----------------------------------------------------
-- Table `target`.`rents_by_category_city_and_year`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `target`.`rents_by_category_city_and_year` ;

CREATE TABLE IF NOT EXISTS `target`.`rents_by_category_city_and_year` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `rental` INT NULL,
  `year` INT NULL,
  `category` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `target`.`rents_by_category_country_and_year`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `target`.`rents_by_category_country_and_year` ;

CREATE TABLE IF NOT EXISTS `target`.`rents_by_category_country_and_year` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `rental` INT NULL,
  `year` INT NULL,
  `category` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `target`.`money_lost_on_rentals`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `target`.`money_lost_on_rentals` ;

CREATE TABLE IF NOT EXISTS `target`.`money_lost_on_rentals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `total_copies_lost` INT NULL,
  `title` VARCHAR(45) NULL,
  `total_rental_lost` FLOAT NULL,
  `total_replacement_cost` FLOAT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `target`.`top_5_popularity_comparison`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `target`.`top_5_popularity_comparison` ;

CREATE TABLE IF NOT EXISTS `target`.`top_5_popularity_comparison` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `sakila_film_title` VARCHAR(45) NULL,
  `sakila_film_popularity` FLOAT NULL,
  `sakila_category` VARCHAR(45) NULL,
  `imdb_film_title` VARCHAR(45) NULL,
  `imdb_film_popularity` FLOAT NULL,
  `imdb_film_category` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
