-- ----------------------------------------------------------------------------
-- VtM20 lookup tables
-- ----------------------------------------------------------------------------
-- Use ^ to indicate start/end of player dice roll requirements.
-- ’  “”
-- ----------------------------------------------------------------------------
-- Changelog
-- When     | Who    | What
-- ---------+--------+---------------------------------------------------------
-- 21/06/12 | Lawson | Initial release
-- 21/11/13 | Lawson | Split files
-- ----------------------------------------------------------------------------

-- Output to screen
SELECT 'VtM20: 01 Creating Database' AS ' ';

-- Set MySQL STRICT Mode
SET SESSION sql_mode='STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION,NO_ZERO_DATE,NO_ZERO_IN_DATE';

DROP DATABASE IF EXISTS VtM20;

CREATE DATABASE VtM20
  CHARSET utf8
  COLLATE utf8_unicode_ci;

GRANT EXECUTE
  ON VtM20.*
  TO 'VtM20User'@'localhost'
  IDENTIFIED BY '10gb!hotw';

-- Load next script
source 02_VtM20_Create_Tables.sql;
