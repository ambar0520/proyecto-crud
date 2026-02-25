from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Conexión a MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ambar0522",
    database="Proyecto_Crud"
)

## Ruta para el registro de usuarios
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        Username = request.form['username']
        Password = request.form['password']
        cursor = db.cursor()
        sql = "INSERT INTO USERS (Username, Password) VALUES (%s, %s)"
        values = (Username, Password)
        cursor.execute(sql, values)
        db.commit()
        cursor.close()
        return "Usuario registrado con éxito"
    return render_template('register.html')

## Ruta para el login
@app.route('/login', methods=['GET'])
def login():
    Username = request.form['username']
    Password = request.form['password']

    cursor = db.cursor()
    sql = "SELECT * FROM USERS WHERE Username = %s AND Password = %s"
    values = (Username, Password)
    cursor.execute(sql, values)
    user = cursor.fetchone()
    cursor.close()

    if user:
        return "Inicio de sesión exitoso"
    else:
        return "Usuario o contraseña incorrectos"

## Ruta de contraseña olvidada
@app.route('/forgot-password', methods=['GET'])
def forgot_password():
    Username = request.form['username']
    cursor = db.cursor()
    sql = "SELECT * FROM USERS WHERE Username = %s"
    cursor.execute(sql, (Username,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return "Se ha enviado un enlace de recuperación de contraseña a tu correo electrónico."
    else:
        return "Usuario no encontrado."

if __name__ == '__main__':
    app.run(debug=True)




