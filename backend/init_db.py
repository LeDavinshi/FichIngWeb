import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rut TEXT UNIQUE,
    nombre TEXT,
    fecha_nacimiento TEXT,
    direccion TEXT,
    colegio_procedencia TEXT,
    cursos_repetidos INTEGER,
    nombre_padre TEXT,
    rut_padre TEXT,
    nombre_madre TEXT,
    rut_madre TEXT,
    nombre_contest_encuesta TEXT,
    jefe_hogar TEXT,
    vive_hogar INTEGER,
    titular TEXT,
    titrut TEXT,
    titphone TEXT,
    suplente TEXT,
    suprut TEXT,
    supphone TEXT,
    n_hermanos INTEGER,
    hermanos_estudian INTEGER,
    hermanos_no_estudian INTEGER,
    otros_viven INTEGER,
    ocupacion_madre TEXT,
    ocupacion_jefe TEXT,
    psicolog TEXT,
    aprende TEXT,
    estudia TEXT,
    religion TEXT,
    pie TEXT,
    emergencia TEXT,
    domicilio TEXT,
    celular TEXT,
    enfermedad TEXT,
    chile_solidario INTEGER,
    presento_certificado INTEGER,
    necesita_PAE INTEGER,
    figura_pate INTEGER,
    fig_aporta_recursos INTEGER,
    locomocion INTEGER,
    asistereligion INTEGER,
    ano_madre TEXT,
    ano_jefe TEXT,
    curso TEXT,
    letra TEXT
)
''')
conn.commit()
conn.close()