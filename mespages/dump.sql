CREATE TABLE IF NOT EXISTS burgers (
burger_number INTEGER PRIMARY KEY,
name VARCHAR(200) unique,
image VARCHAR(50),
description text,
prix float,
mincal float,
maxcal float,
cat_id integer
);
CREATE TABLE IF NOT EXISTS cards (
id INTEGER PRIMARY KEY,
mytitle text unique not null,     
mydescription text unique not null,
mybutton TEXT,
url VARCHAR(200),
image VARCHAR(200));
CREATE TABLE IF NOT EXISTS cats (
id INTEGER PRIMARY KEY,
name VARCHAR(200) unique,     
url VARCHAR(200),
image VARCHAR(200)
);
CREATE TABLE IF NOT EXISTS users (
user_number INTEGER PRIMARY KEY,
prenom VARCHAR(255) unique,
email VARCHAR(255) unique,
code VARCHAR(255) unique,
dateofbirth date,
confidentialite integer,
offres integer
);
INSERT or ignore INTO users (email,prenom,code) VALUES ('cleo@gmail.com','cleo jeanne','098790');
INSERT or ignore INTO burgers (name) VALUES ('big mac');
INSERT or ignore INTO burgers (name) VALUES ('big mac francais');
INSERT or ignore INTO burgers (name) VALUES ('big mac americain');
INSERT or ignore INTO burgers (name) VALUES ('big mac allemand');
INSERT or ignore INTO burgers (name) VALUES ('big mac first');
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,cat_id) VALUES ("Mix n' Match Meals",'14.00','1540','2750',5);

INSERT or ignore INTO burgers (name,prix,mincal,cat_id) VALUES ("Whopper","6.89","670",6);
INSERT or ignore INTO burgers (name,prix,mincal,cat_id) VALUES ("Double Whopper®","7.29","919",6);
INSERT or ignore INTO burgers (name,prix,mincal,cat_id) VALUES ("Triple Whopper","7.59","1169",6);
INSERT or ignore INTO cards (mytitle,mydescription,mybutton) VALUES ("Now extended through 6/30/23!","You don't want to miss this! Join Royal Perks now to get your 🍟 every week, with any purchase, now through June 30, 2023.","Sign Up to Redeem");
INSERT or ignore INTO cards (mytitle,mydescription,mybutton) VALUES ("Get rewarded like Royalty","Join Royal Perks to earn Crowns, redeem for BK® food and upsize a side or drink for free daily.","Sign Up to Redeem");
INSERT or ignore INTO cards (mytitle,mydescription,mybutton) VALUES ("Free* Whopper, Croissan'wich, or Original Chicken Sandwich on your first digital order","Only on the BK® App and bk.com. Available on delivery. *Min $3+ Purch. req'd.","Sign Up to Redeem");

