from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database connection
def db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='yourusername',
        password='yourpassword',
        database='telemedicine'
    )
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User  registered successfully!"})

@app.route('/login', methods=['POST'])
def login():
    username = request.form['loginUsername']
    password = request.form['loginPassword']
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/submit_symptoms', methods=['POST'])
def submit_symptoms():
    symptom_description = request.form['symptomDescription']
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO symptoms (description) VALUES (%s)", (symptom_description,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Symptoms submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)