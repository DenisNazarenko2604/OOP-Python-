import sqlite3

#Привязка курсора ввода к файлу 
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()

# print(connection)
# print(cur)
# connection.close()
#-------------------------------------------------------
#Создание таблицы
connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()

# cur.execute("CREATE TABLE first_table (name TEXT)")

# cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3")
# cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=2")
# cur.execute("DELETE FROM first_table WHERE rowid=1")
# cur.execute("DROP TABLE first_table")
connection.commit()

res = cur.fetchall()
print(res)
connection.close()
#--------------------------------------------------------
# cur.execute("CREATE TABLE first_table (name TEXT)") - данную строку нужно обробатывать только ОДИН РАЗ. Тоесть после запуска кода ее нужно закоментировать
# cur.execute("INSERT INTO first_table (name) VALUES ('Nick');") - этот тоже жалательно после запуска закоментировать
# cur.execute("DROP TABLE first_table") - очень СТРЕМНАЯ команда. Она удаляет таблицу без возможного воостанавления
#--------------------------------------------------------