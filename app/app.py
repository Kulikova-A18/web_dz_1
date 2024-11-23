from flask import Flask, request, make_response
from datetime import datetime
import os

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
