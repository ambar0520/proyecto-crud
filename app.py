from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",          # ajusta según tu configuración
    password="Ambar0522", # ajusta según tu configuración
    database="Proyecto_Crud"
)

# ------------------ CREATE ------------------
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

# ------------------ READ ------------------
@app.route('/users')
def users():
    cursor = db.cursor()
    sql = "SELECT * FROM USERS"
    cursor.execute(sql)
    users = cursor.fetchall()   # importante para consumir resultados
    cursor.close()
    return render_template('users.html', users=users)

# ------------------ LOGIN ------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Username = request.form['username']
        Password = request.form['password']
        cursor = db.cursor()
        sql = "SELECT * FROM USERS WHERE Username = %s AND Password = %s"
        cursor.execute(sql, (Username, Password))
        user = cursor.fetchone()   # importante para consumir resultados
        cursor.close()

        if user:
            return "Inicio de sesión exitoso"
        else:
            return "Usuario o contraseña incorrectos"
    return render_template('login.html')

# ------------------ UPDATE ------------------
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        Username = request.form['username']
        NewPassword = request.form['new_password']
        cursor = db.cursor()
        sql = "UPDATE USERS SET Password = %s WHERE Username = %s"
        cursor.execute(sql, (NewPassword, Username))
        db.commit()
        cursor.close()
        return "Contraseña actualizada con éxito"
    return render_template('update.html')

# ------------------ DELETE ------------------
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        user_id = request.form['id']   # el formulario debe pedir el ID
        cursor = db.cursor()
        sql = "DELETE FROM USERS WHERE ID = %s"
        cursor.execute(sql, (user_id,))
        db.commit()
        cursor.close()
        return "Usuario eliminado con éxito"
    return render_template('delete.html')


# ------------------ FORGOT PASSWORD ------------------
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        Username = request.form['username']
        cursor = db.cursor()
        sql = "SELECT * FROM USERS WHERE Username = %s"
        cursor.execute(sql, (Username,))
        user = cursor.fetchone()   # importante
        cursor.close()

        if user:
            return "Se ha enviado un enlace de recuperación (simulado)"
        else:
            return "Usuario no encontrado"
    return render_template('forgot_pass.html')

# ------------------ MAIN ------------------
if __name__ == "__main__":
    app.run(debug=True)


