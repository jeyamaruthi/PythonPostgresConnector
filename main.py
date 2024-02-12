import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="1967", port=5432)


cur = conn.cursor()

#Create a table
cur.execute(""" CREATE TABLE IF NOT EXISTS person (
id INT PRIMARY KEY,
name VARCHAR(255),
age INT,
gender CHAR
);
""")


#Insert values into table
cur.execute("""INSERT INTO person (id,name,age,gender)
values
(1,'Jey',28,'m'),
(2,'Fiaz',29,'m'),
(3,'Nilesh',32,'m'),
(4,'KumaraPriya',33,'f');
""")

cur.execute("""
select * from person where age <= 50
""")

#print(cur.fetchall())

# TO print line by line

for row in cur.fetchall():
    print(row)


conn.commit()

cur.close()

conn.close()