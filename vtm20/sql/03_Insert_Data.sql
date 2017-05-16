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
