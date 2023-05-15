import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="")

mycursor = mydb.cursor()

mycursor.execute("show databases")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print("----------------------------------")

mycursor.execute("SELECT * FROM music_shop.items")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print("----------------------------------")

sql = "INSERT INTO music_shop.items (name, cost, types_id, number_of_items) VALUES (%s, %s, %s, %s)"
val = ("Some instrument", "1900", "1", "3")
mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("SELECT * FROM music_shop.items")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print("----------------------------------")

sql = "DELETE FROM music_shop.items WHERE name = 'Some instrument'"

mycursor.execute(sql)

mydb.commit()

mycursor.execute("SELECT * FROM music_shop.items")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
