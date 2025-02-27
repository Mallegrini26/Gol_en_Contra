from flask import Flask, render_template, request, redirect, session, url_for, flash
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'Argentina'
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'pagina_deportes'

mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        usuario = request.form['usuario']
        password = request.form['password']
        provincia = request.form['provincia']
        descripcion = request.form['descripcion']
        hashed_password = generate_password_hash(password)

        conexion = mysql.connect()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        user = cursor.fetchone()

        if user:
            flash('Este usuario ya está registrado.')
            return redirect(url_for('registro'))

        cursor.execute("INSERT INTO usuarios (nombre, correo, usuario, password, provincia, descripcion) VALUES (%s, %s, %s, %s, %s, %s)", (nombre, correo, usuario, hashed_password, provincia, descripcion))
        conexion.commit()
        flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.')
        return redirect(url_for('login'))

    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        conexion = mysql.connect()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        user = cursor.fetchone()

        if user and check_password_hash(user[4], password):
            session['login'] = True
            session['usuario'] = user[3]
            flash('Inicio de sesión exitoso.')
            return redirect(url_for('index'))
        else:
            flash('Correo electrónico o contraseña incorrectos.')

    return render_template('login.html')

@app.route('/admin/')
def admin_index():
    if not 'login' in session:
        return redirect(url_for('login'))
    return render_template('admin/index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/futbol')
def futbol():
    return render_template('futbol.html')

@app.route('/futbol_ascenso')
def futbol_ascenso():
    return render_template('futbol_ascenso.html')

@app.route('/futbol_internacional')
def futbol_internacional():
    return render_template('futbol_internacional.html')

@app.route('/seleccion_argentina')
def seleccion_argentina():
    return render_template('seleccion_argentina.html')

@app.route('/copa_america')
def copa_america():
    return render_template('copa_america.html')

@app.route('/voley')
def voley():
    return render_template('voley.html')

@app.route('/boxeo')
def boxeo():
    return render_template('boxeo.html')

@app.route('/boxeo2')
def boxeo2():
    return render_template('boxeo2.html')

@app.route('/tenis')
def tenis():
    return render_template('tenis.html')

@app.route('/deportes_varios')
def deportes_varios():
    return render_template('deportes_varios.html')


if __name__ == '__main__':
    app.run(debug=True)
