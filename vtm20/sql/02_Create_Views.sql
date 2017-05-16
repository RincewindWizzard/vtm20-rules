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
