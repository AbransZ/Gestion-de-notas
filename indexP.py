import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


def cargar_materias(cedula_profesor):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT m.id_ma, m.nombre FROM materias m INNER JOIN materia_prof mp ON m.id_ma = mp.id_materia WHERE mp.ced_prof = %s"
    cursor.execute(query, (cedula_profesor,))
    result = cursor.fetchall()
    connection.close()
    return result


def cargar_estudiantes(id_materia):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT u.cedula, u.nombre FROM usuarios u INNER JOIN materias_estu me ON u.cedula = me.ced_estudiante WHERE me.id_ma = %s"
    cursor.execute(query, (id_materia,))
    result = cursor.fetchall()
    connection.close()
    return result


def obtener_calificaciones(cedula_estudiante, id_materia):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT calificacion FROM notas WHERE ced_estudiante = %s AND id_materia = %s"
    cursor.execute(query, (cedula_estudiante, id_materia))
    result = cursor.fetchall()
    connection.close()
    return [str(row[0]) for row in result]


def crear_ventana(nombre, cedula):
    root = tk.Tk()
    root.configure(bg='#0066CC')

    frame = tk.Frame(root, bg='white',
                     highlightbackground='#0066CC', highlightthickness=5)
    frame.pack(padx=5, pady=5)

    welcome_label = tk.Label(
        frame, text=f"¡Bienvenido! Profesor, {nombre}", bg='white', font=('Arial',   26), fg='black')
    welcome_label.pack()

    materias_profesor = cargar_materias(cedula)
    materias_combo = ttk.Combobox(
        frame, values=[m[1] for m in materias_profesor])
    materias_combo.pack(pady=20, side='top')

    estudiantes_listbox = tk.Listbox(
        frame, height=10, width=40, selectmode=tk.SINGLE)
    estudiantes_listbox.pack(side="left")

    calificacion_entry = tk.Entry(frame)
    calificacion_entry.pack(pady=20)

    calificaciones_label = tk.Label(
        frame, text="Calificaciones: ", bg='white', font=('Arial',   15), fg='black')
    calificaciones_label.pack(pady=25)

    def on_materia_selected(event):
        obtener_estudiantes()

    materias_combo.bind('<<ComboboxSelected>>', on_materia_selected)

    def obtener_estudiantes():
        estudiantes_listbox.delete(0, tk.END)
        id_materia = materias_profesor[materias_combo.current()][0]
        estudiantes = cargar_estudiantes(id_materia)
        for estudiante in estudiantes:
            cedula_estudiante = estudiante[0]
            nombre_estudiante = estudiante[1]
            estudiantes_listbox.insert(
                tk.END, f"{nombre_estudiante} ({cedula_estudiante})")

    def on_estudiante_selected(event):
        seleccionado = estudiantes_listbox.get(
            estudiantes_listbox.curselection())
        cedula_estudiante = int(seleccionado.split(' ')[-1][1:-1])
        id_materia = materias_profesor[materias_combo.current()][0]
        calificaciones = obtener_calificaciones(cedula_estudiante, id_materia)
        calificaciones_label.config(
            text=f"{seleccionado}: {', '.join(calificaciones)}")

    estudiantes_listbox.bind('<<ListboxSelect>>', on_estudiante_selected)

    def registrar():
        calificacion = calificacion_entry.get()
        if not estudiantes_listbox.curselection():
            messagebox.showerror("Error", "No hay estudiante seleccionado")
        seleccionado = estudiantes_listbox.get(
            estudiantes_listbox.curselection())
        cedula_estudiante = int(seleccionado.split(' ')[-1][1:-1])
        id_materia = materias_profesor[materias_combo.current()][0]
        calificaciones_del_estudiante = obtener_calificaciones(
            cedula_estudiante, id_materia)
        if len(calificaciones_del_estudiante) >= 5:
            messagebox.showerror(
                "Error", "El estudiante ya tiene  5 calificaciones para esta materia.")
        else:
            connection = mysql.connector.connect(
                host='localhost', user='root', password='', database='registro')
            cursor = connection.cursor()
            query = "INSERT INTO notas (ced_estudiante, calificacion, id_materia) VALUES (%s, %s, %s)"
            cursor.execute(query, (cedula_estudiante,
                           calificacion, id_materia))
            connection.commit()
            connection.close()
            messagebox.showinfo("Registro", "Registro exitoso!!")
            obtener_estudiantes()

    register_button = tk.Button(frame, text="Registrar", bg='gray', font=(
        'Arial',   15), fg='white', command=registrar)
    register_button.pack(side=tk.LEFT, padx=55)

    consult_button = tk.Button(frame, text="Consultar", bg='gray', font=(
        'Arial',   15), fg='white', command=obtener_estudiantes)
    consult_button.pack(side=tk.RIGHT, padx=55)

    root.mainloop()
