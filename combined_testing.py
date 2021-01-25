import time
from datetime import datetime

from selenium import webdriver
import pymysql
now = datetime.now()
today = now.strftime("%m/%d/%y %X")

def Insert_post():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='v4v77OlCF3', passwd='5EmH5HUA29', db='v4v77OlCF3')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("INSERT into v4v77OlCF3.users (user_id , user_name , creation_date) VALUES (6, 'Jnifir', '" + str(today) + "' )")
    cursor.close()
    conn.close()

def Select_db():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='v4v77OlCF3', passwd='5EmH5HUA29', db='v4v77OlCF3')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM v4v77OlCF3.users;")
    for row in cursor:
        if row:
            print(row)
    cursor.close()
    conn.close()

# Insert_post()
# time.sleep(3)
Select_db()
