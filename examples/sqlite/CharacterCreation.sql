-- This Table contains a list of all Dots (Base, Freebie, XP) spent.
-- Beware that Dots != Freebie/XP spent!
CREATE TABLE Dots (
  Type TEXT,
  Trait TEXT,
  time t TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  CHECK(Type IN ('Creation', 'Base', 'Freebie', 'XP')) NOT NULL
);

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
    'Path of Enlighment'
  )) NOT NULL
);


CREATE VIEW Attributes AS 
SELECT Name, TraitCategories.Type as Type, COUNT() as Dots
FROM TraitCategories 
JOIN Dots 
ON Dots.Trait = TraitCategories.Name 
WHERE TraitCategories.Type in ('Physical', 'Social', 'Mental') GROUP BY Dots.Trait;

-- Order of Primary, secondary, tertiary Attributes
CREATE VIEW AttributeOrder AS
SELECT Category 
FROM AttributeSpent 
ORDER BY Dots DESC;

-- How Many Dots are Spent in the Categories?
CREATE VIEW AttributeSpent AS
SELECT 'Base' as Type, TraitCategories.Type as Category, COUNT() as Dots 
FROM TraitCategories 
LEFT OUTER JOIN Dots 
ON Dots.Trait = TraitCategories.Name 
WHERE TraitCategories.Type in ('Physical', 'Social', 'Mental') 
AND Dots.Type = 'Base' 
GROUP BY TraitCategories.Type;

CREATE VIEW Abilities AS 
SELECT Name, TraitCategories.Type as Type, COUNT() as Dots
FROM TraitCategories 
JOIN Dots 
ON Dots.Trait = TraitCategories.Name 
WHERE TraitCategories.Type in ('Talent', 'Skill', 'Knowledge')
GROUP BY Dots.Trait;



-- select * from TraitCategories JOIN Dots ON Dots.Trait = TraitCategories.Name WHERE TraitCategories.Type in ('Physical', 'Social', 'Mental');

-- Creation Values
INSERT INTO Dots (Type, Trait) VALUES ('Creation', 'Strength');
INSERT INTO Dots (Type, Trait) VALUES ('Creation', 'Dexterity');
INSERT INTO Dots (Type, Trait) VALUES ('Creation', 'Stamina');

INSERT INTO Dots (Type, Trait) VALUES ('Creation', 'Charisma');
INSERT INTO Dots (Type, Trait) VALUES ('Creation', 'Manipulation');
INSERT INTO Dots (Type, Trait) VALUES ('Creation', 'Appearance');

INSERT INTO Dots (Type, Trait) VALUES ('Creation', 'Perception');
INSERT INTO Dots (Type, Trait) VALUES ('Creation', 'Intelligence');
INSERT INTO Dots (Type, Trait) VALUES ('Creation', 'Wits');




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
INSERT INTO TraitCategories (Name, Type) VALUES ('Willpower',  'Virtue');

INSERT INTO TraitCategories (Name, Type) VALUES ('Humanity', 'Path of Enlighment');

