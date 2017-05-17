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




