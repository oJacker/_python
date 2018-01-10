/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50714
Source Host           : 127.0.0.1:3306
Source Database       : perfectcrm

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2018-01-10 17:33:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add user', '2', 'add_user');
INSERT INTO `auth_permission` VALUES ('5', 'Can change user', '2', 'change_user');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete user', '2', 'delete_user');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add group', '4', 'add_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can change group', '4', 'change_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete group', '4', 'delete_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 客户跟进记录', '7', 'add_customerfollowup');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 客户跟进记录', '7', 'change_customerfollowup');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 客户跟进记录', '7', 'delete_customerfollowup');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 课程表', '8', 'add_course');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 课程表', '8', 'change_course');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 课程表', '8', 'delete_course');
INSERT INTO `auth_permission` VALUES ('25', 'Can add role', '9', 'add_role');
INSERT INTO `auth_permission` VALUES ('26', 'Can change role', '9', 'change_role');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete role', '9', 'delete_role');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 标签', '10', 'add_tag');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 标签', '10', 'change_tag');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 标签', '10', 'delete_tag');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 客户表', '11', 'add_customer');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 客户表', '11', 'change_customer');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 客户表', '11', 'delete_customer');
INSERT INTO `auth_permission` VALUES ('34', 'Can add payment', '12', 'add_payment');
INSERT INTO `auth_permission` VALUES ('35', 'Can change payment', '12', 'change_payment');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete payment', '12', 'delete_payment');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 上课记录', '13', 'add_courserecord');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 上课记录', '13', 'change_courserecord');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 上课记录', '13', 'delete_courserecord');
INSERT INTO `auth_permission` VALUES ('40', 'Can add menu', '14', 'add_menu');
INSERT INTO `auth_permission` VALUES ('41', 'Can change menu', '14', 'change_menu');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete menu', '14', 'delete_menu');
INSERT INTO `auth_permission` VALUES ('43', 'Can add user profile', '15', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('44', 'Can change user profile', '15', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete user profile', '15', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('46', 'Can add enrollment', '16', 'add_enrollment');
INSERT INTO `auth_permission` VALUES ('47', 'Can change enrollment', '16', 'change_enrollment');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete enrollment', '16', 'delete_enrollment');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 学习记录', '17', 'add_studyrecord');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 学习记录', '17', 'change_studyrecord');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 学习记录', '17', 'delete_studyrecord');
INSERT INTO `auth_permission` VALUES ('52', 'Can add 校区', '18', 'add_branch');
INSERT INTO `auth_permission` VALUES ('53', 'Can change 校区', '18', 'change_branch');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete 校区', '18', 'delete_branch');
INSERT INTO `auth_permission` VALUES ('55', 'Can add 班级', '19', 'add_classlist');
INSERT INTO `auth_permission` VALUES ('56', 'Can change 班级', '19', 'change_classlist');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete 班级', '19', 'delete_classlist');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$100000$ZFiRIpiNdhCH$FgGnO15NBXlYxoG3lDrb1ICIV20//ThXOxU2h2jutwU=', '2018-01-10 08:44:52.949400', '1', 'admin', '', '', 'admin@mail.com', '1', '1', '2018-01-10 08:43:52.908400');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$100000$MYlVUrRnHnoK$McQ6ihocBQ4VSOGUY7w0RPivDk/RWlbmhGbXfZYF9T8=', '2018-01-10 08:50:42.000000', '0', 'jack', '', '', '', '1', '1', '2018-01-10 08:48:51.000000');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
INSERT INTO `auth_user_user_permissions` VALUES ('1', '2', '52');
INSERT INTO `auth_user_user_permissions` VALUES ('2', '2', '53');
INSERT INTO `auth_user_user_permissions` VALUES ('3', '2', '54');
INSERT INTO `auth_user_user_permissions` VALUES ('4', '2', '32');
INSERT INTO `auth_user_user_permissions` VALUES ('5', '2', '33');
INSERT INTO `auth_user_user_permissions` VALUES ('6', '2', '31');

-- ----------------------------
-- Table structure for `crm_branch`
-- ----------------------------
DROP TABLE IF EXISTS `crm_branch`;
CREATE TABLE `crm_branch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `addr` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_branch
-- ----------------------------
INSERT INTO `crm_branch` VALUES ('1', 'bg', 'wdkdq');
INSERT INTO `crm_branch` VALUES ('2', 'sh', 'sdifwjisdf');

-- ----------------------------
-- Table structure for `crm_classlist`
-- ----------------------------
DROP TABLE IF EXISTS `crm_classlist`;
CREATE TABLE `crm_classlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_tpye` smallint(6) NOT NULL,
  `semester` smallint(5) unsigned NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `branch_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `crm_classlist_branch_id_course_id_semester_82c1a6a6_uniq` (`branch_id`,`course_id`,`semester`),
  KEY `crm_classlist_branch_id_26374f76` (`branch_id`),
  KEY `crm_classlist_course_id_8a4c36de` (`course_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_classlist
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_classlist_teachers`
-- ----------------------------
DROP TABLE IF EXISTS `crm_classlist_teachers`;
CREATE TABLE `crm_classlist_teachers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classlist_id` int(11) NOT NULL,
  `userprofile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `crm_classlist_teachers_classlist_id_userprofile_id_fdeb6cf0_uniq` (`classlist_id`,`userprofile_id`),
  KEY `crm_classlist_teachers_classlist_id_4b676750` (`classlist_id`),
  KEY `crm_classlist_teachers_userprofile_id_4ba87056` (`userprofile_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_classlist_teachers
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_course`
-- ----------------------------
DROP TABLE IF EXISTS `crm_course`;
CREATE TABLE `crm_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `price` smallint(5) unsigned NOT NULL,
  `period` smallint(5) unsigned NOT NULL,
  `outline` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_course
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_courserecord`
-- ----------------------------
DROP TABLE IF EXISTS `crm_courserecord`;
CREATE TABLE `crm_courserecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `day_num` smallint(5) unsigned NOT NULL,
  `has_homework` tinyint(1) NOT NULL,
  `homework_title` varchar(128) DEFAULT NULL,
  `homework_content` longtext,
  `outline` longtext NOT NULL,
  `date` date NOT NULL,
  `from_class_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `crm_courserecord_from_class_id_day_num_4a38bdfe_uniq` (`from_class_id`,`day_num`),
  KEY `crm_courserecord_from_class_id_4408a85a` (`from_class_id`),
  KEY `crm_courserecord_teacher_id_3ace9808` (`teacher_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_courserecord
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_customer`
-- ----------------------------
DROP TABLE IF EXISTS `crm_customer`;
CREATE TABLE `crm_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `qq` varchar(64) NOT NULL,
  `qq_name` varchar(64) DEFAULT NULL,
  `phone` varchar(64) DEFAULT NULL,
  `source` smallint(6) NOT NULL,
  `referral_form` varchar(64) DEFAULT NULL,
  `content` longtext NOT NULL,
  `status` smallint(6) NOT NULL,
  `memo` longtext,
  `date` datetime(6) NOT NULL,
  `consult_course_id` int(11) NOT NULL,
  `consultant_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `qq` (`qq`),
  KEY `crm_customer_consult_course_id_62aafa42` (`consult_course_id`),
  KEY `crm_customer_consultant_id_11f5298a` (`consultant_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_customer
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_customerfollowup`
-- ----------------------------
DROP TABLE IF EXISTS `crm_customerfollowup`;
CREATE TABLE `crm_customerfollowup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `intention` smallint(6) NOT NULL,
  `date` datetime(6) NOT NULL,
  `consultant_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `crm_customerfollowup_consultant_id_f64b5970` (`consultant_id`),
  KEY `crm_customerfollowup_customer_id_16ca1a28` (`customer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_customerfollowup
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_customer_tags`
-- ----------------------------
DROP TABLE IF EXISTS `crm_customer_tags`;
CREATE TABLE `crm_customer_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `crm_customer_tags_customer_id_tag_id_2f3e4566_uniq` (`customer_id`,`tag_id`),
  KEY `crm_customer_tags_customer_id_cb3e3b39` (`customer_id`),
  KEY `crm_customer_tags_tag_id_3dbac3dd` (`tag_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_customer_tags
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_enrollment`
-- ----------------------------
DROP TABLE IF EXISTS `crm_enrollment`;
CREATE TABLE `crm_enrollment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contract_agreed` tinyint(1) NOT NULL,
  `contract_approved` tinyint(1) NOT NULL,
  `date` datetime(6) NOT NULL,
  `consultant_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `enrolled_class_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `crm_enrollment_customer_id_enrolled_class_id_4589de06_uniq` (`customer_id`,`enrolled_class_id`),
  KEY `crm_enrollment_consultant_id_17808eee` (`consultant_id`),
  KEY `crm_enrollment_customer_id_4e9336cf` (`customer_id`),
  KEY `crm_enrollment_enrolled_class_id_7ea2b50c` (`enrolled_class_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_enrollment
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_menu`
-- ----------------------------
DROP TABLE IF EXISTS `crm_menu`;
CREATE TABLE `crm_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_menu
-- ----------------------------
INSERT INTO `crm_menu` VALUES ('1', '销售首页', 'sales_index');
INSERT INTO `crm_menu` VALUES ('2', '学生首页', 'stu_index');
INSERT INTO `crm_menu` VALUES ('3', '客户库', 'customer_list');

-- ----------------------------
-- Table structure for `crm_payment`
-- ----------------------------
DROP TABLE IF EXISTS `crm_payment`;
CREATE TABLE `crm_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(10) unsigned NOT NULL,
  `date` datetime(6) NOT NULL,
  `consultant_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `crm_payment_consultant_id_dadfc95b` (`consultant_id`),
  KEY `crm_payment_course_id_99bfc342` (`course_id`),
  KEY `crm_payment_customer_id_edbd2a4a` (`customer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_payment
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_role`
-- ----------------------------
DROP TABLE IF EXISTS `crm_role`;
CREATE TABLE `crm_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_role
-- ----------------------------
INSERT INTO `crm_role` VALUES ('1', '销售');
INSERT INTO `crm_role` VALUES ('2', '学生');

-- ----------------------------
-- Table structure for `crm_role_menus`
-- ----------------------------
DROP TABLE IF EXISTS `crm_role_menus`;
CREATE TABLE `crm_role_menus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `crm_role_menus_role_id_menu_id_955dcb97_uniq` (`role_id`,`menu_id`),
  KEY `crm_role_menus_role_id_d8dd6bc2` (`role_id`),
  KEY `crm_role_menus_menu_id_f3321925` (`menu_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_role_menus
-- ----------------------------
INSERT INTO `crm_role_menus` VALUES ('1', '1', '1');
INSERT INTO `crm_role_menus` VALUES ('2', '1', '3');
INSERT INTO `crm_role_menus` VALUES ('3', '2', '2');

-- ----------------------------
-- Table structure for `crm_studyrecord`
-- ----------------------------
DROP TABLE IF EXISTS `crm_studyrecord`;
CREATE TABLE `crm_studyrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attendance` smallint(6) NOT NULL,
  `score` smallint(6) NOT NULL,
  `memo` longtext,
  `date` date NOT NULL,
  `course_record_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `crm_studyrecord_student_id_course_record_id_24d12464_uniq` (`student_id`,`course_record_id`),
  KEY `crm_studyrecord_course_record_id_e3601e93` (`course_record_id`),
  KEY `crm_studyrecord_student_id_18b0c323` (`student_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_studyrecord
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_tag`
-- ----------------------------
DROP TABLE IF EXISTS `crm_tag`;
CREATE TABLE `crm_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_tag
-- ----------------------------

-- ----------------------------
-- Table structure for `crm_userprofile`
-- ----------------------------
DROP TABLE IF EXISTS `crm_userprofile`;
CREATE TABLE `crm_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_userprofile
-- ----------------------------
INSERT INTO `crm_userprofile` VALUES ('1', 'jack', '2');

-- ----------------------------
-- Table structure for `crm_userprofile_roles`
-- ----------------------------
DROP TABLE IF EXISTS `crm_userprofile_roles`;
CREATE TABLE `crm_userprofile_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `crm_userprofile_roles_userprofile_id_role_id_cee8b0c7_uniq` (`userprofile_id`,`role_id`),
  KEY `crm_userprofile_roles_userprofile_id_39ea736f` (`userprofile_id`),
  KEY `crm_userprofile_roles_role_id_33eee41d` (`role_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of crm_userprofile_roles
-- ----------------------------
INSERT INTO `crm_userprofile_roles` VALUES ('1', '1', '1');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2018-01-10 08:48:51.834400', '2', 'jack', '1', '[{\"added\": {}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2018-01-10 08:50:35.895400', '2', 'jack', '2', '[{\"changed\": {\"fields\": [\"is_staff\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2018-01-10 08:51:17.135400', '2', 'jack', '2', '[{\"changed\": {\"fields\": [\"user_permissions\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2018-01-10 08:51:50.746400', '1', 'bg', '1', '[{\"added\": {}}]', '18', '2');
INSERT INTO `django_admin_log` VALUES ('5', '2018-01-10 08:52:07.365400', '2', 'sh', '1', '[{\"added\": {}}]', '18', '2');
INSERT INTO `django_admin_log` VALUES ('6', '2018-01-10 08:53:23.622400', '1', 'jack', '1', '[{\"added\": {}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2018-01-10 09:14:54.629400', '1', '销售首页', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2018-01-10 09:15:43.598400', '2', '学生首页', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2018-01-10 09:16:33.227400', '3', '客户库', '1', '[{\"added\": {}}]', '14', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2018-01-10 09:18:17.446400', '1', '销售', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2018-01-10 09:19:25.924400', '1', 'jack', '2', '[{\"changed\": {\"fields\": [\"roles\"]}}]', '15', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2018-01-10 09:20:09.424400', '2', '学生', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2018-01-10 09:30:07.003400', '2', 'jack', '2', '[{\"changed\": {\"fields\": [\"user_permissions\"]}}]', '2', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2018-01-10 09:30:33.948400', '1', '销售', '2', '[{\"changed\": {\"fields\": [\"menus\"]}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2018-01-10 09:30:54.186400', '1', '销售', '2', '[{\"changed\": {\"fields\": [\"menus\"]}}]', '9', '1');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'crm', 'customerfollowup');
INSERT INTO `django_content_type` VALUES ('8', 'crm', 'course');
INSERT INTO `django_content_type` VALUES ('9', 'crm', 'role');
INSERT INTO `django_content_type` VALUES ('10', 'crm', 'tag');
INSERT INTO `django_content_type` VALUES ('11', 'crm', 'customer');
INSERT INTO `django_content_type` VALUES ('12', 'crm', 'payment');
INSERT INTO `django_content_type` VALUES ('13', 'crm', 'courserecord');
INSERT INTO `django_content_type` VALUES ('14', 'crm', 'menu');
INSERT INTO `django_content_type` VALUES ('15', 'crm', 'userprofile');
INSERT INTO `django_content_type` VALUES ('16', 'crm', 'enrollment');
INSERT INTO `django_content_type` VALUES ('17', 'crm', 'studyrecord');
INSERT INTO `django_content_type` VALUES ('18', 'crm', 'branch');
INSERT INTO `django_content_type` VALUES ('19', 'crm', 'classlist');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-01-10 08:33:12.660400');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-01-10 08:33:14.938400');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-01-10 08:33:15.290400');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-01-10 08:33:15.305400');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2018-01-10 08:33:15.439400');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2018-01-10 08:33:15.515400');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2018-01-10 08:33:15.593400');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2018-01-10 08:33:15.608400');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2018-01-10 08:33:15.710400');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2018-01-10 08:33:15.714400');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2018-01-10 08:33:15.732400');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2018-01-10 08:33:15.943400');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0009_alter_user_last_name_max_length', '2018-01-10 08:33:16.048400');
INSERT INTO `django_migrations` VALUES ('14', 'sessions', '0001_initial', '2018-01-10 08:33:16.149400');
INSERT INTO `django_migrations` VALUES ('15', 'crm', '0001_initial', '2018-01-10 08:37:46.099400');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('w78bde998ja9lvc1e3064piue2lgre5c', 'YjE0YTU4Y2M2MGE0YmVhZjJkMzE4OGI0N2EwMDE4NWMwYWFlMGQ3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZGNmMjBjNzhlYjA3ODQwN2Y0NjM2ZTQwNDU4MWYzYTkyNjkxNjZhOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-01-24 08:44:52.955400');
INSERT INTO `django_session` VALUES ('reoob3k66mca063r1m9oulb60nudp45l', 'NmZiYjg5OTQ4OTA3ZGE0Yjk4MzIzYTg0YjNhZjdkNzM3ZmI3ZWJiODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTkzOTIwNDk5ZTAzOTMwOTM4M2Q1MmMwZDA5NmI5ZjEyMGQ0NjBjYiIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=', '2018-01-24 08:50:42.668400');
