BEGIN TRANSACTION;
DROP TABLE IF EXISTS "nurseapp_record";
CREATE TABLE IF NOT EXISTS "nurseapp_record" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"pressure1"	integer NOT NULL,
	"pressure2"	integer NOT NULL,
	"bpm"	integer NOT NULL,
	"status_bpm"	varchar(10) NOT NULL,
	"patient_id"	integer NOT NULL,
	"date"	date NOT NULL,
	"status_pressure"	varchar(10) NOT NULL,
	FOREIGN KEY("patient_id") REFERENCES "nurseapp_patient"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "nurseapp_rangep2";
CREATE TABLE IF NOT EXISTS "nurseapp_rangep2" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"pressure2_min"	integer NOT NULL,
	"pressure2_max"	integer NOT NULL,
	"level"	integer NOT NULL,
	"status"	varchar(15) NOT NULL
);
DROP TABLE IF EXISTS "nurseapp_rangep1";
CREATE TABLE IF NOT EXISTS "nurseapp_rangep1" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"pressure1_min"	integer NOT NULL,
	"pressure1_max"	integer NOT NULL,
	"level"	integer NOT NULL,
	"status"	varchar(15) NOT NULL
);
DROP TABLE IF EXISTS "nurseapp_rangeb";
CREATE TABLE IF NOT EXISTS "nurseapp_rangeb" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"age"	integer NOT NULL,
	"gender"	varchar(1) NOT NULL,
	"bpm_min"	integer NOT NULL,
	"bpm_max"	integer NOT NULL,
	"status"	varchar(15) NOT NULL
);
DROP TABLE IF EXISTS "django_session";
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
DROP TABLE IF EXISTS "nurseapp_range";
CREATE TABLE IF NOT EXISTS "nurseapp_range" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"age"	integer NOT NULL,
	"gender"	varchar(1) NOT NULL,
	"pressure1_min"	integer NOT NULL,
	"pressure1_max"	integer NOT NULL,
	"pressure2_min"	integer NOT NULL,
	"pressure2_max"	integer NOT NULL,
	"bpm_min"	integer NOT NULL,
	"bpm_max"	integer NOT NULL
);
DROP TABLE IF EXISTS "nurseapp_patient";
CREATE TABLE IF NOT EXISTS "nurseapp_patient" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(30) NOT NULL,
	"lastname"	varchar(30) NOT NULL,
	"gender"	varchar(1) NOT NULL,
	"cid"	integer NOT NULL UNIQUE,
	"birth"	date NOT NULL,
	"age"	integer NOT NULL
);
DROP TABLE IF EXISTS "auth_group";
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(150) NOT NULL UNIQUE
);
DROP TABLE IF EXISTS "auth_user";
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(30) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"last_name"	varchar(150) NOT NULL
);
DROP TABLE IF EXISTS "auth_permission";
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "auth_user_user_permissions";
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "auth_user_groups";
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "auth_group_permissions";
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "django_migrations";
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL
);
INSERT INTO "nurseapp_record" VALUES (1,100,75,75,'Normal',1,'2020-06-01','Normal');
INSERT INTO "nurseapp_record" VALUES (2,12,12,12,'',1,'2020-06-02','');
INSERT INTO "nurseapp_record" VALUES (3,33,33,33,'',1,'2020-02-02','');
INSERT INTO "nurseapp_rangep2" VALUES (2,60,79,1,'Normal');
INSERT INTO "nurseapp_rangep2" VALUES (3,80,89,2,'High (Stage1)');
INSERT INTO "nurseapp_rangep2" VALUES (4,90,119,3,'High (Stage2)');
INSERT INTO "nurseapp_rangep2" VALUES (5,120,999,4,'HyperCrisis');
INSERT INTO "nurseapp_rangep2" VALUES (6,0,59,0,'Low');
INSERT INTO "nurseapp_rangep1" VALUES (1,60,119,1,'Normal');
INSERT INTO "nurseapp_rangep1" VALUES (2,0,59,0,'Low');
INSERT INTO "nurseapp_rangep1" VALUES (3,120,129,2,'Elevated');
INSERT INTO "nurseapp_rangep1" VALUES (4,130,139,3,'High (Stage1)');
INSERT INTO "nurseapp_rangep1" VALUES (5,140,180,4,'High (stage2)');
INSERT INTO "nurseapp_rangep1" VALUES (6,180,999,5,'HyperCrisis');
INSERT INTO "nurseapp_rangeb" VALUES (1,100,'m',60,100,'Normal');
INSERT INTO "django_session" VALUES ('aaxizcfogxqrbxr7j1asa46b0dqqmrs3','NzJkNDlkN2NlYTQyZjZhZDEwZmRlMGRkMGNiMWM2YTc0NjlmZTEyYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2OWU5ZWFmYmU2ODU2NTQyMDI2NTNlN2RlNWVlMTRlOWZmZDgyN2ViIn0=','2020-06-15 19:25:04.440466');
INSERT INTO "django_session" VALUES ('3vz7lgyxjie50b78boyfdah16ulmp5bi','OWUxOTFiZDZjZTNiY2M0ODRmNGM1OTRiMmZhMjBiMWJkNTMxNDBhNDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkMGUxZWE4MmMzNTgyMmIzNmU0ZGIyY2FjODJlMjg3NDQ0ZWQ2NDZiIn0=','2020-06-16 05:45:25.603537');
INSERT INTO "nurseapp_range" VALUES (1,200,'m',90,120,60,80,54,85);
INSERT INTO "nurseapp_patient" VALUES (1,'John','Smith','m',123456,'1976-02-05',0);
INSERT INTO "auth_group" VALUES (1,'nurses');
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$180000$cF43kCg4h6xF$TcZHF9NTysdBrINtG/DvNCE5xL6NMPDYQ1mxZIavVBU=','2020-06-01 19:25:04.437464',1,'admin','','',1,1,'2020-06-01 19:24:54.959269','');
INSERT INTO "auth_user" VALUES (2,'pbkdf2_sha256$180000$xNyqmc4pPRT6$7M0EYUPkvHX9nHYMGUV8FIyrX8SsaXgsiladJD4Ur0g=','2020-06-02 05:45:25.600534',0,'nurse','','',0,1,'2020-06-01 19:25:24','');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_patient','Can add patient');
INSERT INTO "auth_permission" VALUES (26,7,'change_patient','Can change patient');
INSERT INTO "auth_permission" VALUES (27,7,'delete_patient','Can delete patient');
INSERT INTO "auth_permission" VALUES (28,7,'view_patient','Can view patient');
INSERT INTO "auth_permission" VALUES (29,8,'add_range','Can add range');
INSERT INTO "auth_permission" VALUES (30,8,'change_range','Can change range');
INSERT INTO "auth_permission" VALUES (31,8,'delete_range','Can delete range');
INSERT INTO "auth_permission" VALUES (32,8,'view_range','Can view range');
INSERT INTO "auth_permission" VALUES (33,9,'add_record','Can add record');
INSERT INTO "auth_permission" VALUES (34,9,'change_record','Can change record');
INSERT INTO "auth_permission" VALUES (35,9,'delete_record','Can delete record');
INSERT INTO "auth_permission" VALUES (36,9,'view_record','Can view record');
INSERT INTO "auth_permission" VALUES (37,10,'add_rangeb','Can add range b');
INSERT INTO "auth_permission" VALUES (38,10,'change_rangeb','Can change range b');
INSERT INTO "auth_permission" VALUES (39,10,'delete_rangeb','Can delete range b');
INSERT INTO "auth_permission" VALUES (40,10,'view_rangeb','Can view range b');
INSERT INTO "auth_permission" VALUES (41,11,'add_rangep1','Can add range p1');
INSERT INTO "auth_permission" VALUES (42,11,'change_rangep1','Can change range p1');
INSERT INTO "auth_permission" VALUES (43,11,'delete_rangep1','Can delete range p1');
INSERT INTO "auth_permission" VALUES (44,11,'view_rangep1','Can view range p1');
INSERT INTO "auth_permission" VALUES (45,12,'add_rangep2','Can add range p2');
INSERT INTO "auth_permission" VALUES (46,12,'change_rangep2','Can change range p2');
INSERT INTO "auth_permission" VALUES (47,12,'delete_rangep2','Can delete range p2');
INSERT INTO "auth_permission" VALUES (48,12,'view_rangep2','Can view range p2');
INSERT INTO "auth_user_groups" VALUES (1,2,1);
INSERT INTO "auth_group_permissions" VALUES (1,1,32);
INSERT INTO "auth_group_permissions" VALUES (2,1,33);
INSERT INTO "auth_group_permissions" VALUES (3,1,34);
INSERT INTO "auth_group_permissions" VALUES (4,1,35);
INSERT INTO "auth_group_permissions" VALUES (5,1,36);
INSERT INTO "auth_group_permissions" VALUES (6,1,25);
INSERT INTO "auth_group_permissions" VALUES (7,1,26);
INSERT INTO "auth_group_permissions" VALUES (8,1,27);
INSERT INTO "auth_group_permissions" VALUES (9,1,28);
INSERT INTO "auth_group_permissions" VALUES (10,1,29);
INSERT INTO "auth_group_permissions" VALUES (11,1,30);
INSERT INTO "auth_group_permissions" VALUES (12,1,31);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2020-06-01 19:22:51.494766');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2020-06-01 19:22:51.507777');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2020-06-01 19:22:51.518786');
INSERT INTO "django_migrations" VALUES (4,'admin','0002_logentry_remove_auto_add','2020-06-01 19:22:51.535801');
INSERT INTO "django_migrations" VALUES (5,'admin','0003_logentry_add_action_flag_choices','2020-06-01 19:22:51.546810');
INSERT INTO "django_migrations" VALUES (6,'contenttypes','0002_remove_content_type_name','2020-06-01 19:22:51.563825');
INSERT INTO "django_migrations" VALUES (7,'auth','0002_alter_permission_name_max_length','2020-06-01 19:22:51.570831');
INSERT INTO "django_migrations" VALUES (8,'auth','0003_alter_user_email_max_length','2020-06-01 19:22:51.580840');
INSERT INTO "django_migrations" VALUES (9,'auth','0004_alter_user_username_opts','2020-06-01 19:22:51.590849');
INSERT INTO "django_migrations" VALUES (10,'auth','0005_alter_user_last_login_null','2020-06-01 19:22:51.601858');
INSERT INTO "django_migrations" VALUES (11,'auth','0006_require_contenttypes_0002','2020-06-01 19:22:51.604861');
INSERT INTO "django_migrations" VALUES (12,'auth','0007_alter_validators_add_error_messages','2020-06-01 19:22:51.614869');
INSERT INTO "django_migrations" VALUES (13,'auth','0008_alter_user_username_max_length','2020-06-01 19:22:51.628882');
INSERT INTO "django_migrations" VALUES (14,'auth','0009_alter_user_last_name_max_length','2020-06-01 19:22:51.638890');
INSERT INTO "django_migrations" VALUES (15,'auth','0010_alter_group_name_max_length','2020-06-01 19:22:51.647898');
INSERT INTO "django_migrations" VALUES (16,'auth','0011_update_proxy_permissions','2020-06-01 19:22:51.654904');
INSERT INTO "django_migrations" VALUES (17,'nurseapp','0001_initial','2020-06-01 19:22:51.661910');
INSERT INTO "django_migrations" VALUES (18,'sessions','0001_initial','2020-06-01 19:22:51.665913');
INSERT INTO "django_migrations" VALUES (19,'nurseapp','0002_record_date','2020-06-01 19:44:49.181187');
INSERT INTO "django_migrations" VALUES (20,'nurseapp','0003_auto_20200602_1232','2020-06-02 16:32:32.320868');
INSERT INTO "django_migrations" VALUES (21,'nurseapp','0004_auto_20200602_1238','2020-06-02 16:38:13.394171');
DROP INDEX IF EXISTS "nurseapp_record_patient_id_cc06626c";
CREATE INDEX IF NOT EXISTS "nurseapp_record_patient_id_cc06626c" ON "nurseapp_record" (
	"patient_id"
);
DROP INDEX IF EXISTS "django_session_expire_date_a5c62663";
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
DROP INDEX IF EXISTS "auth_permission_content_type_id_2f476e4b";
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
DROP INDEX IF EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
DROP INDEX IF EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c";
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
DROP INDEX IF EXISTS "auth_user_user_permissions_user_id_a95ead1b";
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
DROP INDEX IF EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
DROP INDEX IF EXISTS "auth_user_groups_group_id_97559544";
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
DROP INDEX IF EXISTS "auth_user_groups_user_id_6a12ed8b";
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
DROP INDEX IF EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
DROP INDEX IF EXISTS "auth_group_permissions_permission_id_84c5c92e";
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
DROP INDEX IF EXISTS "auth_group_permissions_group_id_b120cbf9";
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
DROP INDEX IF EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
COMMIT;
