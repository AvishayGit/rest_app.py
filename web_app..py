from flask import Flask, request
import pymysql

import time
conn = pymysql.connect(host='remotemysql.com', port=3306, user='v4v77OlCF3', passwd='5EmH5HUA29', db='v4v77OlCF3')
conn.autocommit(True)
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/users/get_user_data/<user_id>' , methods=['GET'])

def get_user_data(user_id):
    cursor.execute("SELECT user_name FROM v4v77OlCF3.users WHERE user_id = " + str(user_id) + ";")
    user = cursor.fetchone()
    if user:
        return "<H1 id='user'>" + user[0] + "</H1>", 200
    else:
        return "<H1 id='eror'>" "no such user "  + user_id + "</H1>", 500


app.run(host='127.0.0.1', debug=True, port=5001)
