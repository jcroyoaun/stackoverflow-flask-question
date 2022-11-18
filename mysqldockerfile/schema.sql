CREATE DATABASE /*!32312 IF NOT EXISTS*/ `mysqldb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

CREATE TABLE `visitor` (
  `accessed_at` float(18,6),
  `user_id` int(20) DEFAULT NULL,
  `page_id` int(20) DEFAULT NULL,
  PRIMARY KEY (`accessed_at`)
) 