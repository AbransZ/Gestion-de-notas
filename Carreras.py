import tkinter as tk
from tkinter import messagebox
import mysql.connector


def guardarCarrera(id, nombre):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "INSERT INTO carreras (id, nombre) VALUES (%s, %s)"
    cursor.execute(query, (id, nombre))
    connection.commit()

    connection.close()


def consultarCarrera(id):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT * FROM carreras WHERE id = %s"
    cursor.execute(query, (id,))
    materia = cursor.fetchone()
    connection.close()
    return materia


def actualizarCarrera(id, nombre):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "UPDATE carreras SET nombre = %s  WHERE id = %s"
    cursor.execute(query, (nombre, id))
    connection.commit()
    messagebox.showinfo("Éxito", "Carrera actualizada correctamente")

    connection.close()


def ventanaCarr():
    materias_window = tk.Tk()
    materias_window.title("Gestión de Carreras")
    materias_window.configure(bg='#0066CC')

    title_label = tk.Label(materias_window, text="Gestión de Carreras",
                           bg='#0066CC', fg='white', font=('Arial', 20))
    title_label.pack(pady=10)

    id_label = tk.Label(materias_window, text="Identificador:",
                        bg='#0066CC', fg='white', font=('Arial', 12))
    id_label.pack()
    id_entry = tk.Entry(materias_window, width=30)
    id_entry.pack()

    nombre_label = tk.Label(materias_window, text="Nombre:",
                            bg='#0066CC', fg='white', font=('Arial', 12))
    nombre_label.pack()
    nombre_entry = tk.Entry(materias_window, width=30)
    nombre_entry.pack()

    def guardarNuevaCarrera():
        id = int(id_entry.get())
        nombre = nombre_entry.get()
        guardarCarrera(id, nombre)
        messagebox.showinfo("Éxito", "Carrera guardada correctamente")
        nombre_entry.delete(0, tk.END)
        id_entry.delete(0, tk.END)

    def consultarMostrarCarrera():
        id = int(id_entry.get())
        materia = consultarCarrera(id)
        if materia:
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, materia[1])
        else:
            messagebox.showinfo("Error", "Carrera no encontrada")

    def actualizarCarreraExistente():
        id = int(id_entry.get())
        nombre = nombre_entry.get()
        actualizarCarrera(id, nombre)
        nombre_entry.delete(0, tk.END)
        id_entry.delete(0, tk.END)

    save_button = tk.Button(materias_window, text="Guardar Nueva", bg='gray', fg='white', font=(
        'Arial', 12), command=guardarNuevaCarrera)
    save_button.pack(pady=10)

    consult_button = tk.Button(materias_window, text="Consultar Materia", bg='gray', fg='white', font=(
        'Arial', 12), command=consultarMostrarCarrera)
    consult_button.pack(pady=5)

    update_button = tk.Button(materias_window, text="Actualizar Materia", bg='gray', fg='white', font=(
        'Arial', 12), command=actualizarCarreraExistente)
    update_button.pack(pady=5)

    cancel_button = tk.Button(materias_window, text="Cancelar", bg='gray', fg='white', font=(
        'Arial', 12), command=materias_window.destroy)
    cancel_button.pack()

    materias_window.mainloop()
