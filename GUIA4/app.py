import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required


load_dotenv()


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return jsonify({"mensaje": "Servidor funcionando"})

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    user = User(
        username=data["username"],
        password=data["password"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"mensaje": "Usuario creado"})

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if not user or user.password != data["password"]:
        return jsonify({"error": "Credenciales incorrectas"}), 401

    token = create_access_token(identity=user.username)

    return jsonify({"token": token})

@app.route("/profile")
@jwt_required()
def profile():
    return jsonify({"mensaje": "Ruta protegida"})

if __name__ == "__main__":

    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG") == "True"

    app.run(port=port, debug=debug)