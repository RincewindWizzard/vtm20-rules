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


