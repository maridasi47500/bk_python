CREATE TABLE IF NOT EXISTS burgers (
burger_number INTEGER PRIMARY KEY,
name VARCHAR(200) unique,
image VARCHAR(50),
description text,
prix float,
mincal float,
maxcal float,
burgercat_id integer,
mytype varchar(100)
);
CREATE TABLE IF NOT EXISTS ingredients (
id INTEGER PRIMARY KEY,
name VARCHAR(200) unique,
image VARCHAR(50),
description text,
prix float,
mincal float,
maxcal float
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
token text,
signedin integer,
restaurant_id integer,
address_id integer,
pickup integer
);
CREATE TABLE IF NOT EXISTS bks (
id INTEGER PRIMARY KEY,
title VARCHAR(200) unique,
lat VARCHAR(200) unique,
lon VARCHAR(200) unique,
address text
);
CREATE TABLE IF NOT EXISTS favbks (
id INTEGER PRIMARY KEY,
user_id integer unique,
bk_id integer unique
);
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk1','Avenida Nações Unidas, Burger King, Centro, Novo Hamburgo, Região Geográfica Imediata de Novo Hamburgo - São Leopoldo, Metropolitan Region of Porto Alegre, Região Geográfica Intermediária de Porto Alegre, Rio Grande do Sul, South Region, 93310-002, Brazil','-29.6838785','-51.133577755343005');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk2','Burger King, Parnamirim, Recife, Região Geográfica Imediata do Recife, Região Metropolitana do Recife, Região Geográfica Intermediária do Recife, Pernambuco, Northeast Region, 52060-590, Brazil','-8.0353669','-34.9129296');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk3','Burger King, Parnamirim, Recife, Região Geográfica Imediata do Recife, Região Metropolitana do Recife, Região Geográfica Intermediária do Recife, Pernambuco, Northeast Region, 52060-590, Brazil','-8.0354408','-34.91296855');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk4','Burger King, Avenida Interlagos, Campo Grande, Vila Arriete, São Paulo, Região Imediata de São Paulo, Região Metropolitana de São Paulo, Região Geográfica Intermediária de São Paulo, São Paulo, Southeast Region, 04660-006, Brazil','-23.6815839','-46.689319417340016');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk8','Burger King, 1321, Rua Augusta, Consolação, São Paulo, Região Imediata de São Paulo, Região Metropolitana de São Paulo, Região Geográfica Intermediária de São Paulo, São Paulo, Southeast Region, 01305-100, Brazil','-23.5555588','-46.657349');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk999','Burger King, 2294, Avenida Brigadeiro Luís Antônio, Jardim Paulista, São Paulo, Região Imediata de São Paulo, Região Metropolitana de São Paulo, Região Geográfica Intermediária de São Paulo, São Paulo, Southeast Region, 01402-000, Brazil','-23.56777','-46.6493222');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk667','Burger King, 569, Rua Frei Caneca, Consolação, São Paulo, Região Imediata de São Paulo, Região Metropolitana de São Paulo, Região Geográfica Intermediária de São Paulo, São Paulo, Southeast Region, 01307-001, Brazil','-23.5543122','-46.6524059');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk','Burger King, Avenida John Boyd Dunlop, Campinas, Região Imediata de Campinas, Região Metropolitana de Campinas, Região Geográfica Intermediária de Campinas, São Paulo, Southeast Region, 13033-050, Brazil','-22.909815','-47.0923249');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk68','Burger King, Estrada do Coqueiro Grande, Cajazeiras, Salvador, Região Geográfica Imediata de Salvador, Região Metropolitana de Salvador, Região Geográfica Intermediária de Salvador, Bahia, Northeast Region, 41340-120, Brazil','-12.9049619','-38.4003086');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk789','Burger King, Wagenwegstraat, Paramaribo, Centrum, Paramaribo, Suriname','5.82745445','-55.1556997');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk789','Burger King, 1793, Rua Silva Teles, Belém, São Paulo, Região Imediata de São Paulo, Região Metropolitana de São Paulo, Região Geográfica Intermediária de São Paulo, São Paulo, Southeast Region, 03026-001, Brazil','-23.5237975','-46.605083627795786');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk78','Burger King, 35G/H, Rua São José, Castelo, Centro, Zona Central do Rio de Janeiro, Rio de Janeiro, Região Geográfica Imediata do Rio de Janeiro, Região Metropolitana do Rio de Janeiro, Região Geográfica Intermediária do Rio de Janeiro, Rio de Janeiro, Southeast Region, 20011-020, Brazil','-22.9049933','-43.1749227');
INSERT or ignore INTO 'bks' (title,address,lat,lon) VALUES('bk7887','Burger King, Regent Street, Lacytown, Alberttown, City of Georgetown, Eccles-Ramsburg Village District, Demerara-Mahaica, Guyana','6.8101662','-58.1612344');

CREATE TABLE IF NOT EXISTS addresses (
id INTEGER PRIMARY KEY,
address text
);
CREATE TABLE IF NOT EXISTS preorders (
  id INTEGER PRIMARY KEY,
  burger_id integer,
  user_id integer,
  qty varchar(100),
  data text,
  display integer
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

INSERT or ignore INTO users (email,prenom,code) VALUES ('cloe@gmail.com','cleo jeanne','098790');
INSERT or ignore INTO burgercats (name,url) VALUES ('Forfaits famille','burgers');
INSERT or ignore INTO burgercats (name,url) VALUES ('Hamburgers grillés à la flamme','flame');
INSERT or ignore INTO burgercats (name,url) VALUES ('Poulet et plus','meat');
INSERT or ignore INTO burgercats (name,url) VALUES ('accompagnements','sides');
INSERT or ignore INTO burgercats (name,url) VALUES ('Boissons & café','coffee');
INSERT or ignore INTO burgercats (name,url) VALUES ('dessert et bonbons','dessert');

INSERT or ignore INTO burgercats (name,url) VALUES ('burger jr','myburger');
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('big mac',20.00,300,800,1,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('big mac francais',20.00,1300,1800,2,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('big mac americain',25.00,1300,1900,2,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('big mac allemand',30.00,1100,1800,2,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('american original chicken sandwich',20.00,1000,2000,3,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('italian original chicken sandwich',20.00,1000,2000,3,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('mexican original chicken sandwich',20.00,1000,2000,3,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('bk royal crispy chicken',20.00,1000,2000,3,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('big mac first',20.00,1000,2000,3,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('frites',20.00,1000,2000,4,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ('calamar',20.00,1000,2000,4,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ("coca cola",'14.00','1540','2750',5,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ("sprite",'14.00','1540','2750',5,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ("ice tea",'14.00','1540','2750',5,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,burgercat_id,image) VALUES ("Mix n' Match Meals",'14.00','1540','2750',5,"burger.png");

INSERT or ignore INTO burgers (name,prix,mincal,burgercat_id,image) VALUES ("Whopper","6.89","670",6,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,burgercat_id,image) VALUES ("cheeseburger","6.89","670",7,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,burgercat_id,image) VALUES ("Double Whopper®","7.29","919",6,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,burgercat_id,image) VALUES ("Triple Whopper","7.59","1169",6,"burger.png");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,image,mytype) VALUES ('fries',20.00,300,800,"burger.png","jrsides");
INSERT or ignore INTO burgers (name,prix,mincal,maxcal,image,mytype) VALUES ('apple juice',20.00,300,800,"burger.png","jrdrinks");


INSERT or ignore INTO ingredients (name) VALUES ('mayo');
INSERT or ignore INTO ingredients (name) VALUES ('bacon');
INSERT or ignore INTO ingredients (name) VALUES ('stacker sauce');
INSERT or ignore INTO ingredients (name) VALUES ('ketchup');
INSERT or ignore INTO ingredients (name) VALUES ('moutarde');
INSERT or ignore INTO ingredients (name) VALUES ('lettuce');
INSERT or ignore INTO ingredients (name) VALUES ('onion');
INSERT or ignore INTO ingredients (name) VALUES ('pickle');
INSERT or ignore INTO ingredients (name) VALUES ('BBQ sauce');
INSERT or ignore INTO ingredients (name,mincal) VALUES ('american cheese',124);



INSERT or ignore INTO cards (mytitle,mydescription,mybutton) VALUES ("Now extended through 6/30/23!","You don't want to miss this! Join Royal Perks now to get your 🍟 every week, with any purchase, now through June 30, 2023.","Sign Up to Redeem");
INSERT or ignore INTO cards (mytitle,mydescription,mybutton) VALUES ("Get rewarded like Royalty","Join Royal Perks to earn Crowns, redeem for BK® food and upsize a side or drink for free daily.","Sign Up to Redeem");
INSERT or ignore INTO cards (mytitle,mydescription,mybutton) VALUES ("Free* Whopper, Croissan'wich, or Original Chicken Sandwich on your first digital order","Only on the BK® App and bk.com. Available on delivery. *Min $3+ Purch. req'd.","Sign Up to Redeem");
