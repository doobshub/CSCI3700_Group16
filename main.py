from flask import Flask, render_template, jsonify
import util

app = Flask(__name__)

username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'

@app.route('/')
def index():
    return "CSCI 3700:Homework 3"

@app.route('/api/update_basket_a')
def update_basket_a():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    
    try:
        cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
        connection.commit()
        return "Success!"
    except Exception as e:
        return str(e)
    
    util.disconnect_from_db(connection, cursor)

@app.route('/api/unique')
def unique_fruits():
    cursor, connection = util.connect_to_db(username, password, host, port, database)
    
    try:
        cursor.execute("SELECT DISTINCT fruit_a FROM basket_a LEFT JOIN basket_b ON basket_a.fruit_a = basket_b.fruit_b WHERE basket_b.fruit_b IS NULL")
        fruits_a = cursor.fetchall()
        
        cursor.execute("SELECT DISTINCT fruit_b FROM basket_b LEFT JOIN basket_a ON basket_b.fruit_b = basket_a.fruit_a WHERE basket_a.fruit_a IS NULL")
        fruits_b = cursor.fetchall()

        unique_a = [fruit[0] for fruit in fruits_a]
        unique_b = [fruit[0] for fruit in fruits_b]

        return render_template('index.html', fruits_a=unique_a, fruits_b=unique_b)
    except Exception as e:
        return str(e)
        
    util.disconnect_from_db(connection, cursor)

if __name__ == '__main__':
    	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
