import pymysql as ps

try:
    bd=ps.connect(host="172.17.0.2",
                  user="root",
                  password="batman")
    print("gained access to the bd")
    cr=bd.cursor()
    mas=['c','u','r','d']
    cr.execute("create database curd;")
    cr.execute("use curd;")
    print("create mew bd")
    cr.execute("create table table_in_curd(id INT AUTO_INCREMENT PRIMARY KEY);")
    print("create table in bd")
    for i in mas:
        cr.execute(f"ALTER TABLE table_in_curd ADD {i} varchar(255);")
    print("add new columns")
    cr.execute(f"INSERT INTO table_in_curd (c,u,r,d) VALUES ('curent','update','read','delete');")
    print("update values")
    cr.execute("select * from table_in_curd;")
    rows = cr.fetchall()
    for row in rows:
        print(f"{row}\n")
    bd.commit()
    cr.close()
    bd.close()
except Exception:
    cr.execute("DROP DATABASE curd")
    print("Error ")