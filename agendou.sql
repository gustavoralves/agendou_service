PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "facilities" (
 ID TEXT PRIMARY KEY,
 name TEXT NOT NULL,
 category TEXT,
 address TEXT,
 colors TEXT,
 picture TEXT,
 website TEXT );
INSERT INTO facilities VALUES('1','puppy pet','Pet Shop','Rua Foo, Boo','#ffffff_#000000_#0000ff','','');
CREATE TABLE services (
 ID TEXT PRIMARY KEY,
 name TEXT NOT NULL,
 description TEXT,
 facility_id TEXT NOT NULL,
 is_available INTEGER,
 FOREIGN KEY (facility_id) REFERENCES facilities (ID)
);
INSERT INTO services VALUES('1','Banho e Tosa','Lave o seu pet','1',1);
CREATE TABLE employment (
ID TEXT PRIMARY key,
user_id TEXT NOT NULL,
facility_id TEXT NOT NULL,
FOREIGN KEY (user_id) REFERENCES users (ID)
FOREIGN KEY (facility_id) REFERENCES facilities (ID));
INSERT INTO employment VALUES('1','1','1');
CREATE TABLE schedules (
ID TEXT PRIMARY KEY,
datetime TEXT NOT NULL,
service_id TEXT NOT NULL,
is_available INTEGER NOT NULL,
FOREIGN KEY (service_id) REFERENCES services (ID));
INSERT INTO schedules VALUES('1','2023-02-18-18-00','1',1);
INSERT INTO schedules VALUES('2','2023-02-18-19-30','1',0);
INSERT INTO schedules VALUES('3','2023-02-18-17-30','1',1);
INSERT INTO schedules VALUES('4','2023-02-18-16-30','1',1);
INSERT INTO schedules VALUES('5','2023-02-18-14-30','1',1);
INSERT INTO schedules VALUES('6','2023-02-18-12-30','1',0);
CREATE TABLE appointments (
ID TEXT PRIMARY KEY,
users_id INTEGER NOT NULL,
schedules_id INTEGER NOT NULL,
FOREIGN KEY (users_id) REFERENCES users (ID),
FOREIGN KEY (schedules_id) REFERENCES schedules (ID));
INSERT INTO appointments VALUES('1',1,1);
CREATE TABLE users(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
CPF TEXT NOT NULL,
email TEXT NOT NULL,
password TEXT NOT NULL,
phone TEXT NOT NULL,
whatsapp BOOLEAN,
provider_id BOOLEAN,
disable BOOLEAN);
DELETE FROM sqlite_sequence;
COMMIT;
