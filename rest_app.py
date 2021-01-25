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
        cursor.execute("SELECT user_name FROM v4v77OlCF3.users WHERE user_id = "+str(user_id)+";")
        user = cursor.fetchone()
        if user:
            return {'Status =': 'Ok' , 'User name' : user[0]}, 200
        else:
            return {"User": "Not Found"}, 500

    elif request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        creation_date = request_data.get('creation_date')
        try:
            cursor.execute("INSERT into v4v77OlCF3.users (user_id , user_name , creation_date) VALUES ('" + user_id + "', '" + user_name + "', '" + creation_date + "' )")
            return {'status': 'ok' , 'user add': user_name}, 200
        except:
            return {"Status" : "Error" , "Reason" : "Id all ready exists"},500


    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        cursor.execute("SELECT user_name FROM v4v77OlCF3.users WHERE user_id = "+str(user_id)+";")
        user = cursor.fetchone()
        if user:
            cursor.execute("UPDATE v4v77OlCF3.users SET user_name = '"+user_name+"' WHERE user_id = '"+str(user_id)+"'")
            return {user_name : 'User name'}, 200
        # else:
        #     return {"status": "error", "reason": "id not exists"}, 500


    elif request.method == 'DELETE':
        cursor.execute("SELECT * FROM v4v77OlCF3.users WHERE user_id = " + str(user_id) + ";")
        user = cursor.fetchone()
        if user:
            cursor.execute("DELETE FROM v4v77OlCF3.users WHERE user_id = '" +str(user_id)+ "' ")
            return {'status': 'OK' ,  'User Deleted' : user_id}, 200
        else:
            return {'status': 'error' ,  'reason' : 'no such id'}, 500


@app.route ('/users/test')
def hel():
    return "<H1 id='user'>" ' Ok we r good to go '"</H1>", 200



app.run(host='127.0.0.1', debug=True, port=5000)

cursor.close()
conn.close()