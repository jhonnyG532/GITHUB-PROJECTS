import os
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv() 
app = Flask(__name__)
CORS(app) 

class Producto:
    """Clase con atributos encapsulados (uso de _)"""
    def __init__(self, id, nombre, precio):
        self._id = id
        self._nombre = nombre
        self._precio = precio

    def to_dict(self):
        """Método para convertir el objeto a un diccionario JSON"""
        return {
            "id": self._id,
            "nombre": self._nombre,
            "precio": self._precio
        }

class GestorTienda:
    """Clase para manejar las transacciones (CRUD)"""
    def __init__(self):
        self._inventario = []

    def agregar_producto(self, nombre, precio):
        nuevo_id = len(self._inventario) + 1
        nuevo_prod = Producto(nuevo_id, nombre, precio)
        self._inventario.append(nuevo_prod)
        return nuevo_prod.to_dict()

    def listar_todo(self):
        return [p.to_dict() for p in self._inventario]

tienda = GestorTienda()


@app.route('/api/productos', methods=['GET'])
def listar_productos():
    """CRUD: Listar todos los productos"""
    datos = tienda.listar_todo()
    return jsonify({"total": len(datos), "productos": datos}), 200

@app.route('/api/productos', methods=['POST'])
def crear_producto():
    """CRUD: Crear un producto leyendo el Payload JSON"""
    try:
        payload = request.get_json()
        
        if not payload or "nombre" not in payload or "precio" not in payload:
            return jsonify({"error": "Faltan campos obligatorios"}), 400

        nuevo = tienda.agregar_producto(payload["nombre"], payload["precio"])
        return jsonify({"mensaje": "Producto creado", "data": nuevo}), 201

    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    puerto = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    
    app.run(host='0.0.0.0', port=puerto, debug=debug)