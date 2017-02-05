-- ----------------------------------------------------------------------------
-- VtM20 lookup tables
-- ----------------------------------------------------------------------------
-- Use ^ to indicate start/end of player dice roll requirements.
-- ’  “”
-- ----------------------------------------------------------------------------
-- Changelog
-- When     | Who    | What
-- ---------+--------+---------------------------------------------------------
-- 25/06/12 | Lawson | Initial release
-- 21/11/13 | Lawson | Split files
-- ----------------------------------------------------------------------------

-- Output to screen
SELECT 'VtM20: 05 Inserting Logs' AS ' ';

USE VtM20;

-- VtM20_Logs_Admin_Login (ID,DTStamp,UserID)
-- VtM20_Logs_Admin_Pages (GameID,Page,Hits)
-- VtM20_Logs_Chars_Edits (ID,DTStamp,CharID,UserID,IsAdminEdit,StatType,Stat,Value,Cost,Notes)


-- Output to screen
SELECT 'VtM20: ... done.' AS ' ';
