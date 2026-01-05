from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# ---------------- DATABASE CONFIG ----------------
DATABASE_URL = os.environ.get("DATABASE_URL")

# Fix Render postgres URL
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---------------- MODEL ----------------
class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# 🔥 CREATE TABLES ON STARTUP
with app.app_context():
    db.create_all()

# ---------------- ROUTES ----------------
@app.route("/", methods=["GET"])
def home():
    return "Contact API Running on Render 🚀"

@app.route("/contact", methods=["POST"])
def contact():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        if not all([name, email, subject, message]):
            return jsonify({"status": "error", "message": "All fields required"}), 400

        new_contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        db.session.add(new_contact)
        db.session.commit()

        return jsonify({
            "status": "success",
            "message": "Message saved successfully"
        }), 201

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
