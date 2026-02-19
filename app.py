from flask import Flask, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conexión a MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",           
    password="Ambar0522",           
    database="Proyecto_Crud"
)

@app.route('/register', methods=['POST'])
def register():
    Username = request.form['username']
    Password = request.form['password']

    cursor = db.cursor()
    sql = "INSERT INTO USERS (Username, Password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()

    return "Usuario registrado con éxito"

if __name__ == '__main__':
    app.run(debug=True)
