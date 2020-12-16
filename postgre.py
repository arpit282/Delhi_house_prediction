import psycopg2

conn = psycopg2.connect(database="SQL", user = "postgres", password = "DATAscience282", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")


cur = conn.cursor()
cur.execute("SELECT * from customer")
rows = cur.fetchall()
for row in rows:
   print ("customer = ", row[0]);
   print ("first name = ", row[1]);
   print ("last name = ", row[2]);
   print ("age = ", row[3])
   print ("email = ", row[4])
print( "Operation done successfully");
conn.close()