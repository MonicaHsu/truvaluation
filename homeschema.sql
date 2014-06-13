-- Example table schema
-- To import your schemas into your database, run:
-- `mysql -u username -p database < schema.sql`
-- where username is your MySQL username
 
-- Load data into table
-- LOAD DATA LOCAL INFILE ‘predicted_current_listings.csv’ INTO TABLE homes
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY ''
-- LINES TERMINATED BY '\n'
-- IGNORE 0 LINES
-- (id, year_built, zip_code, list_price, beds, baths, sqft, dom, parking, sale_price, views, favs, xouts, latitude, longitude, crime_score, prediction, bike_score, transit_score, walk_score);
 
CREATE TABLE `homes` (
  `home` char(50) NOT NULL DEFAULT '',
  `year_built` int(11) DEFAULT NULL,
  `zip_code` int(11) DEFAULT NULL,
  `list_price` int(11) DEFAULT NULL,
  `beds` int(11) DEFAULT NULL,
  `baths` int(11) DEFAULT NULL,
  `sqft` int(11) DEFAULT NULL,
  `dom` int(11) DEFAULT NULL,
  `parking` int(11) DEFAULT NULL,
  `sale_price` int(11) DEFAULT NULL,
  `views` int(11) DEFAULT NULL,
  `favs` int(11) DEFAULT NULL,
  `xouts` int(11) DEFAULT NULL,
  `latitude` decimal(19,4) DEFAULT NULL,
  `longitude` decimal(19,4) DEFAULT NULL,
  `crime_score` decimal(2,1) DEFAULT NULL,
  `prediction` decimal(2,1) DEFAULT NULL,
  `bike_score` int(11) DEFAULT NULL,
  `transit_score` int(11) DEFAULT NULL,
  `walk_score` int(11) DEFAULT NULL,
  PRIMARY KEY (`home`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;