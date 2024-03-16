import tkinter as tk
from tkinter import messagebox
import mysql.connector


def guardarMateria(id, nombre):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "INSERT INTO materias (id_ma, nombre) VALUES (%s, %s)"
    cursor.execute(query, (id, nombre))
    connection.commit()
    connection.close()


def consultarMateria(id):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT * FROM materias WHERE id_ma = %s"
    cursor.execute(query, (id,))
    materia = cursor.fetchone()
    connection.close()
    return materia


def actualizarMateria(id, nombre):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "UPDATE materias SET nombre = %s  WHERE id_ma = %s"
    cursor.execute(query, (nombre, id))
    connection.commit()
    messagebox.showinfo("Éxito", "Materia actualizada correctamente")
    connection.close()


def ventanaMate():
    materias_window = tk.Tk()
    materias_window.title("Gestión de Materias")
    materias_window.configure(bg='#0066CC')

    title_label = tk.Label(materias_window, text="Gestión de Materias",
                           bg='#0066CC', fg='white', font=('Arial', 20))
    title_label.pack(pady=10)

    id_label = tk.Label(materias_window, text="Matrícula:",
                        bg='#0066CC', fg='white', font=('Arial', 12))
    id_label.pack()
    id_entry = tk.Entry(materias_window, width=30)
    id_entry.pack()

    nombre_label = tk.Label(materias_window, text="Nombre:",
                            bg='#0066CC', fg='white', font=('Arial', 12))
    nombre_label.pack()
    nombre_entry = tk.Entry(materias_window, width=30)
    nombre_entry.pack()

    def guardarNuevaMateria():
        id = int(id_entry.get())
        nombre = nombre_entry.get()
        guardarMateria(id, nombre)
        messagebox.showinfo("Éxito", "Materia guardada correctamente")

    def consultarMostrarMateria():
        id = int(id_entry.get())
        materia = consultarMateria(id)
        if materia:
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, materia[1])
        else:
            messagebox.showinfo("Error", "Materia no encontrada")

    def actualizarMateriaExistente():
        id = int(id_entry.get())
        nombre = nombre_entry.get()
        actualizarMateria(id, nombre)
        nombre_entry.delete(0, tk.END)
        id_entry.delete(0, tk.END)

    save_button = tk.Button(materias_window, text="Guardar Nueva", bg='gray', fg='white', font=(
        'Arial', 12), command=guardarNuevaMateria)
    save_button.pack(pady=10)

    consult_button = tk.Button(materias_window, text="Consultar Materia", bg='gray', fg='white', font=(
        'Arial', 12), command=consultarMostrarMateria)
    consult_button.pack(pady=5)

    update_button = tk.Button(materias_window, text="Actualizar Materia", bg='gray', fg='white', font=(
        'Arial', 12), command=actualizarMateriaExistente)
    update_button.pack(pady=5)

    cancel_button = tk.Button(materias_window, text="Cancelar", bg='gray', fg='white', font=(
        'Arial', 12), command=materias_window.destroy)
    cancel_button.pack()

    materias_window.mainloop()
