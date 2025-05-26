from flask import Flask, request, jsonify, render_template, session ,redirect, url_for , flash
import openai
import os
import dotenv 
import json
import difflib
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta


app = Flask(__name__)

# Load predefined static responses
with open("responses.json", "r") as f:
    static_responses = json.load(f)

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

#setup database connection 
#initialize mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'anas'
app.config['MYSQL_PASSWORD'] = 'neotech@223'
app.config['MYSQL_DB'] = 'neotech_db'

# setup session time
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(minutes=20)

# Initialize MySQL connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB']
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_message = data.get("message", "").strip().lower()

    try:
        # Try OpenAI first
        response =  openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for NeoTech Institute."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})

    except Exception as e:
        print(f"⚠️ OpenAI API failed: {e}")

        # Use difflib to find best match from static_responses
        possible_keys = list(static_responses.keys())
        best_match = difflib.get_close_matches(user_message, possible_keys, n=1, cutoff=0.5)

        if best_match:
            reply = static_responses[best_match[0]]
        else:
            reply = static_responses.get("default", "Sorry, I didn't understand that.")

        return jsonify({"response": reply})

# Route for handling user registration
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    contact = data.get("contact")

    if not name or not contact:
        return jsonify({"success": False, "message" : "Full name and Email/Phone number are required."}), 400
    
    conn = get_db_connection()
    if conn is None:
        return jsonify({"success": False, "message" : "Database connection failed."}), 500
    
    cursor = conn.cursor()

    try:
        # Check if the user already exists
        cursor.execute("SELECT student_pk_id FROM students WHERE email = %s", (contact,))
        existing_user = cursor.fetchone()
        if existing_user:
            return jsonify({"success": False , "message": "User already exists with this contact."}), 409
        # this is for web registration for general enquiry

        print(f"Registering user for general enquiry: Name={name},Contact={contact}")
        return jsonify({"success": True, "message": "Thank you for your interest we'll contact you soon!."})
    except mysql.connector.Error as err:
        print(f"❌ Database error during general registration: {err}")
        return jsonify({"success": False, "message": "Failed to process registration due to a server error."}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)


