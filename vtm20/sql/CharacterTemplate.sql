PRAGMA foreign_keys = ON;

-- This section describes rules not specific to the character, 
-- which are later enforced by the table schemata using foreign key constrains.
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

CREATE TABLE Clans (
  Name TEXT PRIMARY KEY
);

CREATE TABLE ClanDisciplines (
  Clan TEXT,
  Discipline TEXT,
  FOREIGN KEY(Clan) REFERENCES Clans(Name),
  FOREIGN KEY(Discipline) REFERENCES Traits(Name)
);


CREATE TABLE DotTypes (
  Name TEXT PRIMARY KEY NOT NULL  
);

CREATE TABLE CreationDots (
  Type Text,
  Amount INTEGER
);

-- The Following Tables contain the data specific to your character

-- This Table contains a list of all Dots (Base, Freebie, XP) spent.
-- Beware that Dots != Freebie/XP spent!
CREATE TABLE Dots (
  Type TEXT NOT NULL,
  Trait TEXT NOT NULL,
  time t TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(Type) REFERENCES DotTypes(Name),
  FOREIGN KEY(Trait) REFERENCES Traits(Name)
);



CREATE TABLE Vampire (
  Name TEXT DEFAULT '',
  Player TEXT DEFAULT '',
  Chronicle TEXT DEFAULT '',
  Clan TEXT DEFAULT 'Ventrue',
  Sire TEXT DEFAULT '',
  Nature TEXT DEFAULT 'Architect',
  Demeanor TEXT DEFAULT 'Architect',
  Concept TEXT DEFAULT 'Architect',
  id INTEGER PRIMARY KEY DEFAULT 0,
  FOREIGN KEY(Clan) REFERENCES Clans(Name),
  FOREIGN KEY(Nature) REFERENCES Archetypes(Name),
  FOREIGN KEY(Demeanor) REFERENCES Archetypes(Name),
  FOREIGN KEY(Concept) REFERENCES Archetypes(Name),
  CHECK (id = 0) -- Enforces single row-table
);




CREATE VIEW Disciplines AS SELECT Name FROM Traits WHERE type = 'discipline';


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
INSERT INTO Traits ('Name', 'Type') VALUES ('Koldunic Sorcery', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Daimoinon', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Celerity', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Animalism', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Mytherceria', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Vicissitude', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Protean', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Obeah', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Temporis', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Dementation', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Visceratika', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Chimerstry', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Auspex', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Fortitude', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Quietus', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Thaumaturgy', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Countermagic', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Obfuscate', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Flight', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Obtenebration', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Sanguinus', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Necromancy', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Valeren', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Presence', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Ogham', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Dominate', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Potence', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Bardo', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Assamite Sorcery', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Spiritus', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Thanatosis', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Melpominee', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Serpentis', 'discipline');
INSERT INTO Traits ('Name', 'Type') VALUES ('Resources', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Contacts', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Fame', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Generation', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Retainers', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Allies', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Rituals', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Domain', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Status', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Alternate Identity', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Herd', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Mentor', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Influence', 'background');
INSERT INTO Traits ('Name', 'Type') VALUES ('Black Hand Membership', 'background');
INSERT INTO Clans ('Name') VALUES ('Telyavelic Tremere');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Telyavelic Tremere', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Telyavelic Tremere', 'Presence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Telyavelic Tremere', 'Thaumaturgy');
INSERT INTO Clans ('Name') VALUES ('Lhiannan');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lhiannan', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lhiannan', 'Ogham');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lhiannan', 'Presence');
INSERT INTO Clans ('Name') VALUES ('Toreador');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Toreador', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Toreador', 'Celerity');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Toreador', 'Presence');
INSERT INTO Clans ('Name') VALUES ('Brujah Antitribu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Brujah Antitribu', 'Celerity');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Brujah Antitribu', 'Potence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Brujah Antitribu', 'Presence');
INSERT INTO Clans ('Name') VALUES ('City Gangrel');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('City Gangrel', 'Celerity');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('City Gangrel', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('City Gangrel', 'Protean');
INSERT INTO Clans ('Name') VALUES ('Panders');
INSERT INTO Clans ('Name') VALUES ('Lasombra Antitribu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lasombra Antitribu', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lasombra Antitribu', 'Obtenebration');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lasombra Antitribu', 'Potence');
INSERT INTO Clans ('Name') VALUES ('Kiasyd');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Kiasyd', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Kiasyd', 'Mytherceria');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Kiasyd', 'Obtenebration');
INSERT INTO Clans ('Name') VALUES ('Harbingers of Skulls');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Harbingers of Skulls', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Harbingers of Skulls', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Harbingers of Skulls', 'Necromancy');
INSERT INTO Clans ('Name') VALUES ('Angellis Ater (Potence)');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Angellis Ater (Potence)', 'Daimoinon');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Angellis Ater (Potence)', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Angellis Ater (Potence)', 'Potence');
INSERT INTO Clans ('Name') VALUES ('Ahrimanes');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ahrimanes', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ahrimanes', 'Presence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ahrimanes', 'Spiritus');
INSERT INTO Clans ('Name') VALUES ('Giovanni');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Giovanni', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Giovanni', 'Necromancy');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Giovanni', 'Potence');
INSERT INTO Clans ('Name') VALUES ('Daitya');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Daitya', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Daitya', 'Presence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Daitya', 'Serpentis');
INSERT INTO Clans ('Name') VALUES ('Gargoyles');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Gargoyles', 'Flight');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Gargoyles', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Gargoyles', 'Potence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Gargoyles', 'Visceratika');
INSERT INTO Clans ('Name') VALUES ('Warrior Setites');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Warrior Setites', 'Potence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Warrior Setites', 'Presence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Warrior Setites', 'Serpentis');
INSERT INTO Clans ('Name') VALUES ('Tremere Antitribu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tremere Antitribu', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tremere Antitribu', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tremere Antitribu', 'Thaumaturgy');
INSERT INTO Clans ('Name') VALUES ('Lasombra');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lasombra', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lasombra', 'Obtenebration');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lasombra', 'Potence');
INSERT INTO Clans ('Name') VALUES ('Caitiff');
INSERT INTO Clans ('Name') VALUES ('Angellis Ater (Presence)');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Angellis Ater (Presence)', 'Daimoinon');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Angellis Ater (Presence)', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Angellis Ater (Presence)', 'Presence');
INSERT INTO Clans ('Name') VALUES ('Cappadocians');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Cappadocians', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Cappadocians', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Cappadocians', 'Necromancy');
INSERT INTO Clans ('Name') VALUES ('Ravnos');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ravnos', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ravnos', 'Chimerstry');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ravnos', 'Fortitude');
INSERT INTO Clans ('Name') VALUES ('Assamite Sorcerers');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite Sorcerers', 'Assamite Sorcery');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite Sorcerers', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite Sorcerers', 'Quietus');
INSERT INTO Clans ('Name') VALUES ('Ventrue Antitribu (Auspex)');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ventrue Antitribu (Auspex)', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ventrue Antitribu (Auspex)', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ventrue Antitribu (Auspex)', 'Fortitude');
INSERT INTO Clans ('Name') VALUES ('Daughters of Cacophony');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Daughters of Cacophony', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Daughters of Cacophony', 'Melpominee');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Daughters of Cacophony', 'Presence');
INSERT INTO Clans ('Name') VALUES ('Salubri');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Salubri', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Salubri', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Salubri', 'Obeah');
INSERT INTO Clans ('Name') VALUES ('Ravnos Antitribu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ravnos Antitribu', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ravnos Antitribu', 'Chimerstry');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ravnos Antitribu', 'Fortitude');
INSERT INTO Clans ('Name') VALUES ('Malkavian Antitribu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Malkavian Antitribu', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Malkavian Antitribu', 'Dementation');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Malkavian Antitribu', 'Obfuscate');
INSERT INTO Clans ('Name') VALUES ('Brahman');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Brahman', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Brahman', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Brahman', 'Chimerstry');
INSERT INTO Clans ('Name') VALUES ('Wu Zao (Obeah)');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Wu Zao (Obeah)', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Wu Zao (Obeah)', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Wu Zao (Obeah)', 'Obeah');
INSERT INTO Clans ('Name') VALUES ('Ventrue');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ventrue', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ventrue', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ventrue', 'Presence');
INSERT INTO Clans ('Name') VALUES ('Tremere');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tremere', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tremere', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tremere', 'Thaumaturgy');
INSERT INTO Clans ('Name') VALUES ('Malkavian');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Malkavian', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Malkavian', 'Dementation');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Malkavian', 'Obfuscate');
INSERT INTO Clans ('Name') VALUES ('Assamite Antitribu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite Antitribu', 'Celerity');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite Antitribu', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite Antitribu', 'Quietus');
INSERT INTO Clans ('Name') VALUES ('Assamite Viziers');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite Viziers', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite Viziers', 'Celerity');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite Viziers', 'Quietus');
INSERT INTO Clans ('Name') VALUES ('Noiad');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Noiad', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Noiad', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Noiad', 'Protean');
INSERT INTO Clans ('Name') VALUES ('Children of Osiris');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Children of Osiris', 'Bardo');
INSERT INTO Clans ('Name') VALUES ('Assamite');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite', 'Celerity');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Assamite', 'Quietus');
INSERT INTO Clans ('Name') VALUES ('Blood Brothers');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Blood Brothers', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Blood Brothers', 'Potence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Blood Brothers', 'Sanguinus');
INSERT INTO Clans ('Name') VALUES ('Toreador Antitribu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Toreador Antitribu', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Toreador Antitribu', 'Celerity');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Toreador Antitribu', 'Presence');
INSERT INTO Clans ('Name') VALUES ('Wu Zao (Valeren)');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Wu Zao (Valeren)', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Wu Zao (Valeren)', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Wu Zao (Valeren)', 'Valeren');
INSERT INTO Clans ('Name') VALUES ('Followers of Set');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Followers of Set', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Followers of Set', 'Presence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Followers of Set', 'Serpentis');
INSERT INTO Clans ('Name') VALUES ('Gangrel');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Gangrel', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Gangrel', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Gangrel', 'Protean');
INSERT INTO Clans ('Name') VALUES ('Anda');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Anda', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Anda', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Anda', 'Protean');
INSERT INTO Clans ('Name') VALUES ('Mariners');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Mariners', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Mariners', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Mariners', 'Protean');
INSERT INTO Clans ('Name') VALUES ('Country Gangrel');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Country Gangrel', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Country Gangrel', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Country Gangrel', 'Protean');
INSERT INTO Clans ('Name') VALUES ('Nagaraja');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Nagaraja', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Nagaraja', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Nagaraja', 'Necromancy');
INSERT INTO Clans ('Name') VALUES ('Angellis Ater (Obtenebration)');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Angellis Ater (Obtenebration)', 'Daimoinon');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Angellis Ater (Obtenebration)', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Angellis Ater (Obtenebration)', 'Obtenebration');
INSERT INTO Clans ('Name') VALUES ('Lamia');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lamia', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lamia', 'Necromancy');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Lamia', 'Potence');
INSERT INTO Clans ('Name') VALUES ('Salubri Antitribu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Salubri Antitribu', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Salubri Antitribu', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Salubri Antitribu', 'Obeah');
INSERT INTO Clans ('Name') VALUES ('Dominate Malkavians');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Dominate Malkavians', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Dominate Malkavians', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Dominate Malkavians', 'Obfuscate');
INSERT INTO Clans ('Name') VALUES ('Brujah');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Brujah', 'Celerity');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Brujah', 'Potence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Brujah', 'Presence');
INSERT INTO Clans ('Name') VALUES ('Baali');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Baali', 'Daimoinon');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Baali', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Baali', 'Presence');
INSERT INTO Clans ('Name') VALUES ('Kolduns');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Kolduns', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Kolduns', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Kolduns', 'Vicissitude');
INSERT INTO Clans ('Name') VALUES ('Old Clan Tzimisce');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Old Clan Tzimisce', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Old Clan Tzimisce', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Old Clan Tzimisce', 'Dominate');
INSERT INTO Clans ('Name') VALUES ('Tzimisce');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tzimisce', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tzimisce', 'Auspex');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tzimisce', 'Vicissitude');
INSERT INTO Clans ('Name') VALUES ('Samedi');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Samedi', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Samedi', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Samedi', 'Thanatosis');
INSERT INTO Clans ('Name') VALUES ('True Brujah');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('True Brujah', 'Potence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('True Brujah', 'Presence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('True Brujah', 'Temporis');
INSERT INTO Clans ('Name') VALUES ('Tlacique');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tlacique', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tlacique', 'Presence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Tlacique', 'Protean');
INSERT INTO Clans ('Name') VALUES ('Nosferatu Antitribu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Nosferatu Antitribu', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Nosferatu Antitribu', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Nosferatu Antitribu', 'Potence');
INSERT INTO Clans ('Name') VALUES ('Nosferatu');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Nosferatu', 'Animalism');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Nosferatu', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Nosferatu', 'Potence');
INSERT INTO Clans ('Name') VALUES ('Ventrue Antitribu (Presence)');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ventrue Antitribu (Presence)', 'Dominate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ventrue Antitribu (Presence)', 'Fortitude');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Ventrue Antitribu (Presence)', 'Presence');
INSERT INTO Clans ('Name') VALUES ('Serpents of the Light');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Serpents of the Light', 'Presence');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Serpents of the Light', 'Obfuscate');
INSERT INTO ClanDisciplines ('Clan', 'Discipline') VALUES ('Serpents of the Light', 'Serpentis');
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

INSERT INTO Vampire ('id') VALUES (0);

