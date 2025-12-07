import sqlite3

connection = sqlite3.connect("AnimalKingdom.cl3", 5)
cur = connection.cursor()

# cur.execute("CREATE TABLE animals (name TEXT, type TEXT)") 

# cur.execute("INSERT INTO animals (name, type) VALUES ('Лев', 'Ссавець');")
# cur.execute("INSERT INTO animals (name, type) VALUES ('Крокодил', 'Плазун');")
# cur.execute("INSERT INTO animals (name, type) VALUES ('Орел', 'Птах');")
# cur.execute("INSERT INTO animals (name, type) VALUES ('Морська черепаха', 'Плазун');")
# cur.execute("INSERT INTO animals (name, type) VALUES ('Мавпа', 'Ссавець');")

# cur.execute("UPDATE animals SET name='Сокіл' WHERE name='Орел'")

# cur.execute("SELECT * FROM animals WHERE type ='Ссавець")
mammals = cur.fetchall()

# cur.execute("SELECT * FROM animals")
all_animals = cur.fetchall()
connection.commit()

print(f"Ссавці:\n {mammals}")
print(f"Усі тварини:\n {all_animals}")
connection.close()