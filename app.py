from flask import Flask, jsonify, request
from app_bcv import TasaBCV

app = Flask(__name__)

@app.route('/tasa/bcv/hoy', methods=['GET'])
def get_tasa_bcv_hoy():
    try:
        tasa = TasaBCV.hoy()
        return jsonify({'tasa': tasa}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tasa/bcv', methods=['GET'])
def get_tasa_bcv():
    fecha = request.args.get('fecha')
    if not fecha:
        return jsonify({'error': 'Se requiere la fecha como parámetro'}), 400

    try:
        tasa = TasaBCV.fecha(fecha)
        return jsonify({'Tasa': tasa}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tasa/bcv/rango', methods=['GET'])
def get_tasa_bcv_rango():
    fecha_inicio = request.args.get('inicio')
    fecha_fin = request.args.get('fin')
    
    if not fecha_inicio or not fecha_fin:
        return jsonify({'error': 'Se requieren las fechas de inicio y fin como parámetros'}), 400

    try:
        tasas = TasaBCV.desde_hasta(fecha_inicio, fecha_fin)
        return jsonify(tasas), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

#ejemplos:

#http://127.0.0.1:5000/tasa/bcv/hoy  te arroja la de hoy
#http://127.0.0.1:5000/tasa/bcv?fecha=09/03/2024
#http://127.0.0.1:5000/tasa/bcv/rango?inicio=10/2/2025&fin=20/2/2025

