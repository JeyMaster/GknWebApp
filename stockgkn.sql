-- MariaDB dump 10.18  Distrib 10.5.7-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: stockgkn
-- ------------------------------------------------------
-- Server version	10.5.7-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Equipo pool entrega',7,'add_equipo_pool_entrega'),(26,'Can change Equipo pool entrega',7,'change_equipo_pool_entrega'),(27,'Can delete Equipo pool entrega',7,'delete_equipo_pool_entrega'),(28,'Can view Equipo pool entrega',7,'view_equipo_pool_entrega'),(29,'Can add Equipo para entregar',8,'add_equipo_para_entregar'),(30,'Can change Equipo para entregar',8,'change_equipo_para_entregar'),(31,'Can delete Equipo para entregar',8,'delete_equipo_para_entregar'),(32,'Can view Equipo para entregar',8,'view_equipo_para_entregar'),(33,'Can add Basura Electronica',9,'add_basura_electronica'),(34,'Can change Basura Electronica',9,'change_basura_electronica'),(35,'Can delete Basura Electronica',9,'delete_basura_electronica'),(36,'Can view Basura Electronica',9,'view_basura_electronica'),(37,'Can add Detalle de entrega',10,'add_equipo_para_entregar_detalles'),(38,'Can change Detalle de entrega',10,'change_equipo_para_entregar_detalles'),(39,'Can delete Detalle de entrega',10,'delete_equipo_para_entregar_detalles'),(40,'Can view Detalle de entrega',10,'view_equipo_para_entregar_detalles'),(41,'Can add Stock',11,'add_stock'),(42,'Can change Stock',11,'change_stock'),(43,'Can delete Stock',11,'delete_stock'),(44,'Can view Stock',11,'view_stock'),(45,'Can add equipo',12,'add_equipo'),(46,'Can change equipo',12,'change_equipo'),(47,'Can delete equipo',12,'delete_equipo'),(48,'Can view equipo',12,'view_equipo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$b6InR9kxPuH4$uOZ9VKij8VVYUTzUNA5e2Wp5tpW1yhLU8p5JZz9+H9s=','2020-11-24 21:47:34.447182',1,'jose.lopez5_adm','','','neomix5000@gmail.com',1,1,'2020-11-19 15:49:06.072228'),(2,'pbkdf2_sha256$216000$hMGICkl78BjS$fW83sVkLbpE4yUapLSp4/cL35Rqdrj+ZnCzq4r6W6uE=','2020-11-19 18:59:31.094816',0,'jose.lopez5','','','',1,1,'2020-11-19 18:59:03.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `basuraelectronica`
--

DROP TABLE IF EXISTS `basuraelectronica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `basuraelectronica` (
  `id_basura_electronica` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) NOT NULL,
  `cantidad` smallint(6) NOT NULL,
  `modelo` varchar(15) NOT NULL,
  `marca` varchar(15) NOT NULL,
  `no_serie` varchar(100) DEFAULT NULL,
  `planta` varchar(3) NOT NULL,
  `fecha_registro` date NOT NULL,
  `recolectado` tinyint(1) NOT NULL,
  `fecha_recoleccion` date DEFAULT NULL,
  `responsable_id` int(11) NOT NULL,
  PRIMARY KEY (`id_basura_electronica`),
  KEY `BasuraElectronica_responsable_id_b9a78974_fk_auth_user_id` (`responsable_id`),
  CONSTRAINT `BasuraElectronica_responsable_id_b9a78974_fk_auth_user_id` FOREIGN KEY (`responsable_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basuraelectronica`
--

LOCK TABLES `basuraelectronica` WRITE;
/*!40000 ALTER TABLE `basuraelectronica` DISABLE KEYS */;
INSERT INTO `basuraelectronica` VALUES (1,'Impresora',6,'LaserJet M606','Hp','N/A','CEL','2020-11-10',0,NULL,2);
/*!40000 ALTER TABLE `basuraelectronica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detallesentrega`
--

DROP TABLE IF EXISTS `detallesentrega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detallesentrega` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `configurado_por` varchar(15) DEFAULT NULL,
  `fecha_preparacion` date NOT NULL,
  `check_list` varchar(100) DEFAULT NULL,
  `certificado_de_calidad` varchar(100) DEFAULT NULL,
  `solicitud` varchar(100) DEFAULT NULL,
  `site` varchar(5) DEFAULT NULL,
  `departamento` varchar(30) DEFAULT NULL,
  `area` varchar(30) DEFAULT NULL,
  `ubicacion_exacta` varchar(30) DEFAULT NULL,
  `apps_especiales` varchar(200) DEFAULT NULL,
  `registro_en_inventario` tinyint(1) NOT NULL,
  `id_equipo_para_entregar_id` int(11) NOT NULL,
  `preparado_por_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `DetallesEntrega_id_equipo_para_entre_fcf9d1ef_fk_EquipoPar` (`id_equipo_para_entregar_id`),
  KEY `DetallesEntrega_preparado_por_id_9bfcb50c_fk_auth_user_id` (`preparado_por_id`),
  CONSTRAINT `DetallesEntrega_id_equipo_para_entre_fcf9d1ef_fk_EquipoPar` FOREIGN KEY (`id_equipo_para_entregar_id`) REFERENCES `equipoparaentregar` (`id_equipo_para_entregar`),
  CONSTRAINT `DetallesEntrega_preparado_por_id_9bfcb50c_fk_auth_user_id` FOREIGN KEY (`preparado_por_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detallesentrega`
--

LOCK TABLES `detallesentrega` WRITE;
/*!40000 ALTER TABLE `detallesentrega` DISABLE KEYS */;
INSERT INTO `detallesentrega` VALUES (1,'Jose.lopez5','2020-11-24','checklist/checklist_4P94L33.docx','certificado/certificado_4P94L33.docx','','CEL','Proyectos','Lanzamientos','Oficinas proyectos',NULL,0,1,2),(3,NULL,'2020-11-24','','','',NULL,NULL,NULL,NULL,NULL,0,3,2),(4,NULL,'2020-11-24','','','',NULL,NULL,NULL,NULL,NULL,0,4,2),(5,NULL,'2020-11-24','','','',NULL,NULL,NULL,NULL,NULL,0,5,2),(6,'jose.lopez5','2020-11-24','','','solicitudes/solicitud_84FRDW2.docx',NULL,NULL,NULL,NULL,NULL,0,6,2),(7,NULL,'2020-11-24','','','',NULL,NULL,NULL,NULL,NULL,0,7,2);
/*!40000 ALTER TABLE `detallesentrega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-11-19 18:58:19.093287','1','Dell Latitude 5400  Ram:16',1,'[{\"added\": {}}]',11,1),(2,'2020-11-19 18:58:33.211450','2','Dell OptiPlex 5050  Ram:16',1,'[{\"added\": {}}]',11,1),(3,'2020-11-19 18:59:03.734265','2','jose.lopez5',1,'[{\"added\": {}}]',4,1),(4,'2020-11-19 18:59:11.236975','2','jose.lopez5',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(5,'2020-11-24 21:48:04.625851','3','Dell OptiPlex 3060  Ram:16',1,'[{\"added\": {}}]',11,1),(6,'2020-11-24 21:51:50.788127','2','Dell OptiPlex 3060  Ram:16 FBH24Z2',3,'',12,1),(7,'2020-11-24 21:52:21.772356','4','Dell OptiPlex 5060  Ram:16',1,'[{\"added\": {}}]',11,1),(8,'2020-11-24 21:52:35.827343','3','Dell OptiPlex 3060  Ram:16',2,'[{\"changed\": {\"fields\": [\"Cantidad\"]}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'equipos','basura_electronica'),(12,'equipos','equipo'),(8,'equipos','equipo_para_entregar'),(10,'equipos','equipo_para_entregar_detalles'),(7,'equipos','equipo_pool_entrega'),(11,'equipos','stock'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-11-19 15:46:12.368163'),(2,'auth','0001_initial','2020-11-19 15:46:12.565245'),(3,'admin','0001_initial','2020-11-19 15:46:13.007580'),(4,'admin','0002_logentry_remove_auto_add','2020-11-19 15:46:13.122280'),(5,'admin','0003_logentry_add_action_flag_choices','2020-11-19 15:46:13.146210'),(6,'contenttypes','0002_remove_content_type_name','2020-11-19 15:46:13.230984'),(7,'auth','0002_alter_permission_name_max_length','2020-11-19 15:46:13.305783'),(8,'auth','0003_alter_user_email_max_length','2020-11-19 15:46:13.381600'),(9,'auth','0004_alter_user_username_opts','2020-11-19 15:46:13.393556'),(10,'auth','0005_alter_user_last_login_null','2020-11-19 15:46:13.438429'),(11,'auth','0006_require_contenttypes_0002','2020-11-19 15:46:13.445422'),(12,'auth','0007_alter_validators_add_error_messages','2020-11-19 15:46:13.460380'),(13,'auth','0008_alter_user_username_max_length','2020-11-19 15:46:13.490291'),(14,'auth','0009_alter_user_last_name_max_length','2020-11-19 15:46:13.547412'),(15,'auth','0010_alter_group_name_max_length','2020-11-19 15:46:13.617222'),(16,'auth','0011_update_proxy_permissions','2020-11-19 15:46:13.644149'),(17,'auth','0012_alter_user_first_name_max_length','2020-11-19 15:46:13.666094'),(18,'sessions','0001_initial','2020-11-19 15:46:13.693022'),(19,'equipos','0001_initial','2020-11-19 15:48:07.186128');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('071wuzdldbzrl4tk2vk3ltut5sc5bm5i','.eJxVjEEOwiAQRe_C2pC2TGFw6b5nIMMAUjWQlHZlvLsh6UK3_73338LRsWd3tLi5NYirmMTld_PEz1g6CA8q9yq5ln1bveyKPGmTSw3xdTvdv4NMLfdaI_Ic1chMQMpahaAQk8JkwKMfNTDYMCs0EaLRhIAJtTGWBxrMJD5f01w3GA:1kfp9X:Dgz3e77E6sSxOH1J3WtfIg_PL00VFzS92bA-EnlFuSU','2020-12-03 18:59:31.100819'),('a951kcivqrzl3jyniz9z3w1gh8pik7nr','.eJxVjEEOwiAQRe_C2pACI1CX7nsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwk7gIJU6_W8T04LoDumO9NZlaXZc5yl2RB-1yasTP6-H-HRTs5Vsn0ORhJAfGalJAVg3aGCDKMBrw0UdGtNmw4oSeYzbRkbfurPPgSIn3B9kFOAc:1khg9u:5qI8r-wVIm3N0SYcomfiiMWIQOnI69a6mnSx4oBCGdY','2020-12-08 21:47:34.458192'),('z4cdru3nwcr0owug5ljq12zyy1zwujpo','.eJxVjEEOwiAQRe_C2pACI1CX7nsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwk7gIJU6_W8T04LoDumO9NZlaXZc5yl2RB-1yasTP6-H-HRTs5Vsn0ORhJAfGalJAVg3aGCDKMBrw0UdGtNmw4oSeYzbRkbfurPPgSIn3B9kFOAc:1kfp7n:ddtQsQPWXlis6lKdWrRwOsEzoWbDiFNM6th8X_-9GJg','2020-12-03 18:57:43.554857');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipoparaentregar`
--

DROP TABLE IF EXISTS `equipoparaentregar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipoparaentregar` (
  `id_equipo_para_entregar` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_equipo` varchar(12) NOT NULL,
  `usuario_final` varchar(20) NOT NULL,
  `id_equipo_id` int(11) NOT NULL,
  PRIMARY KEY (`id_equipo_para_entregar`),
  KEY `EquipoParaEntregar_id_equipo_id_b44e3073_fk_Equipos_id_equipo` (`id_equipo_id`),
  CONSTRAINT `EquipoParaEntregar_id_equipo_id_b44e3073_fk_Equipos_id_equipo` FOREIGN KEY (`id_equipo_id`) REFERENCES `equipos` (`id_equipo`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipoparaentregar`
--

LOCK TABLES `equipoparaentregar` WRITE;
/*!40000 ALTER TABLE `equipoparaentregar` DISABLE KEYS */;
INSERT INTO `equipoparaentregar` VALUES (1,'DLCELLT511','jaime.castaneda',1),(3,'DLCELPC994','',3),(4,'DLCELPC995','',4),(5,'DLCELPC996','',5),(6,'DLCELPC252','jose.cardenas1',6),(7,'DLCELPC253','carlos.posada',7);
/*!40000 ALTER TABLE `equipoparaentregar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipos`
--

DROP TABLE IF EXISTS `equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipos` (
  `id_equipo` int(11) NOT NULL AUTO_INCREMENT,
  `service_tag` varchar(12) NOT NULL,
  `estado` varchar(2) NOT NULL,
  `fecha_termino_garantia` date DEFAULT NULL,
  `id_stock_id` int(11) NOT NULL,
  PRIMARY KEY (`id_equipo`),
  KEY `Equipos_id_stock_id_588a52d0_fk_Stock_id_stock` (`id_stock_id`),
  CONSTRAINT `Equipos_id_stock_id_588a52d0_fk_Stock_id_stock` FOREIGN KEY (`id_stock_id`) REFERENCES `stock` (`id_stock`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipos`
--

LOCK TABLES `equipos` WRITE;
/*!40000 ALTER TABLE `equipos` DISABLE KEYS */;
INSERT INTO `equipos` VALUES (1,'4P94L33','Et','2024-05-29',1),(3,'FBH24Z2','Pr','2022-09-23',4),(4,'GJYHPY2','Pr','2022-09-23',4),(5,'FBJ24Z2','Pr','2022-09-23',4),(6,'84FRDW2','Ua','2022-06-06',3),(7,'84KTDW2','Ua','2022-06-06',3);
/*!40000 ALTER TABLE `equipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipospoolentrega`
--

DROP TABLE IF EXISTS `equipospoolentrega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipospoolentrega` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_salida` datetime(6) NOT NULL,
  `fecha_entrega` datetime(6) DEFAULT NULL,
  `caso_especial` tinyint(1) NOT NULL,
  `equipo_recibido` tinyint(1) NOT NULL,
  `nombre_equipo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `EquiposPoolEntrega_nombre_equipo_id_03480b27_fk_EquipoPar` (`nombre_equipo_id`),
  CONSTRAINT `EquiposPoolEntrega_nombre_equipo_id_03480b27_fk_EquipoPar` FOREIGN KEY (`nombre_equipo_id`) REFERENCES `equipoparaentregar` (`id_equipo_para_entregar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipospoolentrega`
--

LOCK TABLES `equipospoolentrega` WRITE;
/*!40000 ALTER TABLE `equipospoolentrega` DISABLE KEYS */;
/*!40000 ALTER TABLE `equipospoolentrega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stock` (
  `categoria` varchar(2) NOT NULL,
  `id_stock` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` smallint(6) NOT NULL,
  `modelo` varchar(20) NOT NULL,
  `marca` varchar(15) NOT NULL,
  `ram` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id_stock`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
INSERT INTO `stock` VALUES ('LT',1,9,'Latitude 5400','Dell',16),('PC',2,10,'OptiPlex 5050','Dell',16),('PC',3,28,'OptiPlex 3060','Dell',16),('PC',4,1,'OptiPlex 5060','Dell',16);
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-24 16:54:47
