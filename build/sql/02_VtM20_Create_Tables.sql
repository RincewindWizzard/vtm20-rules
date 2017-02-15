-- ----------------------------------------------------------------------------
-- VtM20 lookup tables
-- ----------------------------------------------------------------------------
-- Use ^ to indicate start/end of player dice roll requirements.
-- ’  “”
-- ----------------------------------------------------------------------------
-- Changelog
-- When     | Who    | What
-- ---------+--------+---------------------------------------------------------
-- 21/06/12 | Lawson | Initial work
-- 21/11/13 | Lawson | Split files
-- ----------------------------------------------------------------------------

-- Output to screen
SELECT 'VtM20: 02 Creating Tables' AS ' ';

USE VtM20;

-- 01 Lookup Tables
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Abilities (
  ID     INT UNSIGNED  NOT NULL AUTO_INCREMENT COMMENT "Ability ID",
  AType  VARCHAR(16)   NOT NULL                COMMENT "Ability Type - Talents, Skills or Knowledges",
  Name   VARCHAR(64)   NOT NULL                COMMENT "Ability Name",
  Descr  VARCHAR(2000) NOT NULL                COMMENT "Ability Description",
  Level1 VARCHAR(255)  NOT NULL                COMMENT "Ability Level 1 Description",
  Level2 VARCHAR(255)  NOT NULL                COMMENT "Ability Level 2 Description",
  Level3 VARCHAR(255)  NOT NULL                COMMENT "Ability Level 3 Description",
  Level4 VARCHAR(255)  NOT NULL                COMMENT "Ability Level 4 Description",
  Level5 VARCHAR(255)  NOT NULL                COMMENT "Ability Level 5 Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Abilities_Other (
  ID     INT UNSIGNED  NOT NULL AUTO_INCREMENT COMMENT "Other Ability ID",
  AType  VARCHAR(16)   NOT NULL                COMMENT "Other Ability Type - Talents, Skills or Knowledges",
  Name   VARCHAR(64)   NOT NULL                COMMENT "Other Ability Name",
  Descr  VARCHAR(2000) NOT NULL                COMMENT "Other Ability Description",
  Level1 VARCHAR(255)  NOT NULL                COMMENT "Other Ability Level 1 Description",
  Level2 VARCHAR(255)  NOT NULL                COMMENT "Other Ability Level 2 Description",
  Level3 VARCHAR(255)  NOT NULL                COMMENT "Other Ability Level 3 Description",
  Level4 VARCHAR(255)  NOT NULL                COMMENT "Other Ability Level 4 Description",
  Level5 VARCHAR(255)  NOT NULL                COMMENT "Other Ability Level 5 Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Archetypes (
  ID    INT UNSIGNED  NOT NULL AUTO_INCREMENT COMMENT "Archetype ID",
  Name  VARCHAR(64)   NOT NULL                COMMENT "Archetype Name",
  Descr VARCHAR(2000) NOT NULL                COMMENT "Archetype Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Attributes (
  ID     INT UNSIGNED  NOT NULL AUTO_INCREMENT COMMENT "Attribute ID",
  AType  VARCHAR(16)   NOT NULL                COMMENT "Attribute Type - Physical, Social or Mental",
  Name   VARCHAR(16)   NOT NULL                COMMENT "Attribute Name",
  Descr  VARCHAR(2000) NOT NULL                COMMENT "Attribute Description",
  Level1 VARCHAR(255)  NOT NULL                COMMENT "Attribute Level 1 Description",
  Level2 VARCHAR(255)  NOT NULL                COMMENT "Attribute Level 2 Description",
  Level3 VARCHAR(255)  NOT NULL                COMMENT "Attribute Level 3 Description",
  Level4 VARCHAR(255)  NOT NULL                COMMENT "Attribute Level 4 Description",
  Level5 VARCHAR(255)  NOT NULL                COMMENT "Attribute Level 5 Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Backgrounds (
  ID       INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Background ID",
  Name     VARCHAR(64)      NOT NULL                COMMENT "Background Name",
  HasNotes TINYINT UNSIGNED NOT NULL                COMMENT "Does this Background need Notes?",
  Descr    VARCHAR(3000)    NOT NULL                COMMENT "Background Description",
  Level1   VARCHAR(1000)    NOT NULL                COMMENT "Background Level 1 Description",
  Level2   VARCHAR(1000)    NOT NULL                COMMENT "Background Level 2 Description",
  Level3   VARCHAR(1000)    NOT NULL                COMMENT "Background Level 3 Description",
  Level4   VARCHAR(1000)    NOT NULL                COMMENT "Background Level 4 Description",
  Level5   VARCHAR(1000)    NOT NULL                COMMENT "Background Level 5 Description",
  Level6   VARCHAR(255)     NULL                    COMMENT "Background Level 6 Description",
  Level7   VARCHAR(255)     NULL                    COMMENT "Background Level 7 Description",
  Level8   VARCHAR(255)     NULL                    COMMENT "Background Level 8 Description",
  Level9   VARCHAR(255)     NULL                    COMMENT "Background Level 9 Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Disciplines (
  ID     INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Discipline ID",
  Name   VARCHAR(64)      NOT NULL                COMMENT "Discipline Name",
  IsSorc TINYINT UNSIGNED NOT NULL                COMMENT "Is this Discipline a Sorcery-based Discipline?",
  Descr  VARCHAR(3000)    NOT NULL                COMMENT "Discipline Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Clans (
  ID            INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Clan ID",
  Name          VARCHAR(64)      NOT NULL                COMMENT "Clan Name",
  IsUgly        TINYINT UNSIGNED NOT NULL                COMMENT "Does this Clan have an Appearance 0?",
  ClanDiscID1   INT UNSIGNED     NOT NULL                COMMENT "[FK] Clan Discipline 1 ID",
  ClanDiscID2   INT UNSIGNED     NOT NULL                COMMENT "[FK] Clan Discipline 2 ID",
  ClanDiscID3   INT UNSIGNED     NOT NULL                COMMENT "[FK] Clan Discipline 3 ID",
  ClanDiscID4   INT UNSIGNED     NULL                    COMMENT "[FK] Clan Discipline 4 ID. Mostly Null, as only Gargoyles have 4 Clan Disciplines (Flight) in the first book",
  WeaknessShort VARCHAR(500)     NOT NULL                COMMENT "Clan Weaknesses - Short Description",
  WeaknessLong  VARCHAR(1000)    NOT NULL                COMMENT "Clan Weaknesses - Long Description",
  Descr         TEXT             NOT NULL                COMMENT "Full Clan Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name),
  FOREIGN KEY (ClanDiscID1) REFERENCES VtM20_Lookup_Disciplines(ID),
  FOREIGN KEY (ClanDiscID2) REFERENCES VtM20_Lookup_Disciplines(ID),
  FOREIGN KEY (ClanDiscID3) REFERENCES VtM20_Lookup_Disciplines(ID),
  FOREIGN KEY (ClanDiscID4) REFERENCES VtM20_Lookup_Disciplines(ID)
);
-- CREATE TABLE IF NOT EXISTS VtM20_Lookup_ComboDisciplines (
--   ID      INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "ComboDiscipline ID",
--   Name    VARCHAR(255)     NOT NULL                COMMENT "ComboDiscipline Name",
--   XPCost  TINYINT UNSIGNED NOT NULL                COMMENT "XP Cost to buy",
--   PreReqs VARCHAR(255)     NULL                    COMMENT "Pre-Requisites for this ComboDiscipline",
--   Descr   TEXT             NOT NULL                COMMENT "ComboDiscipline Description",
--   PRIMARY KEY (ID),
--   UNIQUE  KEY (Name)
-- );
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Disciplines_Powers (
  ID         INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Discipline Power ID",
  DiscID     INT UNSIGNED     NOT NULL                COMMENT "[FK] Discipline ID",
  Discipline VARCHAR(64)      NOT NULL                COMMENT "Discipline this Power belongs to",
  Level      TINYINT UNSIGNED NOT NULL                COMMENT "Level of Power",
  IsMultiBuy TINYINT UNSIGNED NOT NULL                COMMENT "Can this Power be bought multiple times?",
  HasNotes   TINYINT UNSIGNED NOT NULL                COMMENT "Does this Power require notes?",
  Name       VARCHAR(64)      NOT NULL                COMMENT "Discipline Power Name",
  Descr      VARCHAR(6000)    NOT NULL                COMMENT "Discipline Power Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name),
  FOREIGN KEY (DiscID) REFERENCES VtM20_Lookup_Disciplines(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Generations (
  ID           INT UNSIGNED      NOT NULL AUTO_INCREMENT COMMENT "Generation ID",
  Generation   TINYINT UNSIGNED  NOT NULL                COMMENT "Generation value",
  StatMax      TINYINT UNSIGNED  NOT NULL                COMMENT "Maximum Stat Level",
  BloodPerTurn TINYINT UNSIGNED  NOT NULL                COMMENT "Blood Spent per turn",
  BloodPool    SMALLINT UNSIGNED NOT NULL                COMMENT "Blood Pool",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Generation)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Merits (
  ID         INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Merit/Flaw ID",
  MType      VARCHAR(16)      NOT NULL                COMMENT "Merit Type - Physical, Mental, Social, Supernatural, etc.",
  Name       VARCHAR(64)      NOT NULL                COMMENT "Merit/Flaw ID",
  Cost       TINYINT SIGNED   NOT NULL                COMMENT "Freebie Point cost (Flaws have -ve Cost)",
  IsMultiBuy TINYINT UNSIGNED NOT NULL                COMMENT "Can this Merit/Flaw be bought multiple times?",
  HasNotes   TINYINT UNSIGNED NOT NULL                COMMENT "Does this Merit/Flaw require notes?",
  Descr      VARCHAR(2000)    NOT NULL                COMMENT "Merit/Flaw Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Morality (
  ID        INT UNSIGNED  NOT NULL AUTO_INCREMENT COMMENT "Morality ID",
  Name      VARCHAR(64)   NOT NULL                COMMENT "Name",
  Nickname  VARCHAR(128)  NOT NULL                COMMENT "Nickname",
  Virtues   VARCHAR(64)   NOT NULL                COMMENT "Virtues - As appear in book, separated by ' and '",
  Bearing   VARCHAR(512)  NOT NULL                COMMENT "Bearing",
  Beliefs   VARCHAR(3000) NOT NULL                COMMENT "Basic Beliefs",
  Ethics    VARCHAR(800)  NOT NULL                COMMENT "The Ethics of thr Path",
  History   VARCHAR(2048) NOT NULL                COMMENT "History",
  Practices VARCHAR(1200) NOT NULL                COMMENT "Current Practices",
  Followers VARCHAR(1024) NOT NULL                COMMENT "Description of Followers",
  Following VARCHAR(1024) NOT NULL                COMMENT "Following the Path",
  Abilities VARCHAR(1024) NOT NULL                COMMENT "Common Abilities",
  PrefDisc  VARCHAR(1024) NOT NULL                COMMENT "Preferred Disciplines",
  Sins      VARCHAR(2048) NOT NULL                COMMENT "Hierarchy of Sins (html table)",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Sorcery_Paths (
  ID       INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Sorcery Path ID",
  Name     VARCHAR(64)      NOT NULL                COMMENT "Sorcery Path Name",
  IsAssam  TINYINT UNSIGNED NOT NULL                COMMENT "Is this Path available to Assamite Sorcery?",
  IsKoldu  TINYINT UNSIGNED NOT NULL                COMMENT "Is this Path available to Koldunism?",
  IsNecro  TINYINT UNSIGNED NOT NULL                COMMENT "Is this Path available to Necromancy?",
  IsThaum  TINYINT UNSIGNED NOT NULL                COMMENT "Is this Path available to Thaumaturgy?",
  Descr    VARCHAR(3600)    NOT NULL                COMMENT "Sorcery Path Description",
  Level1   VARCHAR(3600)    NOT NULL                COMMENT "Sorcery Path Level 1 Description",
  Level2   VARCHAR(3600)    NOT NULL                COMMENT "Sorcery Path Level 2 Description",
  Level3   VARCHAR(3600)    NOT NULL                COMMENT "Sorcery Path Level 3 Description",
  Level4   VARCHAR(3600)    NOT NULL                COMMENT "Sorcery Path Level 4 Description",
  Level5   VARCHAR(3600)    NOT NULL                COMMENT "Sorcery Path Level 5 Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Sorcery_Rituals (
  ID       INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Sorcery Ritual ID",
  Name     VARCHAR(64)      NOT NULL                COMMENT "Sorcery Ritual Name",
  Level    TINYINT UNSIGNED NOT NULL                COMMENT "Sorcery Ritual Level",
  IsAssam  TINYINT UNSIGNED NOT NULL                COMMENT "Is this Ritual available to Assamite Sorcery?",
  IsKoldu  TINYINT UNSIGNED NOT NULL                COMMENT "Is this Ritual available to Koldunism?",
  IsNecro  TINYINT UNSIGNED NOT NULL                COMMENT "Is this Ritual available to Necromancy?",
  IsThaum  TINYINT UNSIGNED NOT NULL                COMMENT "Is this Ritual available to Thaumaturgy?",
  Descr    VARCHAR(4000)    NOT NULL                COMMENT "Sorcery Ritual Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Lookup_Virtues (
  ID      INT UNSIGNED  NOT NULL AUTO_INCREMENT COMMENT "Virtue ID",
  Name    VARCHAR(64)   NOT NULL                COMMENT "Virtue Name",
  Descr   VARCHAR(2000) NOT NULL                COMMENT "Virtue Description",
  Level1  VARCHAR(64)   NOT NULL                COMMENT "Virtue Level 1 Description",
  Level2  VARCHAR(64)   NOT NULL                COMMENT "Virtue Level 2 Description",
  Level3  VARCHAR(64)   NOT NULL                COMMENT "Virtue Level 3 Description",
  Level4  VARCHAR(64)   NOT NULL                COMMENT "Virtue Level 4 Description",
  Level5  VARCHAR(64)   NOT NULL                COMMENT "Virtue Level 5 Description",
  Level6  VARCHAR(64)   NULL                    COMMENT "Virtue Level 6 Description",
  Level7  VARCHAR(64)   NULL                    COMMENT "Virtue Level 7 Description",
  Level8  VARCHAR(64)   NULL                    COMMENT "Virtue Level 8 Description",
  Level9  VARCHAR(64)   NULL                    COMMENT "Virtue Level 9 Description",
  Level10 VARCHAR(64)   NULL                    COMMENT "Virtue Level 10 Description",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
-- 02 UGC
CREATE TABLE IF NOT EXISTS VtM20_Users (
  ID        INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "User ID",
  Name      VARCHAR(12)      NOT NULL                COMMENT "User Name",
  Pass      VARCHAR(24)      NOT NULL                COMMENT "User Password",
  FullName  VARCHAR(64)      NOT NULL                COMMENT "Full name of User",
  IsRevoked TINYINT UNSIGNED NOT NULL                COMMENT "Is this User ID Revoked?",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name)
);
CREATE TABLE IF NOT EXISTS VtM20_Games (
  ID             INT UNSIGNED     NOT NULL AUTO_INCREMENT   COMMENT "Game ID",
  Name           VARCHAR(64)      NOT NULL                  COMMENT "Game Name",
  StoryTellerID  INT UNSIGNED     NOT NULL                  COMMENT "[FK] User ID of this game's Storyteller",
  Logo           VARCHAR(64)      NOT NULL                  COMMENT "Game Logo filename",
  Abilities      VARCHAR(8)       NOT NULL DEFAULT '13/9/5' COMMENT "Base Abilities scores e.g. '13/9/5'",
  Attributes     VARCHAR(8)       NOT NULL DEFAULT '7/5/3'  COMMENT "Base Attributes scores e.g. '7/5/3'",
  Backgrounds    TINYINT UNSIGNED NOT NULL DEFAULT 5        COMMENT "Base Backgrounds Spend e.g. 5",
  Disciplines    TINYINT UNSIGNED NOT NULL DEFAULT 3        COMMENT "Base Disciplines Spend e.g. 3",
  Virtues        TINYINT UNSIGNED NOT NULL DEFAULT 7        COMMENT "Base Virtues Spend e.g. 3",
  FreebiePoints  TINYINT UNSIGNED NOT NULL DEFAULT 15       COMMENT "Base Freebie Points Spend e.g. 15",
  BaseGeneration TINYINT UNSIGNED NOT NULL DEFAULT 13       COMMENT "Base Generation e.g. 13",
  MaxBackgrounds TINYINT UNSIGNED NOT NULL DEFAULT 5        COMMENT "Maximum value of Backgrounds allowed e.g. 5"
  YBEarly        INT SIGNED       NOT NULL                  COMMENT "Earliest allowed IC Birth year",
  YBLate         INT SIGNED       NOT NULL                  COMMENT "Latest allowed IC Birth year",
  YEEarly        INT SIGNED       NOT NULL                  COMMENT "Earliest allowed IC Embrace year",
  YELate         INT SIGNED       NOT NULL                  COMMENT "Latest allowed IC Embrace year",
  ICDate         DATE             NOT NULL                  COMMENT "Game Current In Character Date - used to determine default Journal date on Calendar picker, and Gehenna Ticker if present",
  ICStart        DATE             NOT NULL                  COMMENT "IC Date the Game Started",
  Started        DATE             NOT NULL                  COMMENT "Date the Game started",
  Finished       DATE             NULL                      COMMENT "Date the Game finished",
  IsActive       TINYINT UNSIGNED NOT NULL                  COMMENT "Is This Game still active?",
  Display        TINYINT UNSIGNED NOT NULL                  COMMENT "Is This Game still to be displayed?",
  PRIMARY KEY (ID),
  UNIQUE  KEY (Name),
  FOREIGN KEY (StoryTellerID) REFERENCES VtM20_Users(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars (
  ID            INT UNSIGNED      NOT NULL AUTO_INCREMENT COMMENT "Character ID",
  Name          VARCHAR(64)       NOT NULL                COMMENT "Character Name",
  IsApproved    TINYINT UNSIGNED  NOT NULL                COMMENT "Is this Character Approved to play?",
  UserID        INT UNSIGNED      NOT NULL                COMMENT "[FK] User ID owner of Character",
  GameID        INT UNSIGNED      NOT NULL                COMMENT "[FK] Game ID this Character is in",
  ClanID        INT UNSIGNED      NOT NULL                COMMENT "[FK] Clan ID of Character Clan",
  NatureID      INT UNSIGNED      NOT NULL                COMMENT "[FK] Archetype ID of Character Nature",
  DemeanorID    INT UNSIGNED      NOT NULL                COMMENT "[FK] Archetype ID of Character Demeanor",
  MoralityID    INT UNSIGNED      NOT NULL                COMMENT "[FK] Morality ID of Character Morality",
  Morality      TINYINT UNSIGNED  NOT NULL                COMMENT "Character Morality",
  Willpower     TINYINT UNSIGNED  NOT NULL                COMMENT "Character Willpower",
  Generation    TINYINT UNSIGNED  NOT NULL                COMMENT "Character Generation",
  CurrWillpower TINYINT UNSIGNED  NOT NULL                COMMENT "Current Willpower",
  CurrBloodPool SMALLINT UNSIGNED NOT NULL                COMMENT "Current Bloodpool",
  XPTotal       SMALLINT UNSIGNED NOT NULL                COMMENT "Character XP Total awarded",
  XPAvail       SMALLINT UNSIGNED NOT NULL                COMMENT "Character XP available to spend",
  WeaknessNotes VARCHAR(255)      NOT NULL                COMMENT "Any additional notes for the Clan Weakness",
  Health0       TINYINT UNSIGNED  NOT NULL                COMMENT "Health Box 0 (Bruised for Huge Chars)",
  Health1       TINYINT UNSIGNED  NOT NULL                COMMENT "Health Box 1 (Bruised)",
  Health2       TINYINT UNSIGNED  NOT NULL                COMMENT "Health Box 2 (Hurt)",
  Health3       TINYINT UNSIGNED  NOT NULL                COMMENT "Health Box 3 (Injured)",
  Health4       TINYINT UNSIGNED  NOT NULL                COMMENT "Health Box 4 (Wounded)",
  Health5       TINYINT UNSIGNED  NOT NULL                COMMENT "Health Box 5 (Mauled)",
  Health6       TINYINT UNSIGNED  NOT NULL                COMMENT "Health Box 6 (Crippled)",
  Health7       TINYINT UNSIGNED  NOT NULL                COMMENT "Health Box 7 (Incapacitated)",
  IsUgly        TINYINT UNSIGNED  NOT NULL                COMMENT "Does this Character have App 0?",
  IsHuge        TINYINT UNSIGNED  NOT NULL                COMMENT "Does this Character have the background Huge Size?",
  IsSorc        TINYINT UNSIGNED  NOT NULL                COMMENT "Does this Character have any Sourcery-based Disciplines (Necromancy, Thaumaturgy)?",
  IsStarting    TINYINT UNSIGNED  NOT NULL                COMMENT "Is this a starting Character (Should have an odd no. ID)?",
  IsDead        TINYINT UNSIGNED  NOT NULL                COMMENT "Is this Character dead?",
  PRIMARY KEY (ID),
  FOREIGN KEY (UserID)     REFERENCES VtM20_Users(ID),
  FOREIGN KEY (GameID)     REFERENCES VtM20_Games(ID),
  FOREIGN KEY (ClanID)     REFERENCES VtM20_Lookup_Clans(ID),
  FOREIGN KEY (NatureID)   REFERENCES VtM20_Lookup_Archetypes(ID),
  FOREIGN KEY (DemeanorID) REFERENCES VtM20_Lookup_Archetypes(ID),
  FOREIGN KEY (MoralityID) REFERENCES VtM20_Lookup_Morality(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Games_Users (
  ID              INT UNSIGNED     NOT NULL AUTO_INCREMENT       COMMENT "User / Game relationship ID",
  GameID          INT UNSIGNED     NOT NULL                      COMMENT "[FK] ID of Game this User is playing",
  UserID          INT UNSIGNED     NOT NULL                      COMMENT "[FK] ID of User playing this Game",
  IsPlayer        TINYINT UNSIGNED NOT NULL                      COMMENT "Is this Person a Player in the Game? (0=guest)",
  DefaultCharID   INT UNSIGNED     NOT NULL                      COMMENT "[FK] ID of default Character for this User in this Game",
  DefaultHomepage VARCHAR(50)      NOT NULL DEFAULT 'mboard.htm' COMMENT "Default Homepage for this User in this Game",
  IsMBoardIC      TINYINT UNSIGNED NOT NULL                      COMMENT "Are the User's Message Board posts set to 'In Character' as default?",
  PRIMARY KEY (ID),
  FOREIGN KEY (GameID)        REFERENCES VtM20_Games(ID),
  FOREIGN KEY (UserID)        REFERENCES VtM20_Users(ID),
  FOREIGN KEY (DefaultCharID) REFERENCES VtM20_Chars(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Games_Advancement (
  ID             INT UNSIGNED     NOT NULL AUTO_INCREMENT     COMMENT "Game Advancement ID",
  GameID         INT UNSIGNED     NOT NULL                    COMMENT "[FK] ID of Game this User is playing",
  NewAbil        TINYINT UNSIGNED NOT NULL DEFAULT 3          COMMENT "XP Cost of new Ability",
  NewDisc        TINYINT UNSIGNED NOT NULL DEFAULT 10         COMMENT "XP Cost of new Discipline",
  NewPath        TINYINT UNSIGNED NOT NULL DEFAULT 7          COMMENT "XP Cost of new Necromancy or Thaumaturgy Path",
  AdvAttr        TINYINT UNSIGNED NOT NULL DEFAULT 4          COMMENT "XP Cost of advancing Attribute (current rating x this)",
  AdvAbil        TINYINT UNSIGNED NOT NULL DEFAULT 2          COMMENT "XP Cost of advancing Ability (current rating x this)",
  AdvAbilOther   TINYINT UNSIGNED NOT NULL DEFAULT 2          COMMENT "XP Cost of advancing Other Ability (current rating x this)",
  AdvDiscClan    TINYINT UNSIGNED NOT NULL DEFAULT 5          COMMENT "XP Cost of advancing Clan Discipline (current rating x this)",
  AdvDiscCaitiff TINYINT UNSIGNED NOT NULL DEFAULT 6          COMMENT "XP Cost of advancing Discipline for Caitiff/Pander (current rating x this)",
  AdvDiscNonClan TINYINT UNSIGNED NOT NULL DEFAULT 7          COMMENT "XP Cost of advancing Non-Clan Discipline (current rating x this)",
  AdvPath        TINYINT UNSIGNED NOT NULL DEFAULT 4          COMMENT "XP Cost of advancing Necromancy or Thaumaturgy Secondary Path (current rating x this)",
  AdvVirtues     TINYINT UNSIGNED NOT NULL DEFAULT 2          COMMENT "XP Cost of advancing Virtue (current rating x this)",
  AdvMorality    TINYINT UNSIGNED NOT NULL DEFAULT 2          COMMENT "XP Cost of advancing Humanity or Path of Enlightenment (current rating x this)",
  AdvWillpower   TINYINT UNSIGNED NOT NULL DEFAULT 1          COMMENT "XP Cost of advancing Willpower (current rating x this)",
  Ritual1        VARCHAR(16)      NOT NULL DEFAULT '1 week'   COMMENT "Time it takes to learn a Level 1 Ritual",
  Ritual2        VARCHAR(16)      NOT NULL DEFAULT '1 month'  COMMENT "Time it takes to learn a Level 2 Ritual",
  Ritual3        VARCHAR(16)      NOT NULL DEFAULT '3 months' COMMENT "Time it takes to learn a Level 3 Ritual",
  Ritual4        VARCHAR(16)      NOT NULL DEFAULT '6 months' COMMENT "Time it takes to learn a Level 4 Ritual",
  Ritual5        VARCHAR(16)      NOT NULL DEFAULT '1 year'   COMMENT "Time it takes to learn a Level 5 Ritual",
  Ritual6        VARCHAR(16)      NOT NULL DEFAULT '2 years'  COMMENT "Time it takes to learn a Level 6 Ritual",
  Ritual7        VARCHAR(16)      NOT NULL DEFAULT '4 years'  COMMENT "Time it takes to learn a Level 7 Ritual",
  Ritual8        VARCHAR(16)      NOT NULL DEFAULT '8 years'  COMMENT "Time it takes to learn a Level 8 Ritual",
  Ritual9        VARCHAR(16)      NOT NULL DEFAULT '16 years' COMMENT "Time it takes to learn a Level 9 Ritual",
  PRIMARY KEY (ID),
  UNIQUE  KEY (GameID),
  FOREIGN KEY (GameID) REFERENCES VtM20_Games(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Games_Alerts (
  ID         INT UNSIGNED     NOT NULL AUTO_INCREMENT            COMMENT "Alert ID",
  GameID     INT UNSIGNED     NOT NULL                           COMMENT "[FK] Game ID this Alert belongs to",
  FromUserID INT UNSIGNED     NOT NULL                           COMMENT "[FK] From this User ID",
  ToUserID   INT UNSIGNED     NOT NULL                           COMMENT "[FK] To this User ID",
  DTStamp    TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "Timestamp of the Alert",
  IsRead     TINYINT UNSIGNED NOT NULL                           COMMENT "Has this Alert been read by this User?",
  Message    VARCHAR(255)     NOT NULL                           COMMENT "Alert Message",
  PRIMARY KEY (ID),
  FOREIGN KEY (GameID)     REFERENCES VtM20_Games(ID),
  FOREIGN KEY (FromUserID) REFERENCES VtM20_Users(ID),
  FOREIGN KEY (ToUserID)   REFERENCES VtM20_Users(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Games_Chars (
  ID      INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Games / Chars relationship ID",
  GameID  INT UNSIGNED     NOT NULL                COMMENT "[FK] Game ID of Game",
  CharID  INT UNSIGNED     NOT NULL                COMMENT "[FK] Character ID playing in this Game",
  IsPC    TINYINT UNSIGNED NOT NULL                COMMENT "Is this Character a Player Character (PC)?",
  InParty TINYINT UNSIGNED NOT NULL                COMMENT "Is this Character in the current party?",
  PRIMARY KEY (ID),
  FOREIGN KEY (GameID) REFERENCES VtM20_Games(ID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Games_Messageboard (
  ID         INT UNSIGNED     NOT NULL AUTO_INCREMENT            COMMENT "Messageboard Message ID",
  GameID     INT UNSIGNED     NOT NULL                           COMMENT "[FK] Game ID this message is for",
  Name       VARCHAR(64)      NOT NULL                           COMMENT "Name that has posted the message (can be a User Name for OOC messages, or a Char Name, for IC messages)",
  IsIC       TINYINT UNSIGNED NOT NULL                           COMMENT "Is this an In Character (IC) message?",
  DTStamp    TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "Timestamp of the message",
  Message    TEXT             NOT NULL                           COMMENT "Message contents",
  PrivUserID INT UNSIGNED     NOT NULL                           COMMENT "[FK] UserID this private message is for (to read on their Private Messageboard)",
  PRIMARY KEY (ID),
  FOREIGN KEY (GameID)     REFERENCES VtM20_Games(ID),
  FOREIGN KEY (PrivUserID) REFERENCES VtM20_Users(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Games_Prohibit (
  ID              INT UNSIGNED      NOT NULL AUTO_INCREMENT            COMMENT "Prohibited Thing ID",
  GameID          INT UNSIGNED      NOT NULL                           COMMENT "[FK] Game ID this Prohibited Thing applies to",
  LookupTable     VARCHAR(255)      NOT NULL                           COMMENT "Lookup Table that this Prohibited Thing appears on (stored without the 'VtM20_Lookup_' prefix)",
  ProhibitID      INT UNSIGNED      NOT NULL                           COMMENT "ID of Prohibited Thing on this Lookup Table",
  PRIMARY KEY (ID),
  FOREIGN KEY (GameID) REFERENCES VtM20_Games(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Games_Sessions (
  ID      INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT "Session ID",
  GameID  INT UNSIGNED NOT NULL                COMMENT "[FK] Game ID this Session data applies to",
  Name    VARCHAR(255) NULL                    COMMENT "Title of this Session (if reqd)",
  Session DATE         NOT NULL                COMMENT "RL Date of Session",
  InChar  DATE         NOT NULL                COMMENT "IC Date of Session",
  PRIMARY KEY (ID),
  FOREIGN KEY (GameID) REFERENCES VtM20_Games(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Abilities (
  ID                 INT UNSIGNED      NOT NULL AUTO_INCREMENT COMMENT "Character Ability ID",
  CharID             INT UNSIGNED      NOT NULL                COMMENT "[FK] Character ID",
  Alertness          TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Alertness",
  AlertnessNotes     VARCHAR(255)      NULL                    COMMENT "Alertness Notes",
  Athletics          TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Athletics",
  AthleticsNotes     VARCHAR(255)      NULL                    COMMENT "Athletics Notes",
  Awareness          TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Awareness",
  AwarenessNotes     VARCHAR(255)      NULL                    COMMENT "Awareness Notes",
  Brawl              TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Brawl",
  BrawlNotes         VARCHAR(255)      NULL                    COMMENT "Brawl Notes",
  Empathy            TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Empathy",
  EmpathyNotes       VARCHAR(255)      NULL                    COMMENT "Empathy Notes",
  Expression         TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Expression",
  ExpressionNotes    VARCHAR(255)      NULL                    COMMENT "Expression Notes",
  Intimidation       TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Intimidation",
  IntimidationNotes  VARCHAR(255)      NULL                    COMMENT "Intimidation Notes",
  Leadership         TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Leadership",
  LeadershipNotes    VARCHAR(255)      NULL                    COMMENT "Leadership Notes",
  Streetwise         TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Streetwise",
  StreetwiseNotes    VARCHAR(255)      NULL                    COMMENT "Streetwise Notes",
  Subterfuge         TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Subterfuge",
  SubterfugeNotes    VARCHAR(255)      NULL                    COMMENT "Subterfuge Notes",
  Animal_Ken         TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Animal Ken",
  Animal_KenNotes    VARCHAR(255)      NULL                    COMMENT "Animal Ken Notes",
  Crafts             TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Crafts",
  CraftsNotes        VARCHAR(255)      NULL                    COMMENT "Crafts Notes",
  Drive              TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Drive",
  DriveNotes         VARCHAR(255)      NULL                    COMMENT "Drive Notes",
  Etiquette          TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Etiquette",
  EtiquetteNotes     VARCHAR(255)      NULL                    COMMENT "Etiquette Notes",
  Firearms           TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Firearms",
  FirearmsNotes      VARCHAR(255)      NULL                    COMMENT "Firearms Notes",
  Larceny            TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Larceny",
  LarcenyNotes       VARCHAR(255)      NULL                    COMMENT "Larceny Notes",
  Melee              TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Melee",
  MeleeNotes         VARCHAR(255)      NULL                    COMMENT "Melee Notes",
  Performance        TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Performance",
  PerformanceNotes   VARCHAR(255)      NULL                    COMMENT "Performance Notes",
  Stealth            TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Stealth",
  StealthNotes       VARCHAR(255)      NULL                    COMMENT "Stealth Notes",
  Survival           TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Survival",
  SurvivalNotes      VARCHAR(255)      NULL                    COMMENT "Survival Notes",
  Academics          TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Academics",
  AcademicsNotes     VARCHAR(255)      NULL                    COMMENT "Academics Notes",
  Computers          TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Computers",
  ComputersNotes     VARCHAR(255)      NULL                    COMMENT "Computers Notes",
  Finance            TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Finance",
  FinanceNotes       VARCHAR(255)      NULL                    COMMENT "Finance Notes",
  Investigation      TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Investigation",
  InvestigationNotes VARCHAR(255)      NULL                    COMMENT "Investigation Notes",
  Law                TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Law",
  LawNotes           VARCHAR(255)      NULL                    COMMENT "Law Notes",
  Medicine           TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Medicine",
  MedicineNotes      VARCHAR(255)      NULL                    COMMENT "Medicine Notes",
  Occult             TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Occult",
  OccultNotes        VARCHAR(255)      NULL                    COMMENT "Occult Notes",
  Politics           TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Politics",
  PoliticsNotes      VARCHAR(255)      NULL                    COMMENT "Politics Notes",
  Science            TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Science",
  ScienceNotes       VARCHAR(255)      NULL                    COMMENT "Science Notes",
  Technology         TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Technology",
  TechnologyNotes    VARCHAR(255)      NULL                    COMMENT "Technology Notes",
  PRIMARY KEY (ID),
  UNIQUE  KEY (CharID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Abilities_Other (
  ID        INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Character Other Ability ID",
  CharID    INT UNSIGNED     NOT NULL                COMMENT "[FK] Character ID that owns this Other Ability",
  AbilityID INT UNSIGNED     NOT NULL                COMMENT "[FK] Other Ability ID owned by this Character",
  Value     TINYINT UNSIGNED NOT NULL DEFAULT 1      COMMENT "Level of Other Ability known by this Character",
  Notes     VARCHAR(255)     NULL                    COMMENT "Character Notes for this Other Ability (specializations, for example)",
  PRIMARY KEY (ID),
  UNIQUE  KEY (CharID,AbilityID),
  FOREIGN KEY (CharID)    REFERENCES VtM20_Chars(ID),
  FOREIGN KEY (AbilityID) REFERENCES VtM20_Lookup_Abilities_Other(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Attributes (
  ID                INT UNSIGNED      NOT NULL AUTO_INCREMENT COMMENT "Character Attribute ID",
  CharID            INT UNSIGNED      NOT NULL                COMMENT "[FK] Character ID",
  Strength          TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Strength",
  StrengthNotes     VARCHAR(255)      NULL                    COMMENT "Strength - Notes",
  Dexterity         TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Dexterity",
  DexterityNotes    VARCHAR(255)      NULL                    COMMENT "Dexterity - Notes",
  Stamina           TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Stamina",
  StaminaNotes      VARCHAR(255)      NULL                    COMMENT "Stamina - Notes",
  Charisma          TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Charisma",
  CharismaNotes     VARCHAR(255)      NULL                    COMMENT "Charisma - Notes",
  Manipulation      TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Manipulation",
  ManipulationNotes VARCHAR(255)      NULL                    COMMENT "Manipulation - Notes",
  Appearance        TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Appearance",
  AppearanceNotes   VARCHAR(255)      NULL                    COMMENT "Appearance - Notes",
  Perception        TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Perception",
  PerceptionNotes   VARCHAR(255)      NULL                    COMMENT "Perception - Notes",
  Intelligence      TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Intelligence",
  IntelligenceNotes VARCHAR(255)      NULL                    COMMENT "Intelligence - Notes",
  Wits              TINYINT UNSIGNED  NOT NULL DEFAULT 0      COMMENT "Wits",
  WitsNotes         VARCHAR(255)      NULL                    COMMENT "Wits - Notes",
  PRIMARY KEY (ID),
  UNIQUE  KEY (CharID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Backgrounds (
  ID      INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Character / Background relationship ID",
  CharID  INT UNSIGNED     NOT NULL                COMMENT "[FK] Character ID that owns this Background",
  BackgID INT UNSIGNED     NOT NULL                COMMENT "[FK] Background ID owned by this Character",
  Value   TINYINT UNSIGNED NOT NULL                COMMENT "Level of Background owned by this Character",
  Notes   VARCHAR(255)     NULL                    COMMENT "Character Notes for this Background (names, for example)",
  PRIMARY KEY (ID),
  UNIQUE  KEY (CharID,BackgID),
  FOREIGN KEY (CharID)  REFERENCES VtM20_Chars(ID),
  FOREIGN KEY (BackgID) REFERENCES VtM20_Lookup_Backgrounds(ID)
);
-- CREATE TABLE IF NOT EXISTS VtM20_Chars_ComboDisciplines (
--   ID      INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT "Character / ComboDiscipline relationship ID",
--   CharID  INT UNSIGNED NOT NULL                COMMENT "[FK] Character ID that owns this ComboDiscipline",
--   ComboID INT UNSIGNED NOT NULL                COMMENT "[FK] Combo Discipline ID owned by this Character",
--   PRIMARY KEY (ID),
--   UNIQUE  KEY (CharID,ComboID),
--   FOREIGN KEY (CharID)  REFERENCES VtM20_Chars(ID),
--   FOREIGN KEY (ComboID) REFERENCES VtM20_Lookup_ComboDisciplines(ID)
-- );
CREATE TABLE IF NOT EXISTS VtM20_Chars_Creation (
  ID           INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Character Creation Data ID",
  CharID       INT UNSIGNED     NOT NULL                COMMENT "[FK] Character ID that owns this Creation Data",
  PriorityAttr CHAR(3)          NOT NULL                COMMENT "Priority of Attributes (in Phys, Socal, Mental order) e.g. '123', '312' etc.",
  PriorityAbil CHAR(3)          NOT NULL                COMMENT "Priority of Abilities (in Talents, Skills, Knowl order) e.g. '123', '312' etc.",
  AbilSpend    TINYINT UNSIGNED NOT NULL DEFAULT 0      COMMENT "Ability Points spent",
  AttrSpend    TINYINT UNSIGNED NOT NULL DEFAULT 0      COMMENT "Attribute Points spent",
  DiscSpend    TINYINT UNSIGNED NOT NULL DEFAULT 0      COMMENT "Discipline Points spent",
  BackSpend    TINYINT UNSIGNED NOT NULL DEFAULT 0      COMMENT "Background Points spent",
  MeriSpend    TINYINT UNSIGNED NOT NULL DEFAULT 0      COMMENT "Merits/Flaws Points spent",
  FreeSpend    TINYINT UNSIGNED NOT NULL DEFAULT 0      COMMENT "Freebie Points spent",
  VirtSpend    TINYINT UNSIGNED NOT NULL DEFAULT 0      COMMENT "Virtue Points spent",
  PRIMARY KEY (ID),
  UNIQUE  KEY (CharID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Derangements (
  ID          INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Character Derangements ID",
  CharID      INT UNSIGNED     NOT NULL                COMMENT "[FK] Character ID that has this Derangement",
  Derangement VARCHAR(64)      NOT NULL                COMMENT "Derangement this Character has",
  IsPermanent TINYINT UNSIGNED NOT NULL                COMMENT "Is this Derangement Permanent?",
  WillCost    TINYINT UNSIGNED NOT NULL                COMMENT "How many Willpower points need to spend to recover from this Derangement",
  WillSpend   TINYINT UNSIGNED NOT NULL                COMMENT "How many Willpower points spent to date to recover from this Derangement",
  PRIMARY KEY (ID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Disciplines (
  ID     INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Character / Discipline relationship ID",
  CharID INT UNSIGNED     NOT NULL                COMMENT "[FK] Character ID that owns this Discipline",
  DiscID INT UNSIGNED     NOT NULL                COMMENT "[FK] Discipline ID owned by this Character",
  Value  INT UNSIGNED     NOT NULL                COMMENT "Level that this Character know this Discipline to",
  IsClan TINYINT UNSIGNED NOT NULL DEFAULT 0      COMMENT "Is this a Clan Discipline for this character? (inc. Flight for Gargoyles/Additional Discipline [Merit])",
  Notes  VARCHAR(255)     NULL                    COMMENT "Character Notes for this Discipline (unlikely to be used)",
  PRIMARY KEY (ID),
  UNIQUE  KEY (CharID,DiscID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID),
  FOREIGN KEY (DiscID) REFERENCES VtM20_Lookup_Disciplines(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Disciplines_Powers (
  ID     INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT "Character / Discipline Powers relationship ID",
  CharID INT UNSIGNED NOT NULL                COMMENT "[FK] Character ID that owns this Discipline Power",
  DiscID INT UNSIGNED NOT NULL                COMMENT "[FK] Discipline Power ID that is owned by this Character",
  Notes  VARCHAR(255) NULL                    COMMENT "Character Notes for this Discipline Power",
  PRIMARY KEY (ID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID),
  FOREIGN KEY (DiscID) REFERENCES VtM20_Lookup_Disciplines_Powers(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Journals (
  ID        INT UNSIGNED     NOT NULL AUTO_INCREMENT            COMMENT "Journal ID",
  IsDeleted TINYINT UNSIGNED NOT NULL                           COMMENT "Has this Journal been deleted?",
  GameID    INT UNSIGNED     NOT NULL                           COMMENT "[FK] Game ID this Journal belongs to",
  CharID    INT UNSIGNED     NOT NULL                           COMMENT "[FK] Character ID this Journal belongs to",
  Posted    TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "Timestamp of when Journal was posted",
  Edited    DATETIME         NULL                               COMMENT "DateTime Timestamp of when Journal was last Edited (will need to be set in the SQL command, as MySql version is pre-5.6.5)",
  InChar    DATE             NOT NULL                           COMMENT "In Character (IC) Date when Journal was posted",
  Title     VARCHAR(255)     NOT NULL                           COMMENT "Journal Title",
  Entry     TEXT             NOT NULL                           COMMENT "Journal Entry",
  PRIMARY KEY (ID),
  FOREIGN KEY (GameID) REFERENCES VtM20_Games(ID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Merits (
  ID      INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT "Character / Merit/Flaw relationship ID",
  CharID  INT UNSIGNED NOT NULL                COMMENT "[FK] Character ID that has this Merit/Flaw",
  MeritID INT UNSIGNED NOT NULL                COMMENT "[FK] Merit/Flaw ID that this Character has",
  Notes   VARCHAR(255) NULL                    COMMENT "Character Notes for this Merit/Flaw",
  PRIMARY KEY (ID),
  FOREIGN KEY (CharID)  REFERENCES VtM20_Chars(ID),
  FOREIGN KEY (MeritID) REFERENCES VtM20_Lookup_Merits(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Notes (
  ID       INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT "Character Notes ID",
  CharID   INT UNSIGNED NOT NULL                COMMENT "[FK] Character ID that these Notes belong to",
  Haven    VARCHAR(255) NOT NULL                COMMENT "Character's Haven",
  Concept  VARCHAR(64)  NOT NULL                COMMENT "Character Concept",
  Sire     VARCHAR(64)  NOT NULL                COMMENT "Character's Sire",
  Birth    DATE         NOT NULL                COMMENT "Character's Date of Birth",
  Embrace  DATE         NOT NULL                COMMENT "Character's Date of Embrace",
  Image    VARCHAR(64)  NULL                    COMMENT "Filename of Character picture",
  Notes    TEXT         NULL                    COMMENT "Character Player Notes",
  History  TEXT         NULL                    COMMENT "Character History",
  WishList TEXT         NULL                    COMMENT "Character XP Spend Wishlist",
  STNotes  TEXT         NULL                    COMMENT "Storyteller Notes for this character",
  PRIMARY KEY (ID),
  UNIQUE  KEY (CharID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Sorcery_Paths (
  ID        INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Character / Sorcery Path relationship ID",
  CharID    INT UNSIGNED     NOT NULL                COMMENT "[FK] Character ID that knows this Sorcery Path",
  PathID    INT UNSIGNED     NOT NULL                COMMENT "[FK] Sorcery Path ID that is known by this Character",
  PathOrder TINYINT UNSIGNED NOT NULL                COMMENT "Order in which this Path has been learned by this Character",
  Value     TINYINT UNSIGNED NOT NULL                COMMENT "Level of Path that this Character knows",
  PRIMARY KEY (ID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID),
  FOREIGN KEY (PathID) REFERENCES VtM20_Lookup_Sorcery_Paths(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Sorcery_Rituals (
  ID       INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT "Character / Sorcery Ritual relationship ID",
  CharID   INT UNSIGNED NOT NULL                COMMENT "[FK] Character ID that knows this Sorcery Ritual",
  RitualID INT UNSIGNED NOT NULL                COMMENT "[FK] Sorcery Ritual ID that is known by this Character",
  Notes    VARCHAR(255) NULL                    COMMENT "Character Notes on this Sorcery Ritual",
  PRIMARY KEY (ID),
  FOREIGN KEY (CharID)   REFERENCES VtM20_Chars(ID),
  FOREIGN KEY (RitualID) REFERENCES VtM20_Lookup_Sorcery_Rituals(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Vinculum (
  ID         INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Vinculum ID",
  FromCharID INT UNSIGNED     NOT NULL                COMMENT "[FK] Character that is the object of this Vinculum",
  ToCharID   INT UNSIGNED     NOT NULL                COMMENT "[FK] Character that is the target of this Vinculum",
  Rating     TINYINT UNSIGNED NOT NULL                COMMENT "Level Rating of this Vinculum",
  PRIMARY KEY (ID),
  UNIQUE  KEY (FromCharID, ToCharID),
  UNIQUE  KEY (ToCharID, FromCharID),
  FOREIGN KEY (FromCharID) REFERENCES VtM20_Chars(ID),
  FOREIGN KEY (ToCharID)   REFERENCES VtM20_Chars(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Chars_Virtues (
  ID       INT UNSIGNED     NOT NULL AUTO_INCREMENT COMMENT "Character / Virtue relationship ID",
  CharID   INT UNSIGNED     NOT NULL                COMMENT "[FK] Character ID that has this Virtue",
  VirtueID INT UNSIGNED     NOT NULL                COMMENT "[FK] Virtue ID that this Character has",
  Value    TINYINT UNSIGNED NOT NULL                COMMENT "Level of Virtue that this Character has",
  PRIMARY KEY (ID),
  UNIQUE  KEY (CharID, VirtueID),
  FOREIGN KEY (CharID)   REFERENCES VtM20_Chars(ID),
  FOREIGN KEY (VirtueID) REFERENCES VtM20_Lookup_Virtues(ID)
);
-- 03 Log Tables
CREATE TABLE IF NOT EXISTS VtM20_Logs_Admin_Pages (
  GameID INT UNSIGNED NOT NULL COMMENT "[FK] Game ID of page access",
  Page   VARCHAR(255) NOT NULL COMMENT "Name of page accessed",
  Hits   INT UNSIGNED NOT NULL COMMENT "Number of time this page has been accessed",
  PRIMARY KEY (GameID,Page),
  FOREIGN KEY (GameID) REFERENCES VtM20_Games(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Logs_Admin_Login (
  ID      INT UNSIGNED NOT NULL AUTO_INCREMENT            COMMENT "Login record ID",
  DTStamp TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "Timestamp of the Login",
  UserID  INT UNSIGNED NOT NULL                           COMMENT "[FK] User ID of User that has logged in",
  PRIMARY KEY (ID),
  FOREIGN KEY (UserID) REFERENCES VtM20_Users(ID)
);
CREATE TABLE IF NOT EXISTS VtM20_Logs_Chars_Edits (
  ID          INT UNSIGNED     NOT NULL AUTO_INCREMENT            COMMENT "Character Edit ID",
  DTStamp     TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "Timestamp of the Char Edit",
  UserID      INT UNSIGNED     NOT NULL                           COMMENT "[FK] User ID that has Edited this Char",
  GameID      INT UNSIGNED     NOT NULL                           COMMENT "[FK] Game ID of Char Edit",
  CharID      INT UNSIGNED     NOT NULL                           COMMENT "[FK] Character ID that has been Edited",
  IsAdminEdit TINYINT UNSIGNED NOT NULL                           COMMENT "Was this change done by Game Admin?",
  StatType    VARCHAR(64)      NOT NULL                           COMMENT "Stat type bought (Attr,Abil,etc.)",
  Stat        VARCHAR(64)      NOT NULL                           COMMENT "Stat bought",
  Value       TINYINT UNSIGNED NOT NULL                           COMMENT "Level of Stat bought (0 if n/a)",
  Cost        TINYINT UNSIGNED NOT NULL                           COMMENT "XP cost of this Stat increase (0 if n/a or Admin edit)",
  Notes       TEXT             NULL                               COMMENT "Any Notes altered",
  PRIMARY KEY (ID),
  FOREIGN KEY (UserID) REFERENCES VtM20_Users(ID),
  FOREIGN KEY (GameID) REFERENCES VtM20_Games(ID),
  FOREIGN KEY (CharID) REFERENCES VtM20_Chars(ID)
);

-- Load next script
SOURCE 03_VtM20_Insert_Lookups.sql;
