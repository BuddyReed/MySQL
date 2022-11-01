-- Query: Create 3 new dojos
INSERT INTO `dojo_and_ninjas_schema`.`dojos` (`name`) VALUES ('Burbank'), ("San Jose"), ("Sacramento");

-- Query: Delete the 3 dojos you just created
DELETE FROM `dojo_and_ninjas_schema`.`dojos` WHERE (`id` = '1');

-- Query: Create 3 more dojos
INSERT INTO `dojo_and_ninjas_schema`.`dojos` (`name`) 
VALUES ('Burbank'), ("San Jose"), ("Sacramento");

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO `dojo_and_ninjas_schema`.`ninjas` (`first_name`, `last_name`, `age`, `dojo_id`) 
VALUES ('Roayl', 'Allen', '26', '4');

-- Query: Create 3 ninjas that belong to the second dojo
 INSERT INTO `dojo_and_ninjas_schema`.`ninjas` (`first_name`, `last_name`, `age`, `dojo_id`) 
 VALUES ('John', 'Smith', '26', '5'), ("Rob", "Stark", "42", "5"), ("Dave", "Robert", "45", "5");
 
-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO `dojo_and_ninjas_schema`.`ninjas` (`first_name`, `last_name`, `age`, `dojo_id`) 
VALUES ('Rob', 'Yu', '26', '6'), ("Robert", "Smith", "42", "6"), ("Davida", "John", "46", "6");

-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas WHERE dojo_id = 4;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id = 6;

-- Query: Retrieve the last ninja's dojo

SELECT * FROM dojos WHERE id = (SELECT dojo_id FROM ninjas ORDER BY id DESC LIMIT 1);


