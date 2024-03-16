import tkinter as tk
from tkinter import messagebox
import mysql.connector


def estudiante_existe(ced_estudiante):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT * FROM usuarios WHERE cedula = %s"
    cursor.execute(query, (ced_estudiante,))
    estudiante = cursor.fetchone()
    connection.close()
    return estudiante is not None


def materia_existe(id_materia):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT * FROM materias WHERE id_ma = %s"
    cursor.execute(query, (id_materia,))
    materia = cursor.fetchone()
    connection.close()
    return materia is not None


def inscribir_estudiante(ced_estudiante, id_materia):
    if not estudiante_existe(ced_estudiante):
        messagebox.showerror("Error", "El estudiante no existe.")
        return
    if not materia_existe(id_materia):
        messagebox.showerror("Error", "La materia no existe.")
        return

    try:
        connection = mysql.connector.connect(
            host='localhost', user='root', password='', database='registro')
        cursor = connection.cursor()
        query = "INSERT INTO materias_estu (ced_estudiante, id_ma) VALUES (%s, %s)"
        cursor.execute(query, (ced_estudiante, id_materia))
        connection.commit()
        connection.close()
        messagebox.showinfo(
            "Éxito", "Estudiante inscrito en la materia exitosamente.")
    except mysql.connector.Error as err:
        messagebox.showerror(
            "Error", f"Error al inscribir al estudiante: {err}")


def ventanaInscribirEstudiante():
    inscribir_estudiante_window = tk.Tk()
    inscribir_estudiante_window.title("Inscribir Estudiante en Materia")

    cedula_estudiante_label = tk.Label(
        inscribir_estudiante_window, text="Cédula del Estudiante")
    cedula_estudiante_label.pack()
    cedula_estudiante_entry = tk.Entry(inscribir_estudiante_window)
    cedula_estudiante_entry.pack()

    id_materia_label = tk.Label(
        inscribir_estudiante_window, text="ID de la Materia")
    id_materia_label.pack()
    id_materia_entry = tk.Entry(inscribir_estudiante_window)
    id_materia_entry.pack()

    inscribir_button = tk.Button(inscribir_estudiante_window, text="Inscribir Estudiante",
                                 command=lambda: inscribir_estudiante(cedula_estudiante_entry.get(), id_materia_entry.get()))
    inscribir_button.pack()

    cancel_button = tk.Button(
        inscribir_estudiante_window, text="Cancelar", command=inscribir_estudiante_window.destroy)
    cancel_button.pack()

    inscribir_estudiante_window.mainloop()
