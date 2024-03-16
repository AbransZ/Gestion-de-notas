import tkinter as tk
from tkinter import ttk, Label
import mysql.connector


# funcion para llamar esta ventana


def ventana_consulta_materias(nombre, cedula):
    # Conectarse a la base de datos y obtener las materias del estudiante
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='registro'
    )
    cursor = connection.cursor()

    query = ("SELECT u.nombre AS Profesor, m.nombre AS Materia, n.calificacion AS Calificacion FROM usuarios AS u JOIN materia_prof AS mp ON u.cedula = mp.ced_prof JOIN materias AS m ON mp.id_materia = m.id_ma JOIN materias_estu AS me ON m.id_ma = me.id_ma JOIN notas AS n ON me.ced_estudiante = n.ced_estudiante AND m.id_ma = n.id_materia WHERE me.ced_estudiante  = %s")
    cursor.execute(query, (cedula,))

    # Obtener las filas de resultados
    rows = cursor.fetchall()

    root = tk.Tk()
    root.title("Materias del Estudiante")

    # Crear el estilo para el Treeview
    style = ttk.Style()
    style.configure("Treeview", font=('Arial',  12, 'bold', 'black'))

    # Crear el Treeview con el estilo aplicado
    tree = ttk.Treeview(root, columns=(
        'Materia', 'profesor', 'calificacion'), show='headings')
    tree.heading('#1', text='profesor')
    tree.heading('#2', text='Materia')
    tree.heading('#3', text='calificacion')
    tree.pack(side='top', fill='both', expand=True)

    # Calcular el promedio de las calificaciones
    sum_of_grades = 0
    num_of_grades = len(rows)
    for row in rows:
        # Asumiendo que la calificación es un tipo numérico
        sum_of_grades += float(row[2])
    average_grade = sum_of_grades / num_of_grades if num_of_grades > 0 else 0

    # Crear una etiqueta para mostrar el promedio de calificaciones
    average_label = Label(
        root, text=f"Promedio de Calificaciones: {average_grade}", font=('arial', 12, 'bold'))
    average_label.pack()

    # Insertar datos en el Treeview
    for row in rows:
        tree.insert('', 'end', values=(row[0], row[1], row[2]))

    root.mainloop()
