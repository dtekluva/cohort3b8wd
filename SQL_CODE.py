##### CREATE A DATABASE CALLED STORE
CREATE database store

#### SELECT ALL COLUMNS FROM A TABLE CALLED cohort4norm

SELECT * FROM `cohort4norm`

######## CREATE A TABLE WITH THE NAME PRODUCTS THAT HAS A PRIMARY KEY ID

CREATE TABLE products (id INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL, 
                        name CHAR(50), 
                        qty INT(5), 
                        price INT(5)
                        )

### CREATE A TABLE TRANSACTIONS WITH FOREIGN_KEY RELATIONSHIP TO PRODUCT AND CUSTOMER

CREATE TABLE transactions (id INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL, 
                       			customer_id INT(5),
                       			product_id INT(5),
                       			qty INT(5), 
                       			_date DATE(),
                          		FOREIGN KEY (customer_id) REFERENCES customers(id),
                           		FOREIGN KEY (product_id) REFERENCES products(id)
                          )

##### INSERT MULTIPLE INTO FOREIGN_KEY TABLE

INSERT INTO transactions (customer_id, product_id, qty, _date) VALUES(1, 2, 5, "2020-03-15"), (2, 2, 4, "2020-04-15"), (1, 1, 1, "2020-03-16")


############ CLASS COMMANDS

drop database univelcity
CREATE DATABASE univelcity
USE univelcity
USE univelcity
USE jumia
USE jumia
SELECT * FROM `phones`
SELECT * FROM `continents`
CREATE TABLE cohort4 (id INT(3), name CHAR(50), git_name CHAR(50))
INSERT INTO cohort4 (id, name, git_name) VALUES(1, "Atha", "dtekluva")
SELECT id, name, git_name FROM cohort4
SELECT * FROM `cohort4`
CREATE TABLE cohort4norm (id INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL, name CHAR(50), git_name CHAR(50))
INSERT INTO cohort4 ( name, git_name) VALUES( "Yale", "sothebys")
SELECT * FROM `cohort4norm`
SELECT * FROM `cohort4`
INSERT INTO cohort4norm ( name, git_name) VALUES( "Yale", "sothebys")
SELECT * FROM `cohort4norm`
INSERT INTO cohort4 ( name, git_name) VALUES( "Winston", "sothebys")
SELECT * FROM `cohort4norm`
INSERT INTO cohort4norm ( name, git_name) VALUES( "Winston", "Hamptons")
SELECT * FROM `cohort4norm`
SELECT * FROM `cohort4norm`
CREATE TABLE products (id INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL, name CHAR(50), qty INT(5), price INT(5))
CREATE database store
use store
CREATE TABLE products (id INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL, name CHAR(50), qty INT(5), price INT(5))
CREATE TABLE customers (id INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL, name CHAR(50), email CHAR(50))
CREATE TABLE transactions (id INT(3) PRIMARY KEY AUTO_INCREMENT NOT NULL, customer_id INT(5), product_id INT(5), qty INT(5), _date DATE, FOREIGN KEY (customer_id) REFERENCES customers(id), FOREIGN KEY (product_id) REFERENCES products(id) )
INSERT INTO customers (name, email) VALUES("johnny", "rockets@gmail.com")
INSERT INTO customers (name, email) VALUES("whinnie", "whinie@gmail.com")
SELECT * FROM `customers`
INSERT INTO products (name, price, qty) VALUES("shoes", 500, 6)
INSERT INTO products (name, price, qty) VALUES("bags", 1400, 5)
SELECT * FROM `products`
Expand Requery Edit Explain Profiling Bookmark Database : store Queried time : 15:38:44
SELECT * FROM `customers`


#ASSIGNMENT
In the store database created try to pull out the transactions such that the result carries the actual names and details of products and customers instead of the FOREIGN_KEY id. 

NOTE*** This can be achieved using the join keyword.