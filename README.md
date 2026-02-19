#Proyecto CRUD con Flask, MYSQL Y JavaScript

Este proyecto implementa un sistema básico de **Registro** y **Login** de Usuarios.
El objetivo es conectar formularios en HTML con una base de datos MYSQL usando FLASK
---

##Archivos principales

- **app.py** → Archivo principal de la aplicación Flask. 
- Se conecta con la base de datos MySQL. 
- Define las rutas `/register` y `/login`. 
- Procesa los datos enviados desde los formularios HTML. 

- **register.html** → Formulario de registro de usuarios. 
- Pide nombre de usuario y contraseña. 
- Envía los datos a la ruta `/register`. 
- Incluye validaciones básicas con JavaScript en el frontend. 

- **login.html** → Formulario de inicio de sesión.
 - Permite que un usuario ya registrado ingrese sus credenciales.
  - Envía los datos a la ruta `/login`. 
  - Usa JavaScript para mejorar la interacción del usuario. ---

  ##Bse de Datos

  en Mysql Workbench se creo la base de datos y la tabla de usuarios:

  ```sql
CREATE DATABASE Proyecto_Crud;
USE Proyecto_Crud;

CREATE TABLE USERS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50),
    Password VARCHAR(100) NOT NULL
);