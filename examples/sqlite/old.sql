-- Structure
CREATE TABLE Traits (
  Name TEXT PRIMARY KEY,
  Type TEXT,
  Base      INT DEFAULT 0,  -- Points given at First step
  Freebie   INT DEFAULT 0,  -- Points gained through Freebie
  XP        INT DEFAULT 0   -- Points gained through experience
  CHECK(Type IN (
    -- Attributes
    'Physical', 
    'Social', 
    'Mental', 
    -- Abilities
    'Talent',
    'Skill',
    'Knowledge',
    -- Advantages
    'Discipline',
    'Background',
    'Virtue',
    'Path of Enlighment'
  )) NOT NULL
);

CREATE TABLE Merits (
  Name TEXT PRIMARY KEY,
  Points INT
);

CREATE TABLE Properties (
  Name TEXT PRIMARY KEY,
  Value TEXT
);


-- How Many Damaged taken?
CREATE TABLE Damage (
  Aggravated BOOLEAN
);


---------------------------------------------------------------
-- Data
INSERT INTO Properties VALUES ('Name', NULL);
INSERT INTO Properties VALUES ('Player', NULL);
INSERT INTO Properties VALUES ('Chronicle', NULL);

INSERT INTO Properties VALUES ('Nature', NULL);
INSERT INTO Properties VALUES ('Demeanor', NULL);
INSERT INTO Properties VALUES ('Concept', NULL);

INSERT INTO Properties VALUES ('Clan', NULL);
-- Generation is computed with its corresponding Merit/Flaw
INSERT INTO Properties VALUES ('Sire', NULL);
INSERT INTO Properties VALUES ('Path of Enlighment', 'Humanity');


-- Attributes
INSERT INTO Traits (Name, Type) VALUES ('Strength',  'Physical');
INSERT INTO Traits (Name, Type) VALUES ('Dexterity', 'Physical');
INSERT INTO Traits (Name, Type) VALUES ('Stamina',   'Physical');

INSERT INTO Traits (Name, Type) VALUES ('Charisma',  'Social');
INSERT INTO Traits (Name, Type) VALUES ('Manipulation',  'Social');
INSERT INTO Traits (Name, Type) VALUES ('Apearance',  'Social');

INSERT INTO Traits (Name, Type) VALUES ('Perception',  'Mental');
INSERT INTO Traits (Name, Type) VALUES ('Intelligence',  'Mental');
INSERT INTO Traits (Name, Type) VALUES ('Wits',  'Mental');

-- Abilities
INSERT INTO Traits (Name, Type) VALUES ('Alertness',  'Talent');
INSERT INTO Traits (Name, Type) VALUES ('Athletics',  'Talent');
INSERT INTO Traits (Name, Type) VALUES ('Awareness',  'Talent');
INSERT INTO Traits (Name, Type) VALUES ('Brawl',  'Talent');
INSERT INTO Traits (Name, Type) VALUES ('Empathy',  'Talent');
INSERT INTO Traits (Name, Type) VALUES ('Expression',  'Talent');
INSERT INTO Traits (Name, Type) VALUES ('Intimidation',  'Talent');
INSERT INTO Traits (Name, Type) VALUES ('Leadership',  'Talent');
INSERT INTO Traits (Name, Type) VALUES ('Streetwise',  'Talent');
INSERT INTO Traits (Name, Type) VALUES ('Subterfuge',  'Talent');

INSERT INTO Traits (Name, Type) VALUES ('Animal Ken',  'Skill');
INSERT INTO Traits (Name, Type) VALUES ('Crafts',  'Skill');
INSERT INTO Traits (Name, Type) VALUES ('Drive',  'Skill');
INSERT INTO Traits (Name, Type) VALUES ('Etiquette',  'Skill');
INSERT INTO Traits (Name, Type) VALUES ('Firearms',  'Skill');
INSERT INTO Traits (Name, Type) VALUES ('Larceny',  'Skill');
INSERT INTO Traits (Name, Type) VALUES ('Melee',  'Skill');
INSERT INTO Traits (Name, Type) VALUES ('Performance',  'Skill');
INSERT INTO Traits (Name, Type) VALUES ('Stealth',  'Skill');
INSERT INTO Traits (Name, Type) VALUES ('Survival',  'Skill');

INSERT INTO Traits (Name, Type) VALUES ('Academics',  'Knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Computer',  'Knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Finance',  'Knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Investigation',  'Knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Law',  'Knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Medicine',  'Knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Occult',  'Knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Politics',  'Knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Science',  'Knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Technology',  'Knowledge');


INSERT INTO Traits (Name, Type) VALUES ('Conscience',  'Virtue');
INSERT INTO Traits (Name, Type) VALUES ('Self-Control',  'Virtue');
INSERT INTO Traits (Name, Type) VALUES ('Willpower',  'Virtue');

INSERT INTO Traits (Name, Type) VALUES ('Humanity', 'Path of Enlighment');

UPDATE Properties SET Value='Name' WHERE Name = 'Name';
UPDATE Properties SET Value='Tzimiske' WHERE Name = 'Clan';


-- Attributes
UPDATE Traits SET Base = 2, XP = 1 WHERE Name = 'Strength';
UPDATE Traits SET Base = 2 WHERE Name = 'Dexterity';
UPDATE Traits SET Base = 4 WHERE Name = 'Stamina';

UPDATE Traits SET Base = 1 WHERE Name = 'Charisma';
UPDATE Traits SET Base = 3 WHERE Name = 'Manipulation';
UPDATE Traits SET Base = 2 WHERE Name = 'Appearance';

UPDATE Traits SET Base = 4 WHERE Name = 'Perception';
UPDATE Traits SET Base = 3 WHERE Name = 'Intelligence';
UPDATE Traits SET Base = 3 WHERE Name = 'Wits';



-- Talents
UPDATE Traits SET Base = 2 WHERE Name = 'Alertness';
UPDATE Traits SET Base = 1 WHERE Name = 'Athletics';
UPDATE Traits SET Base = 2 WHERE Name = 'Brawl';
UPDATE Traits SET Base = 1 WHERE Name = 'Expression';
UPDATE Traits SET Base = 3 WHERE Name = 'Intimidation';
UPDATE Traits SET Base = 3 WHERE Name = 'Leadership';
UPDATE Traits SET Base = 1 WHERE Name = 'Streetwise';


-- Skills
INSERT INTO Traits (Name, Type, Freebie) VALUES ('Crafts(Bodyart)',  'Skill', 3);
UPDATE Traits SET Base = 2 WHERE Name = 'Drive';
UPDATE Traits SET Base = 2 WHERE Name = 'Firearms';
UPDATE Traits SET Base = 2 WHERE Name = 'Larceny';
UPDATE Traits SET Base = 1 WHERE Name = 'Melee';
UPDATE Traits SET Base = 2 WHERE Name = 'Stealth';

-- Knowledge
UPDATE Traits SET Base = 1 WHERE Name = 'Computer';
UPDATE Traits SET Base = 2 WHERE Name = 'Finance';
INSERT INTO Traits (Name, Type, Base) VALUES ('Linguistics',  'Knowledge', 2);

-- Virtues
UPDATE Traits SET Base = 1 WHERE Name = 'Conscience';
UPDATE Traits SET Base = 3 WHERE Name = 'Self-Control';
UPDATE Traits SET Base = 3 WHERE Name = 'Courage';

-- Disciplines
INSERT INTO Traits (Name, Type, Base) VALUES('Auspex', 'Discipline', 1);
INSERT INTO Traits (Name, Type, Base, Freebie) VALUES('Vicissitude', 'Discipline', 1, 1);
INSERT INTO Traits (Name, Type, Base) VALUES('Animalism', 'Discipline', 1);

-- Backgrounds
INSERT INTO Traits (Name, Type, Base, Freebie) VALUES ('Resources', 'Background', 3, 0);
INSERT INTO Traits (Name, Type, Base, Freebie) VALUES ('Fame', 'Background', 1, 0);
INSERT INTO Traits (Name, Type, Base, Freebie) VALUES ('Allies', 'Background', 1, 1);


-- Humanity
UPDATE Traits SET Freebie = 1 WHERE Name = 'Humanity';
