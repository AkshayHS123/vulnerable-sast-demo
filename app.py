from flask import Flask, request, render_template_string
import os
import sqlite3

app = Flask(__name__)

# Insecure configuration (Debug Mode Enabled)
app.config['DEBUG'] = True

# Hardcoded secret key (Bad Practice)
app.secret_key = 'supersecretkey123'

# Vulnerable route - SQL Injection
@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    query = "SELECT * FROM users WHERE username = '%s'" % username
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return str(data)

# Vulnerable route - XSS
@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    # Unsafe rendering (XSS vulnerability)
    return render_template_string("<h1>Hello %s!</h1>" % name)

# Command Injection Example
@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    os.system('ping -c 1 ' + ip)
    return "Pinged " + ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
