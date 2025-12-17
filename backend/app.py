from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/alumno', methods=['POST'])
def guardar_alumno():
    data = request.json
    campos = [
        'rut', 'nombre', 'fecha_nacimiento', 'direccion', 'colegio_procedencia', 'cursos_repetidos',
        'nombre_padre', 'rut_padre', 'nombre_madre', 'rut_madre', 'nombre_contest_encuesta',
        'jefe_hogar', 'vive_hogar', 'titular', 'titrut', 'titphone', 'suplente', 'suprut', 'supphone',
        'n_hermanos', 'hermanos_estudian', 'hermanos_no_estudian', 'otros_viven', 'ocupacion_madre',
        'ocupacion_jefe', 'psicolog', 'aprende', 'estudia', 'religion', 'pie', 'emergencia',
        'domicilio', 'celular', 'enfermedad', 'chile_solidario', 'presento_certificado',
        'necesita_PAE', 'figura_pate', 'fig_aporta_recursos', 'locomocion', 'asistereligion',
        'ano_madre', 'ano_jefe', 'curso', 'letra'
    ]
    values = [data.get(campo) for campo in campos]
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute(f'''
            INSERT OR REPLACE INTO alumnos (
                {', '.join(campos)}
            ) VALUES ({','.join(['?']*len(campos))})
        ''', values)
        conn.commit()
        return jsonify({'status': 'ok'})
    except Exception as e:
        print("Error:", e)
        return jsonify({'status': 'error', 'error': str(e)}), 400
    finally:
        conn.close()

# (Opcional) Endpoint para obtener alumno por RUT
@app.route('/api/alumno/<rut>', methods=['GET'])
def obtener_alumno(rut):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM alumnos WHERE rut = ?', (rut,))
    alumno = c.fetchone()
    conn.close()
    if alumno:
        return jsonify(dict(alumno))
    else:
        return jsonify({'error': 'No encontrado'}), 404

@app.route('/api/alumnos', methods=['GET'])
def listar_alumnos():
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM alumnos ORDER BY rut DESC LIMIT 40')
    alumnos = [dict(row) for row in c.fetchall()]
    conn.close()
    return jsonify(alumnos)

if __name__ == '__main__':
    app.run(debug=True)