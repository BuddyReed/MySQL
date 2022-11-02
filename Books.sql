-- Query: Change the name of the C Sharp book to C#
UPDATE books.books SET title = "C#" WHERE books.id = 9;

-- Query: Change the first name of the 4th user to Bill
UPDATE books.users SET first_name = "Bill" WHERE users.id = 9;

-- Query: Have the first user favorite the first 2 books
INSERT INTO `books`.`favorites` (`book_id`, `user_id`) VALUES ('9', '6');

-- Query: Have the second user favorite the first 3 books
INSERT INTO `books`.`favorites` (`book_id`, `user_id`) VALUES ('10', '7');
-- Query: Have the third user favorite the first 4 books
INSERT INTO `books`.`favorites` (`book_id`, `user_id`) VALUES ('11', '8');
-- Query: Have the fourth user favorite all the books
INSERT INTO `books`.`favorites` (`book_id`, `user_id`) VALUES ('1', '9'), 
('9', '9'), ('10', '9'), ('11', '9'), ('12', '9');
-- Query: Retrieve all the users who favorited the 3rd book
SELECT * FROM users JOIN favorites ON users.id = favorites.user_id JOIN books ON favorites.book_id = books.id;

-- Query: Remove the first user of the 3rd book's favorites
DELETE FROM `books`.`favorites` WHERE (`id` = '2');

-- Query: Have the 5th user favorite the 2nd book
INSERT INTO `books`.`favorites` (`book_id`, `user_id`) VALUES ('10', '9');

-- Find all the books that the 3rd user favorited
SELECT title, num_of_pages from books
JOIN favorites ON books.id = favorites.book_id
WHERE favorites.user_id = 8;

-- Query: Find all the users that favorited to the 5th book
SELECT title, num_of_pages from books
JOIN favorites ON books.id = favorites.book_id
WHERE favorites.user_id = 10;
