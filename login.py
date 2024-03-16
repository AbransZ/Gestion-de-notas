import tkinter as tk
from tkinter import messagebox
import mysql.connector
import indexP
import IndexE
import indexD

# Funcion para llamar las ventanas necesarias


def Estudiante(nombre, cedula):
    IndexE.crear_ventanaE(nombre, cedula)


def Profesor(nombre, cedula):
    indexP.crear_ventana(nombre, cedula)


def Director(nombre, cedula):
    indexD.VentanaDirector(nombre, cedula)
# funcion para conectar con base de datos


def login(username_entry, password_entry):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="registro"
        )

        cursor = conn.cursor()
        query = "SELECT * FROM usuarios WHERE cedula=%s AND contrasenia=%s"
        cursor.execute(query, (int(username_entry.get()),
                       int(password_entry.get())))
        resultado = cursor.fetchone()

        if resultado:

            nombre = resultado[1]
            cedula = resultado[0]

            nivel = resultado[3]
            if nivel == 1:

                clear_fields()
                messagebox.showinfo("Éxito", "Bienvenido estudiante.")
                Estudiante(nombre, cedula)

            elif nivel == 2:
                clear_fields()
                messagebox.showinfo("Éxito", "Bienvenido profesor.")
                Profesor(nombre, cedula)

            elif nivel == 3:
                clear_fields()
                messagebox.showinfo("Éxito", "Bienvenido Director.")
                Director(nombre, cedula)

            else:
                messagebox.showerror("Error", "Nivel de usuario desconocido.")
        else:
            messagebox.showerror("Error", "Cédula o contraseña incorrecta.")

        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error de Base de Datos", str(err))
    except Exception as e:
        messagebox.showerror("Error Inesperado", str(e))
    return conn

# Función para realizar el inicio de sesión cuando se presiona el botón


def perform_login():
    login(username_entry, password_entry)


# funcion para limpiar campos


def clear_fields():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Función de inicio de sesión


# Crear la ventana principal
window = tk.Tk()
window.title("Inicio de Sesion")
window.geometry('300x200')

# Crear un marco para contener los elementos de la interfaz de usuario
frame = tk.Frame(master=window, padx=20, pady=20)
frame.pack()

# Crear y empaquetar etiquetas y campos de entrada
username_label = tk.Label(frame, text="Ingrese su cedula")
username_label.pack()
username_entry = tk.Entry(frame)
username_entry.pack()

password_label = tk.Label(frame, text="Contraseña")
password_label.pack()
password_entry = tk.Entry(frame, show="*")  # Oculta el texto ingresado
password_entry.pack()

# Crear y empaquetar el botón de inicio de sesión
login_button = tk.Button(frame, text="Iniciar sesión", command=perform_login)
login_button.pack(side=tk.LEFT, padx=(0, 10), pady=20)

# Crear boton para limpiar los campos

clear_button = tk.Button(frame, text="Limpiar", command=clear_fields)
clear_button.pack(side=tk.LEFT, pady=20)

# Ejecutar el bucle principal de Tkinter
window.mainloop()
# version de prueba
