all:
	cd converter/; python3 mdimport.py

clean:
	rm -r vtm20/sql/CharacterTemplate.sql build vtm20/sql/04_Insert_Rules.sql || true

test:
	cd tests/; python3 test_vtm20character.py
	cd tests/; python3 test_rules.py

vtm20/sql/CharacterTemplate.sql:
	cd vtm20; python3 rules.py
	cat vtm20/sql/*.sql > vtm20/sql/CharacterTemplate.sql

sqltest: vtm20/sql/CharacterTemplate.sql
	mkdir build || true
	sqlite3 build/character.vtm -init vtm20/sql/CharacterTemplate.sql;
