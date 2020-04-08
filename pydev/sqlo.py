import sqlite3 as sq

def db_create():
    dx=sq.connect("d:/test.db")
    cu=dx.cursor()
    cu.execute('create table html_rec(id integer primary key,html_address varchar(255) primary key,html_des varchar(255))')
    cursor.commit()
    cursor.close()
    cu.commit()

def data_insert():
    dx=sq.connect("d:/test.db")
    cu=dx.cursor()
    cu.execute('create table html_rec(id integer primary key,html_address varchar(255) UNIQUE,html_des varchar(255))')
    cursor.commit()
    cursor.close()
    cu.commit()
    
db_create()
