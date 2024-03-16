import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ... (resto de tus funciones guardarCarrera, consultarCarrera, actualizarCarrera)


def profesor_existe(ced_prof):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT * FROM materia_prof WHERE ced_prof = %s"
    cursor.execute(query, (ced_prof,))
    profesor = cursor.fetchone()
    connection.close()
    return profesor is not None


def materia_existe(id_materia):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT * FROM materias WHERE id_ma = %s"
    cursor.execute(query, (id_materia,))
    materia = cursor.fetchone()
    connection.close()
    return materia is not None


def acreditar_materia(ced_prof, id_materia):
    if not profesor_existe(ced_prof):
        messagebox.showerror("Error", "El profesor no esta registrado.")
        return
    if not materia_existe(id_materia):
        messagebox.showerror("Error", "La materia no existe.")
        return

    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "INSERT INTO materia_prof (ced_prof, id_materia) VALUES (%s, %s)"
    cursor.execute(query, (ced_prof, id_materia))
    connection.commit()
    connection.close()
    messagebox.showinfo("Exito!!", "Materia acreditada exitosamente.")


def ventanaAcreditarMateria():
    acreditar_materia_window = tk.Tk()
    acreditar_materia_window.title("Acreditar Materia a Profesor")

    cedula_prof_label = tk.Label(
        acreditar_materia_window, text="Cédula del Profesor")
    cedula_prof_label.pack()
    cedula_prof_entry = tk.Entry(acreditar_materia_window)
    cedula_prof_entry.pack()

    id_materia_label = tk.Label(
        acreditar_materia_window, text="ID de la Materia")
    id_materia_label.pack()
    id_materia_entry = tk.Entry(acreditar_materia_window)
    id_materia_entry.pack()

    acreditar_button = tk.Button(acreditar_materia_window, text="Acreditar Materia",
                                 command=lambda: acreditar_materia(cedula_prof_entry.get(), id_materia_entry.get()))
    acreditar_button.pack()

    cancel_button = tk.Button(
        acreditar_materia_window, text="Cancelar", command=acreditar_materia_window.destroy)
    cancel_button.pack()

    acreditar_materia_window.mainloop()
