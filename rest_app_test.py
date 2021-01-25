from flask import Flask, request
import pymysql
import datetime
now = datetime.datetime.now()
today = now.strftime("%m/%d/%y %X")

conn = pymysql.connect(host='remotemysql.com', port=3306, user='v4v77OlCF3', passwd='5EmH5HUA29', db='v4v77OlCF3')
conn.autocommit(True)
cursor = conn.cursor()

app = Flask(__name__)

# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        cursor.execute("SELECT user_name FROM v4v77OlCF3.users;")
        for row in cursor:
            if row ['user_id'] == user_id:
                return {'HII ': row['user_name']}, 200  # status code
            else:
                return {"noo" : row['user_name']} , 500

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_id2 = request_data.get('user_id')
        user_name2 = request_data.get('user_name')
        creation_date = request_data.get('creation_date')
        cursor.execute("INSERT into v4v77OlCF3.users (user_id , user_name , creation_date) VALUES ('"+user_id2+"', '"+user_name2+"', '" + creation_date + "' )")
        try:
            return {'status': 'ok' , 'user add':user_name2}, 200
        except:
            return {"status" : "error" , "reason" : "id all ready exists"},500
        # finally:
        #     return {"status" : "error" , "reason" : "id all ready exists"}, 500


# todo elif for put and delete
@app.route ('/users/test')
def hel():
    return 'status ok' , 200



app.run(host='127.0.0.1', debug=True, port=5000)

cursor.close()
conn.close()