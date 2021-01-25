import pymysql
import datetime
# # Establishing a connection to DB
# conn = pymysql.connect(host='remotemysql.com', port=3306, user='v4v77OlCF3', passwd='5EmH5HUA29', db='v4v77OlCF3')
#
# # Getting a cursor from Database
# cursor = conn.cursor()
#
# # Getting all data from table “users”
# cursor.execute("SELECT * FROM v4v77OlCF3.users;")
#
# # Iterating table and printing all users
# for row in cursor:
#     print(row)
#
# cursor.close()
# conn.close()

conn = pymysql.connect(host='remotemysql.com', port=3306, user='v4v77OlCF3', passwd='5EmH5HUA29', db='v4v77OlCF3')
conn.autocommit(True)
cursor = conn.cursor()
cursor.execute("SELECT user_name FROM v4v77OlCF3.users;")
for row in cursor:
    if row['user_id']:
        print('hii there' ,row['user_name'])