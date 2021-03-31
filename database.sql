-------------------------
-----   Pet Hotel   -----
-------------------------

-- database name: pet_hotel

-- Drop Tables
--- Delete "owners" table
DROP TABLE IF EXISTS "owners" CASCADE;

--- Delete "pets" table
DROP TABLE IF EXISTS "pets";

-- Create Tables
--- Create "owners" table
CREATE TABLE "owners" (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(64)
);

--- Create "pets" table
CREATE TABLE "pets" (
	"id" SERIAL PRIMARY KEY,
	"owners_id" INT REFERENCES "owners" ON DELETE CASCADE,
	"name" VARCHAR(64),
	"breed" VARCHAR(64),
	"color" VARCHAR(64),
	"checked_in" BOOLEAN DEFAULT TRUE,
	"checked_in_date" DATE
);

-- Populate Tables with Test Data
--- "owners" table data
INSERT INTO "owners"
	("name")
VALUES
	('Fowsia'),
	('McKynlee'),
	('Michael'),
	('William');
	
--- "pets table data
INSERT INTO "pets"
	("owners_id", "name", "breed", "color", "checked_in", "checked_in_date")
VALUES
	(1, 'Nipsey', 'Pitbull', 'Black', TRUE, '2021-03-31'),
	(2, 'Taz', 'Mini Poodle', 'Gray', TRUE, '2021-03-30'),
	(2, 'Buttons', 'Great Dane', 'White', TRUE, '2021-03-30'),
	(2, 'Salvy', 'Cat', 'Yellow', FALSE, NULL),
	(3, 'Dakota', 'Husky', 'White', TRUE, '2021-03-29'),
	(4, 'Bob Barker', 'Boxer', 'Grey', FALSE, NULL);