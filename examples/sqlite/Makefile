all:
	cp CharacterCreation.sql /home/dfl/Programmierung/Qt/VtM20Editor/VtM20Editor/CharacterStructure.sql
	rm test.db; (cat CharacterCreation.sql; cat ExampleChar_HarryLuchting.sql >/dev/null; ) > example.sql; sqlite3 -init example.sql test.db
