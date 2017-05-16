PRAGMA foreign_keys = ON;
CREATE TABLE Traits (
  Name TEXT PRIMARY KEY,
  Type TEXT,
  FOREIGN KEY(Type) REFERENCES TraitCategories(Name)
);

CREATE TABLE TraitCategories (
  Name TEXT PRIMARY KEY
);

CREATE TABLE Archetypes (
  Name TEXT PRIMARY KEY
);


-- This Table contains a list of all Dots (Base, Freebie, XP) spent.
-- Beware that Dots != Freebie/XP spent!

CREATE TABLE Dots (
  Type TEXT NOT NULL,
  Trait TEXT NOT NULL,
  time t TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(Type) REFERENCES DotTypes(Name),
  FOREIGN KEY(Trait) REFERENCES Traits(Name)
);

CREATE TABLE DotTypes (
  Name TEXT PRIMARY KEY NOT NULL  
);

CREATE TABLE CreationDots (
  Type Text,
  Amount INTEGER
);


CREATE VIEW TraitValues AS
SELECT Name, Traits.Type as Type, COUNT(Dots.Trait) as Dots
FROM Traits
LEFT OUTER JOIN Dots ON Dots.Trait = Traits.Name
GROUP BY Name;


--Select DotTypes.Name as DotType, Traits.Name as Trait, Traits.Type as TraitType from DotTypes CROSS JOIN Traits LEFT OUTER JOIN Dots ON DotTypes.Name = Dots.Type AND Traits.Name = Dots.Trait;

CREATE VIEW DotsSpent AS
SELECT 
  DotTypes.Name as DotType, 
  Traits.Name as Trait, 
  Traits.Type as TraitType, 
  COUNT(Dots.time) as Dots
FROM DotTypes 
CROSS JOIN Traits 
LEFT OUTER JOIN Dots 
ON DotTypes.Name = Dots.Type 
AND Traits.Name = Dots.Trait 
GROUP BY DotTypes.Name, Traits.Name;

CREATE VIEW Attributes AS
SELECT *
FROM Traits
WHERE Type in ('physical', 'social', 'mental');

-- Order of Primary, secondary, tertiary Attributes
CREATE VIEW AttributeOrder AS
SELECT TraitType, SUM(Dots) as Dots
FROM DotsSpent
WHERE DotType = 'creation' 
AND TraitType in ('physical', 'social', 'mental')
GROUP BY TraitType
ORDER BY SUM(Dots) DESC;

-- Order of Primary, secondary, tertiary Attributes
CREATE VIEW AbilityOrder AS
SELECT TraitType, SUM(Dots) as Dots
FROM DotsSpent
WHERE DotType = 'creation' 
AND TraitType in ('talent', 'skill', 'knowledge')
GROUP BY TraitType
ORDER BY SUM(Dots) DESC;


CREATE VIEW Abilities AS
SELECT Name, Traits.Type as Type, COUNT(Dots.Type) as Dots
FROM Traits
LEFT OUTER JOIN Dots ON Dots.Trait = Traits.Name
WHERE Traits.Type in ('talent', 'skill', 'knowledge')
GROUP BY Name;

CREATE VIEW Virtues AS
SELECT Name, Traits.Type as Type, COUNT() as Dots
FROM Traits
JOIN Dots
ON Dots.Trait = Traits.Name
WHERE Traits.Type = 'virtue'
GROUP BY Dots.Trait;

CREATE VIEW Humanity AS
SELECT 'Humanity' as Name, SUM(Dots) as Dots
from virtues
where Name in ('Conscience', 'Self-Control');
------------------------------------------------------------------------------------------------
-- Types of Dots
INSERT INTO DotTypes VALUES ('base');
INSERT INTO DotTypes VALUES ('creation');
INSERT INTO DotTypes VALUES ('freebie');
INSERT INTO DotTypes VALUES ('xp');
------------------------------------------------------------------------------------------------

INSERT INTO TraitCategories (Name) VALUES ('physical');
INSERT INTO TraitCategories (Name) VALUES ('social');
INSERT INTO TraitCategories (Name) VALUES ('mental');
INSERT INTO TraitCategories (Name) VALUES ('talent');
INSERT INTO TraitCategories (Name) VALUES ('skill');
INSERT INTO TraitCategories (Name) VALUES ('knowledge');
INSERT INTO TraitCategories (Name) VALUES ('discipline');
INSERT INTO TraitCategories (Name) VALUES ('background');
INSERT INTO TraitCategories (Name) VALUES ('virtue');
INSERT INTO TraitCategories (Name) VALUES ('willpower');
INSERT INTO TraitCategories (Name) VALUES ('path of enlighment');

-- Dots Available
INSERT INTO CreationDots (Type, Amount) VALUES ('Attributes', 7);
INSERT INTO CreationDots (Type, Amount) VALUES ('Attributes', 5);
INSERT INTO CreationDots (Type, Amount) VALUES ('Attributes', 3);
INSERT INTO CreationDots (Type, Amount) VALUES ('Abilities', 13);
INSERT INTO CreationDots (Type, Amount) VALUES ('Abilities', 9);
INSERT INTO CreationDots (Type, Amount) VALUES ('Abilities', 5);
INSERT INTO CreationDots (Type, Amount) VALUES ('Virtues', 7);
INSERT INTO Traits (Name, Type) VALUES ('Melee', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Drive', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Stealth', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Animal Ken', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Etiquette', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Crafts', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Larceny', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Archery', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Riding', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Performance', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Firearms', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Survival', 'skill');
INSERT INTO Traits (Name, Type) VALUES ('Intimidation', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Instruction', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Awareness', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Expression', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Athletics', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Streetwise', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Alertness', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Leadership', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Empathy', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Subterfuge', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Brawl', 'talent');
INSERT INTO Traits (Name, Type) VALUES ('Occult', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Computer', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Seneshal', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Technology', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Law', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Investigation', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Academics', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Medicine', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Politics', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Finance', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Science', 'knowledge');
INSERT INTO Traits (Name, Type) VALUES ('Intelligence', 'mental');
INSERT INTO Traits (Name, Type) VALUES ('Wits', 'mental');
INSERT INTO Traits (Name, Type) VALUES ('Perception', 'mental');
INSERT INTO Traits (Name, Type) VALUES ('Manipulation', 'social');
INSERT INTO Traits (Name, Type) VALUES ('Charisma', 'social');
INSERT INTO Traits (Name, Type) VALUES ('Appearance', 'social');
INSERT INTO Traits (Name, Type) VALUES ('Dexterity', 'physical');
INSERT INTO Traits (Name, Type) VALUES ('Stamina', 'physical');
INSERT INTO Traits (Name, Type) VALUES ('Strength', 'physical');
INSERT INTO Traits (Name, Type) VALUES ('Conviction', 'virtue');
INSERT INTO Traits (Name, Type) VALUES ('Instinct', 'virtue');
INSERT INTO Traits (Name, Type) VALUES ('Willpower', 'virtue');
INSERT INTO Traits (Name, Type) VALUES ('Conscience', 'virtue');
INSERT INTO Traits (Name, Type) VALUES ('Courage', 'virtue');
INSERT INTO Traits (Name, Type) VALUES ('Self-Control', 'virtue');
INSERT INTO Archetypes ('Name') VALUES ('Cavalier');
INSERT INTO Archetypes ('Name') VALUES ('Capitalist');
INSERT INTO Archetypes ('Name') VALUES ('Deviant');
INSERT INTO Archetypes ('Name') VALUES ('Judge');
INSERT INTO Archetypes ('Name') VALUES ('Pedagogue');
INSERT INTO Archetypes ('Name') VALUES ('Curmudgeon');
INSERT INTO Archetypes ('Name') VALUES ('Penitent');
INSERT INTO Archetypes ('Name') VALUES ('Celebrant');
INSERT INTO Archetypes ('Name') VALUES ('Director');
INSERT INTO Archetypes ('Name') VALUES ('Eye of the Storm');
INSERT INTO Archetypes ('Name') VALUES ('Creep Show');
INSERT INTO Archetypes ('Name') VALUES ('Traditionalist');
INSERT INTO Archetypes ('Name') VALUES ('Fanatic');
INSERT INTO Archetypes ('Name') VALUES ('Conniver');
INSERT INTO Archetypes ('Name') VALUES ('Loner');
INSERT INTO Archetypes ('Name') VALUES ('Monster');
INSERT INTO Archetypes ('Name') VALUES ('Rebel');
INSERT INTO Archetypes ('Name') VALUES ('Architect');
INSERT INTO Archetypes ('Name') VALUES ('Sadist');
INSERT INTO Archetypes ('Name') VALUES ('Autocrat');
INSERT INTO Archetypes ('Name') VALUES ('Trickster');
INSERT INTO Archetypes ('Name') VALUES ('Guru');
INSERT INTO Archetypes ('Name') VALUES ('Competitor');
INSERT INTO Archetypes ('Name') VALUES ('Gallant');
INSERT INTO Archetypes ('Name') VALUES ('Child');
INSERT INTO Archetypes ('Name') VALUES ('Caregiver');
INSERT INTO Archetypes ('Name') VALUES ('Masochist');
INSERT INTO Archetypes ('Name') VALUES ('Rogue');
INSERT INTO Archetypes ('Name') VALUES ('Thrill-Seeker');
INSERT INTO Archetypes ('Name') VALUES ('Perfectionist');
INSERT INTO Archetypes ('Name') VALUES ('Idealist');
INSERT INTO Archetypes ('Name') VALUES ('Bravo');
INSERT INTO Archetypes ('Name') VALUES ('Soldier');
INSERT INTO Archetypes ('Name') VALUES ('Chameleon');
INSERT INTO Archetypes ('Name') VALUES ('Conformist');
INSERT INTO Archetypes ('Name') VALUES ('Bon Vivant');
INSERT INTO Archetypes ('Name') VALUES ('Martyr');
INSERT INTO Archetypes ('Name') VALUES ('Sociopath');
INSERT INTO Archetypes ('Name') VALUES ('Survivor');
INSERT INTO Archetypes ('Name') VALUES ('Scientist');
INSERT INTO Archetypes ('Name') VALUES ('Dabbler');
INSERT INTO Archetypes ('Name') VALUES ('Enigma');
INSERT INTO Archetypes ('Name') VALUES ('Visionary');
-- Virtues
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Conscience');
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Self-Control');
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Courage');

-- Base Values
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Strength');
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Dexterity');
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Stamina');

INSERT INTO Dots (Type, Trait) VALUES ('base', 'Charisma');
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Manipulation');
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Appearance');

INSERT INTO Dots (Type, Trait) VALUES ('base', 'Perception');
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Intelligence');
INSERT INTO Dots (Type, Trait) VALUES ('base', 'Wits');
