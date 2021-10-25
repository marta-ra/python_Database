# creation of the University database and implementation of methods for adding new data to the database

import sqlite3 as sql

class DBWorker:
    def __init__(self, db_name):
        self.cur_db = sql.connect(db_name)
        self.cursor = None
        self.result = None
    def connect_db(self):
        self.cursor = self.cur_db.cursor()
    def use_query(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.cur_db.commit()
    def return_result(self):
        return self.result
    def new_student(self, Name,Last_Name,University,Faculty, Speciality):
        self.use_query(f"INSERT INTO Student (Name,Last_Name,University,Faculty, Speciality) VALUES ('{Name}', '{Last_Name}', '{University}', '{Faculty}', '{Speciality}')")
    def new_speciality(self, Speciality_name,Faculty,Term_of_study):
        self.use_query(f"INSERT INTO Speciality (Speciality_name,Faculty,Term_of_study) VALUES ('{Speciality_name}', '{Faculty}', {Term_of_study})")
    def new_faculty(self, Faculty_name,Dean,University):
        self.use_query(f"INSERT INTO Faculty (Faculty_name,Dean,University) VALUES ('{Faculty_name}', '{Dean}', '{University}')")
    def new_university(self, University_name,Address,Number_of_students):
        self.use_query(f"INSERT INTO University (University_name,Address,Number_of_students) VALUES ('{University_name}', '{Address}', {Number_of_students})")
    def new_сlasses(self, Сlass_name,Number_of_hours,Lecturer, Speciality):
        self.use_query(f"INSERT INTO Сlasses (Сlass_name,Number_of_hours,Lecturer, Speciality) VALUES ('{Сlass_name}', {Number_of_hours}, '{Lecturer}', '{Speciality}')")
    def show_student_speciality(self, speciality):
        self.use_query(f"SELECT id, Name, Last_Name FROM Student WHERE Speciality is '{speciality}'")
        result = []
        for row in db.result:
            result.append(row)
        return result

class DB_create:
    def create_db_university(self):
        db = DBWorker('University_DB.db')
        db.connect_db()
        db.use_query(
            'CREATE TABLE University (id integer PRIMARY KEY AUTOINCREMENT, University_name varchar(255), Address varchar(255), Number_of_students int)')
        db.use_query(
            'CREATE TABLE Faculty (id integer PRIMARY KEY AUTOINCREMENT, Faculty_name varchar(255), Dean varchar(255), University varchar(255), FOREIGN KEY (University) references University(University_name))')
        db.use_query(
            'CREATE TABLE Speciality (id integer PRIMARY KEY AUTOINCREMENT, Speciality_name varchar(255), Faculty varchar(255), Term_of_study int, FOREIGN KEY (Faculty) references Faculty(Faculty_name))')
        db.use_query(
            'CREATE TABLE Сlasses (id integer PRIMARY KEY AUTOINCREMENT, Сlass_name varchar(255), Number_of_hours int, Lecturer varchar(255), Speciality varchar(255), FOREIGN KEY (Speciality) references Speciality(Speciality_name))')
        db.use_query(
            'CREATE TABLE Student (id integer PRIMARY KEY AUTOINCREMENT, Name varchar(255), Last_Name varchar(255), University  varchar(255), Faculty varchar(255), Speciality varchar(255), '
            'FOREIGN KEY (Speciality) references Speciality(Speciality_name), FOREIGN KEY (Faculty) references Faculty(Faculty_name), FOREIGN KEY (University) references University(University_name))')

# # Create the University database with all tables and relationships (uncomment to create a database):
# create_db = DB_create()
# create_db.create_db_university()

db = DBWorker('University_DB.db')
db.connect_db()
# Add new data:
db.new_student('Александр', 'Дудин', 'БГУ', 'Экономический', 'Экономист-аналитик')
db.new_university('БГУ', 'Минск', 2000)
db.new_faculty('Экономический', 'Зверева Виктория Сергеевна', 'БГУ')
db.new_speciality('Экономист-аналитик', 'БГУ', 4)
db.new_сlasses('Социологическая аналитика', 140, 'Гончаров Василий Петрович', 'Экономист-аналитик')
# output of students in the specialty:
print(db.show_student_speciality('Программист'))