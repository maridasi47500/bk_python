CREATE TABLE IF NOT EXISTS burgers (
burger_number INTEGER PRIMARY KEY,
name VARCHAR(200) unique,
image VARCHAR(50),
description text,
prix float,
mincal float,
maxcal float,
burgercat_id integer
);
CREATE TABLE IF NOT EXISTS nutinfos (
burger_id INTEGER PRIMARY KEY,
calories float,
gras float,
grassature float,
grastrans float,
cholesterol float,
sodium float,
glucides float,
fibre float,
sucre float,
proteines float
);
CREATE TABLE IF NOT EXISTS burgercats (
  id integer primary key,
  name VARCHAR(200) unique,
  url varchar(200),
  image varchar(200)
);
create table if not exists user_favs (
  id integer primary key,
  user_id integer,
  nb integer,
    burger_id integer
);
create table if not exists user_recents (
  id integer primary key,
  user_id integer,
  nb integer,
    burger_id integer
);
CREATE TABLE IF NOT EXISTS giftcards (
id INTEGER PRIMARY KEY,
numero integer,
user_id integer);

CREATE TABLE IF NOT EXISTS creditcards (
id INTEGER PRIMARY KEY,
nom varchar(100),
zip varchar(20),
creditcard varchar(100),
cvv varchar(100),
datecard date,
user_id integer not null
);

CREATE TABLE IF NOT EXISTS orders (
id INTEGER PRIMARY KEY,
creditcard_id integer,
dateorder date,
user_id integer not null);
CREATE TABLE IF NOT EXISTS orderitems (
id INTEGER PRIMARY KEY,
burger_id integer not null,
qty integer,
order_id integer not null
);

CREATE TABLE IF NOT EXISTS cards (
id INTEGER PRIMARY KEY,
mytitle text unique not null,
mydescription text unique not null,
mybutton TEXT,
url VARCHAR(200),
image VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS cats (
id INTEGER PRIMARY KEY,
name VARCHAR(200) unique,
url VARCHAR(200),
image VARCHAR(200)
);
CREATE TABLE IF NOT EXISTS users (
user_number INTEGER PRIMARY KEY,
prenom VARCHAR(255),
email VARCHAR(255) unique,
code VARCHAR(255) unique,
tel varchar(255),
zip varchar(255),
dateofbirth date,
offres integer,
token text
);
CREATE TABLE IF NOT EXISTS customizeorders (
  id INTEGER PRIMARY KEY,
  burger_id integer,
  customburger_id integer,
  qty varchar(100),
  editthisitem integer,
  chosethisitem integer
);
CREATE TABLE IF NOT EXISTS customcustoms (
  id INTEGER PRIMARY KEY,
  customizeorders_id integer,
  customburger_id integer,
  qty varchar(100),
  chosethisitem integer,
  editthisitem integer
);
INSERT or ignore INTO nutinfos (burger_id,calories,gras,grassature,grastrans,cholesterol,sodium,glucides,fibre,sucre,proteines) VALUES (1.0,683.6,41.8,11.4,0.7,90.4,1175.3,54.6,3.0,13.3,32.0);

INSERT or ignore INTO users (email,prenom,code) VALUES ('cleo@gmail.com','cleo jeanne','098790');
INSERT or ignore INTO burgercats (name,url) VALUES ('Forfaits famille','burgers');
INSERT or ignore INTO burgercats (name,url) VALUES ('Hamburgers grillés à la flamme','flame');
INSERT or ignore INTO burgercats (name,url) VALUES ('Poulet et plus','meat');
INSERT or ignore INTO burgercats (name,url) VALUES ('côtés','sides');
INSERT or ignore INTO burgercats (name,url) VALUES ('dessert et bonbons','dessert');
INSERT or ignore INTO burgercats (name,url) VALUES ('Boissons & café','coffee');
INSERT or ignore INTO burgercats (name,url) VALUES ('salad','salad');
INSERT or ignore INTO burgercats (name,url) VALUES ('burger','myburger');
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id) VALUES ('big mac',20.00,300,800,1);
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id) VALUES ('big mac francais',20.00,1300,1800,2);
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id) VALUES ('big mac americain',25.00,1300,1900,2);
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id) VALUES ('big mac allemand',30.00,1100,1800,2);
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id) VALUES ('big mac first',20.00,1000,2000,3);
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id) VALUES ("Mix n' Match Meals",'14.00','1540','2750',5);

INSERT or ignore INTO burgers (name,prix,mincal,burgercat_id) VALUES ("Whopper","6.89","670",6);
INSERT or ignore INTO burgers (name,prix,mincal,burgercat_id) VALUES ("Double Whopper®","7.29","919",6);
INSERT or ignore INTO burgers (name,prix,mincal,burgercat_id) VALUES ("Triple Whopper","7.59","1169",6);
INSERT or ignore INTO burgers (name) VALUES ('mayo');
INSERT or ignore INTO burgers (name) VALUES ('bacon');
INSERT or ignore INTO burgers (name) VALUES ('stacker sauce');
INSERT or ignore INTO burgers (name) VALUES ('ketchup');
INSERT or ignore INTO burgers (name) VALUES ('moutarde');
INSERT or ignore INTO burgers (name) VALUES ('lettuce');
INSERT or ignore INTO burgers (name) VALUES ('onion');
INSERT or ignore INTO burgers (name) VALUES ('pickle');
INSERT or ignore INTO burgers (name) VALUES ('BBQ sauce');
INSERT or ignore INTO burgers (name,mincal) VALUES ('american cheese',124);

INSERT or ignore INTO cards (mytitle,mydescription,mybutton) VALUES ("Now extended through 6/30/23!","You don't want to miss this! Join Royal Perks now to get your 🍟 every week, with any purchase, now through June 30, 2023.","Sign Up to Redeem");
INSERT or ignore INTO cards (mytitle,mydescription,mybutton) VALUES ("Get rewarded like Royalty","Join Royal Perks to earn Crowns, redeem for BK® food and upsize a side or drink for free daily.","Sign Up to Redeem");
INSERT or ignore INTO cards (mytitle,mydescription,mybutton) VALUES ("Free* Whopper, Croissan'wich, or Original Chicken Sandwich on your first digital order","Only on the BK® App and bk.com. Available on delivery. *Min $3+ Purch. req'd.","Sign Up to Redeem");