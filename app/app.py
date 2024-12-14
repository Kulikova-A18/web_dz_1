from flask import Flask, request, make_response
from datetime import datetime
import sqlite3
from faker import Faker

app = Flask(__name__)
fake = Faker()

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT UNIQUE
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/date', methods=['GET'])
def get_date():
    current_date = datetime.now().strftime('%d.%m.%Y')
    response = make_response(current_date)
    response.headers['X-Author'] = 'Kulikova Alyona'
    return response

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')
    if not name:
        return 'Missing name parameter', 400

    response = make_response(f'<h3>Hello, {name}!</h3>')
    response.set_cookie('name', name)
    response.headers['X-Author'] = 'Kulikova Alyona'
    return response

@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # SQL Injection: вставка пользовательского ввода напрямую в запрос
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    user_data = cursor.fetchall()
    conn.close()

    if user_data:
        return f'User data: {user_data}', 200
    else:
        return 'User not found', 404

@app.route('/generate_users', methods=['POST'])
def generate_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    for _ in range(100):
        username = fake.user_name()
        email = fake.email()
        
        try:
            cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
        except sqlite3.IntegrityError:
            continue

    conn.commit()
    conn.close()
    return 'Generated 100 random users', 201

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0')
