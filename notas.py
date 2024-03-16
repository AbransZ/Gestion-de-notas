import tkinter as tk
from tkinter import ttk, messagebox

import mysql.connector


def ventanaNotas():

    def cargar_datos():
        connection = mysql.connector.connect(
            host='localhost', user='root', password='', database='registro')
        cursor = connection.cursor()
        query = """
            SELECT materias.id_ma, materias.nombre AS materia, usuarios.nombre AS estudiante,usuarios.Cedula as cedula, notas.calificacion
            FROM materias_estu
            JOIN materias ON materias_estu.id_ma = materias.id_ma
            JOIN usuarios ON materias_estu.ced_estudiante = usuarios.cedula
            JOIN notas ON materias_estu.id_ma = notas.id_materia AND materias_estu.ced_estudiante = notas.ced_estudiante
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return rows

    def agregar_calificacion():

        # Crear una ventana secundaria para agregar una nueva calificación
        add_window = tk.Toplevel()
        add_window.title("Agregar Calificación")

        # Etiquetas y campos de entrada para los datos necesarios
        tk.Label(add_window, text="ID de la Materia:").pack()
        entry_id_ma = tk.Entry(add_window)
        entry_id_ma.pack()

        tk.Label(add_window, text="Cédula del Estudiante:").pack()
        entry_ced_estudiante = tk.Entry(add_window)
        entry_ced_estudiante.pack()

        tk.Label(add_window, text="Nueva Calificación:").pack()
        entry_calificacion = tk.Entry(add_window)
        entry_calificacion.pack()

        def insertar_calificacion():
            # Obtener los valores ingresados por el usuario
            id_ma = entry_id_ma.get()
            ced_estudiante = entry_ced_estudiante.get()
            nueva_calificacion = entry_calificacion.get()

            # Conectar a la base de datos y agregar la calificación
            connection = mysql.connector.connect(
                host='localhost', user='root', password='', database='registro')
            cursor = connection.cursor()
            query = "INSERT INTO notas (id_materia, ced_estudiante, calificacion) VALUES (%s, %s, %s)"
            cursor.execute(query, (id_ma, ced_estudiante, nueva_calificacion))
            connection.commit()
            messagebox.showinfo(
                "Exito!", "Calificacion agregada correctamente")
            connection.close()

            # Actualizar la tabla
            actualizar_tabla()

            # Cerrar la ventana de agregar
            add_window.destroy()

        # Botón para agregar la calificación
        tk.Button(add_window, text="Agregar",
                  command=insertar_calificacion).pack()

    def modificar_calificacion():
        # Obtener el item seleccionado en la tabla
        item = tree.selection()[0]
        # Obtener los valores actuales de la fila seleccionada
        values = tree.item(item, 'values')
        # Obtener los nuevos valores de la fila seleccionada
        id_ma = values[0]
        materia = values[1]
        estudiante = values[2]
        cedula = values[3]
        calificacion = values[4]

        # Crear una ventana secundaria para editar la calificación
        edit_window = tk.Toplevel()
        edit_window.title("Editar Calificación")

        # Etiquetas y campos de entrada para los datos necesarios
        tk.Label(edit_window, text="ID de la Materia:").pack()
        entry_id_ma = tk.Entry(edit_window)
        entry_id_ma.insert(0, id_ma)  # Inserta el valor actual
        entry_id_ma.pack()

        tk.Label(edit_window, text="Nombre del Estudiante:").pack()
        entry_estudiante = tk.Entry(edit_window)
        entry_estudiante.insert(0, estudiante)  # Inserta el valor actual
        entry_estudiante.pack()

        tk.Label(edit_window, text="Cédula del Estudiante:").pack()
        entry_cedula = tk.Entry(edit_window)
        entry_cedula.insert(0, cedula)  # Inserta el valor actual
        entry_cedula.pack()

        tk.Label(edit_window, text="Calificación:").pack()
        entry_calificacion = tk.Entry(edit_window)
        entry_calificacion.insert(0, calificacion)  # Inserta el valor actual
        entry_calificacion.pack()

        def actualizar_calificacion():
            # Obtener los nuevos valores ingresados por el usuario
            id_ma_nuevo = entry_id_ma.get()
            estudiante_nuevo = entry_estudiante.get()
            cedula_nuevo = entry_cedula.get()
            calificacion_nueva = entry_calificacion.get()

            # Verificar que los valores ingresados sean válidos
            if calificacion_nueva.isdigit():
                calificacion_nueva = int(calificacion_nueva)

                # Actualizar la calificación en la base de datos
                connection = mysql.connector.connect(
                    host='localhost', user='root', password='', database='registro')
                cursor = connection.cursor()
                query = "UPDATE notas SET calificacion = %s WHERE id_materia = %s AND ced_estudiante = %s"
                cursor.execute(query, (calificacion_nueva,
                               id_ma_nuevo, cedula_nuevo))
                connection.commit()

                # Verificar que la actualización fue exitosa
                if cursor.rowcount > 0:
                    messagebox.showinfo(
                        "Exito!", "Calificación modificada correctamente")
                else:
                    messagebox.showerror(
                        "Error", "No se pudo modificar la calificación.")

                connection.close()

                # Actualizar la tabla
                actualizar_tabla()

                # Cerrar la ventana de edición
                edit_window.destroy()
            else:
                messagebox.showerror(
                    "Error", "La calificación debe ser un número entero.")

                # Cerrar la ventana de edición
                edit_window.destroy()

        # Botón para actualizar la calificación
        tk.Button(edit_window, text="Actualizar",
                  command=actualizar_calificacion).pack()

    def eliminar_calificacion():
        # Verificar si hay una fila seleccionada
        if tree.selection():
            # Obtener el índice de la fila seleccionada
            item = tree.selection()[0]
            # Obtener los valores de la fila seleccionada
            values = tree.item(item, 'values')
            # Obtener la información necesaria para identificar el registro en la base de datos
            id_ma = values[0]
            ced_estudiante = values[3]

            # Confirmar la eliminación con el usuario
            confirm = messagebox.askyesno(
                "Confirmación", "¿Estás seguro de que quieres eliminar esta calificación?")
            if confirm:
                # Conectar a la base de datos
                connection = mysql.connector.connect(
                    host='localhost', user='root', password='', database='registro')
                cursor = connection.cursor()

                # Ejecutar la consulta SQL para eliminar el registro
                query = "DELETE FROM notas WHERE id_materia = %s AND ced_estudiante = %s"
                cursor.execute(query, (id_ma, ced_estudiante))
                connection.commit()

                # Cerrar la conexión a la base de datos
                connection.close()

                # Eliminar la fila del Treeview
                tree.delete(item)

                # Mostrar un mensaje de éxito
                messagebox.showinfo(
                    "Éxito", "La calificación ha sido eliminada.")
            else:
                # Mostrar un mensaje de cancelación
                messagebox.showinfo(
                    "Cancelado", "No se eliminó la calificación.")
        else:
            # Mostrar un mensaje de error si no hay fila seleccionada
            messagebox.showerror("Error", "No hay ninguna fila seleccionada.")

    def actualizar_tabla():
        # Limpiar la tabla
        for row in tree.get_children():
            tree.delete(row)
        # Cargar los datos actualizados y agregarlos a la tabla
        for row in cargar_datos():
            tree.insert("", "end", values=row)

    root = tk.Tk()
    root.title("Gestión de Calificaciones")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Crear el Treeview
    tree = ttk.Treeview(frame, columns=("Id",
                                        "Materia", "Estudiante", "Cedula", "Calificación"), show="headings")
    tree.heading("Id", text="Id")
    tree.heading("Materia", text="Materia")
    tree.heading("Estudiante", text="Estudiante")
    tree.heading("Cedula", text="Cedula")
    tree.heading("Calificación", text="Calificación")
    tree.pack(side="left")

    # Agregar scrollbars
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    vsb.pack(side="right", fill="y")
    tree.configure(yscrollcommand=vsb.set)

    # Cargar datos
    for row in cargar_datos():
        tree.insert("", "end", values=row)

    # Botones de acción
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    add_button = tk.Button(
        button_frame, text="Agregar Calificación", command=agregar_calificacion)
    add_button.pack(side="left", padx=5)

    edit_button = tk.Button(
        button_frame, text="Modificar Calificación", command=modificar_calificacion)
    edit_button.pack(side="left", padx=5)

    delete_button = tk.Button(
        button_frame, text="Eliminar Calificación", command=eliminar_calificacion)
    delete_button.pack(side="left", padx=5)

    refresh_button = tk.Button(
        button_frame, text="Actualizar Tabla", command=actualizar_tabla)
    refresh_button.pack(side="left", padx=5)

    root.mainloop()
