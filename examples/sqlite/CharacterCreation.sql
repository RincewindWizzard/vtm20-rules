PRAGMA foreign_keys = ON;
CREATE TABLE TraitCategories (
  Name TEXT PRIMARY KEY,
  Type TEXT
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
    'Willpower',
    'Path of Enlighment'
  )) NOT NULL
);

-- This Table contains a list of all Dots (Base, Freebie, XP) spent.
-- Beware that Dots != Freebie/XP spent!

CREATE TABLE Dots (
  Type TEXT,
  Trait TEXT,
  time t TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  CHECK(Type IN ('Base', 'Creation', 'Freebie', 'XP')) NOT NULL,
  FOREIGN KEY(Trait) REFERENCES TraitCategories(Name)
);

CREATE TABLE CreationDots (
  Type Text,
  Amount INTEGER
);


CREATE VIEW Traits AS
SELECT Name, TraitCategories.Type as Type, COUNT(Dots.Trait) as Dots
FROM TraitCategories
LEFT OUTER JOIN Dots ON Dots.Trait = TraitCategories.Name
GROUP BY Name;

CREATE VIEW DotsSpent AS
SELECT TraitCategories.Type AS Type, Dots.Type AS DotType, COUNT() as Dots
FROM Dots 
LEFT OUTER JOIN TraitCategories 
ON Dots.Trait = TraitCategories.Name 
GROUP BY TraitCategories.Type, Dots.Type;

CREATE VIEW Attributes AS
SELECT *
FROM Traits
WHERE Type in ('Physical', 'Social', 'Mental');

-- Order of Primary, secondary, tertiary Attributes
CREATE VIEW AttributeOrder AS
SELECT Type FROM DotsSpent
WHERE DotType = 'Creation' AND Type in ('Physical', 'Social', 'Mental')
ORDER BY Dots DESC;


CREATE VIEW Abilities AS
SELECT Name, TraitCategories.Type as Type, COUNT(Dots.Type) as Dots
FROM TraitCategories
LEFT OUTER JOIN Dots ON Dots.Trait = TraitCategories.Name
WHERE TraitCategories.Type in ('Talent', 'Skill', 'Knowledge')
GROUP BY Name;

CREATE VIEW Virtues AS
SELECT Name, TraitCategories.Type as Type, COUNT() as Dots
FROM TraitCategories
JOIN Dots
ON Dots.Trait = TraitCategories.Name
WHERE TraitCategories.Type = 'Virtue'
GROUP BY Dots.Trait;

CREATE VIEW Humanity AS
SELECT 'Humanity' as Name, SUM(Dots) as Dots
from virtues
where Name in ('Conscience', 'Self-Control');

-- select * from TraitCategories JOIN Dots ON Dots.Trait = TraitCategories.Name WHERE TraitCategories.Type in ('Physical', 'Social', 'Mental');

-- Dots Available
INSERT INTO CreationDots (Type, Amount) VALUES ('Attributes', 7);
INSERT INTO CreationDots (Type, Amount) VALUES ('Attributes', 5);
INSERT INTO CreationDots (Type, Amount) VALUES ('Attributes', 3);
INSERT INTO CreationDots (Type, Amount) VALUES ('Abilities', 13);
INSERT INTO CreationDots (Type, Amount) VALUES ('Abilities', 9);
INSERT INTO CreationDots (Type, Amount) VALUES ('Abilities', 5);
INSERT INTO CreationDots (Type, Amount) VALUES ('Virtues', 7);

-- Trait Categories
-- Attributes
INSERT INTO TraitCategories (Name, Type) VALUES ('Strength',  'Physical');
INSERT INTO TraitCategories (Name, Type) VALUES ('Dexterity', 'Physical');
INSERT INTO TraitCategories (Name, Type) VALUES ('Stamina',   'Physical');

INSERT INTO TraitCategories (Name, Type) VALUES ('Charisma',  'Social');
INSERT INTO TraitCategories (Name, Type) VALUES ('Manipulation',  'Social');
INSERT INTO TraitCategories (Name, Type) VALUES ('Appearance',  'Social');

INSERT INTO TraitCategories (Name, Type) VALUES ('Perception',  'Mental');
INSERT INTO TraitCategories (Name, Type) VALUES ('Intelligence',  'Mental');
INSERT INTO TraitCategories (Name, Type) VALUES ('Wits',  'Mental');

-- Abilities
INSERT INTO TraitCategories (Name, Type) VALUES ('Alertness',  'Talent');
INSERT INTO TraitCategories (Name, Type) VALUES ('Athletics',  'Talent');
INSERT INTO TraitCategories (Name, Type) VALUES ('Awareness',  'Talent');
INSERT INTO TraitCategories (Name, Type) VALUES ('Brawl',  'Talent');
INSERT INTO TraitCategories (Name, Type) VALUES ('Empathy',  'Talent');
INSERT INTO TraitCategories (Name, Type) VALUES ('Expression',  'Talent');
INSERT INTO TraitCategories (Name, Type) VALUES ('Intimidation',  'Talent');
INSERT INTO TraitCategories (Name, Type) VALUES ('Leadership',  'Talent');
INSERT INTO TraitCategories (Name, Type) VALUES ('Streetwise',  'Talent');
INSERT INTO TraitCategories (Name, Type) VALUES ('Subterfuge',  'Talent');

INSERT INTO TraitCategories (Name, Type) VALUES ('Animal Ken',  'Skill');
INSERT INTO TraitCategories (Name, Type) VALUES ('Crafts',  'Skill');
INSERT INTO TraitCategories (Name, Type) VALUES ('Drive',  'Skill');
INSERT INTO TraitCategories (Name, Type) VALUES ('Etiquette',  'Skill');
INSERT INTO TraitCategories (Name, Type) VALUES ('Firearms',  'Skill');
INSERT INTO TraitCategories (Name, Type) VALUES ('Larceny',  'Skill');
INSERT INTO TraitCategories (Name, Type) VALUES ('Melee',  'Skill');
INSERT INTO TraitCategories (Name, Type) VALUES ('Performance',  'Skill');
INSERT INTO TraitCategories (Name, Type) VALUES ('Stealth',  'Skill');
INSERT INTO TraitCategories (Name, Type) VALUES ('Survival',  'Skill');

INSERT INTO TraitCategories (Name, Type) VALUES ('Academics',  'Knowledge');
INSERT INTO TraitCategories (Name, Type) VALUES ('Computer',  'Knowledge');
INSERT INTO TraitCategories (Name, Type) VALUES ('Finance',  'Knowledge');
INSERT INTO TraitCategories (Name, Type) VALUES ('Investigation',  'Knowledge');
INSERT INTO TraitCategories (Name, Type) VALUES ('Law',  'Knowledge');
INSERT INTO TraitCategories (Name, Type) VALUES ('Medicine',  'Knowledge');
INSERT INTO TraitCategories (Name, Type) VALUES ('Occult',  'Knowledge');
INSERT INTO TraitCategories (Name, Type) VALUES ('Politics',  'Knowledge');
INSERT INTO TraitCategories (Name, Type) VALUES ('Science',  'Knowledge');
INSERT INTO TraitCategories (Name, Type) VALUES ('Technology',  'Knowledge');


INSERT INTO TraitCategories (Name, Type) VALUES ('Conscience',  'Virtue');
INSERT INTO TraitCategories (Name, Type) VALUES ('Self-Control',  'Virtue');
INSERT INTO TraitCategories (Name, Type) VALUES ('Courage',  'Virtue');

INSERT INTO TraitCategories (Name, Type) VALUES ('Willpower',  'Willpower');

INSERT INTO TraitCategories (Name, Type) VALUES ('Humanity', 'Path of Enlighment');

-- Virtues
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Conscience');
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Self-Control');
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Courage');

-- Base Values
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Strength');
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Dexterity');
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Stamina');

INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Charisma');
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Manipulation');
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Appearance');

INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Perception');
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Intelligence');
INSERT INTO Dots (Type, Trait) VALUES ('Base', 'Wits');
