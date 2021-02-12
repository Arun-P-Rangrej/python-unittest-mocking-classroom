import mysql.connector as sql

class DbHelper:
    def get_maximum_salary(self):
        mycursor.execute("SELECT MAX(salary) FROM employee")
        myresult = mycursor.fetchall()
        return myresult

    def get_minimum_salary(self):
        mycursor.execute("SELECT MIN(salary) FROM employee")
        myresult = mycursor.fetchall()
        return myresult

if __name__ == "__main__":
    db = sql.connect(
    host = "localhost",
    user = "arun",
    passwd = "root",
    database = "datagrokr"
    )
    mycursor = db.cursor()
    # cursor.execute("CREATE DATABASE datagrokr")
    # cursor.execute("CREATE TABLE employee( name VARCHAR(255), salary INTEGER(6))")
    # myquery="INSERT INTO salary(name,salary) VALUES (%s,%s)"
    # values=[ ("Arun P Rangrej",60000),("Padma K",40000),("Dinakar",34000),("Primith",4000)]
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
