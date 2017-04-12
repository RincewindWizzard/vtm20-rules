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
