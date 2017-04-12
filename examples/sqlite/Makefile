all:
	rm test.db; (cat CharacterCreation.sql; cat ExampleChar_HarryLuchting.sql; ) > example.sql; sqlite3 -init example.sql test.db
