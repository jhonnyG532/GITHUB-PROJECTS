from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    # Corregido: Column con 'n' y String con 'S' mayúscula
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(20), nullable=False, default='usuario')

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'rol': self.rol
        }