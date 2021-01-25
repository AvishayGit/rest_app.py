import pymysql
import datetime

now = datetime.datetime.now()
today = now.strftime("%m/%d/%y %X")




conn = pymysql.connect(host='remotemysql.com', port=3306, user='v4v77OlCF3', passwd='5EmH5HUA29', db='v4v77OlCF3')
conn.autocommit(True)
cursor = conn.cursor()

cursor.execute("SELECT * FROM v4v77OlCF3.users;")
# cursor.execute("INSERT into v4v77OlCF3.users (user_id , user_name , creation_date) VALUES (1, 'john', '"+str(today)+"' )")
# cursor.execute("INSERT into v4v77OlCF3.users (user_id , user_name , creation_date) VALUES (2, 'Yoni', '"+str(today)+"' )")

print(("INSERT into v4v77OlCF3.users (user_id, user_name , creation_date) VALUES (15,‘Dalia','"+str(today)+"')"))


cursor.close()
conn.close()