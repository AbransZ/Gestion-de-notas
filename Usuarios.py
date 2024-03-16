import tkinter as tk
import mysql.connector


# Función para guardar un nuevo usuario


def guardarUsuario(cedula, nombre, contrasenia, nivel):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "INSERT INTO usuarios (Cedula, nombre, contrasenia, nivel) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (cedula, nombre, contrasenia, nivel))
    connection.commit()
    connection.close()

# Función para consultar un usuario por su cédula


def consultarUsuario(cedula):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "SELECT * FROM usuarios WHERE Cedula = %s"
    cursor.execute(query, (cedula,))
    usuario = cursor.fetchone()  # Obtener el primer usuario que coincida con la cédula
    connection.close()
    return usuario

# Función para actualizar los valores de un usuario


def actualizarUsuario(cedula, nombre, contrasenia, nivel):
    connection = mysql.connector.connect(
        host='localhost', user='root', password='', database='registro')
    cursor = connection.cursor()
    query = "UPDATE usuarios SET nombre = %s, contrasenia = %s, nivel = %s WHERE Cedula = %s"
    cursor.execute(query, (nombre, contrasenia, nivel, cedula))
    connection.commit()
    connection.close()

# Función para crear la ventana de gestión de usuarios


def ventanaUsuarios():
    # Crear la ventana
    usuarios_window = tk.Toplevel()
    usuarios_window.title("Gestión de Usuarios")
    usuarios_window.configure(bg='#0066CC')

    # Etiqueta de título
    title_label = tk.Label(usuarios_window, text="Gestión de Usuarios",
                           bg='#0066CC', fg='white', font=('Arial', 20))
    title_label.pack(pady=10)

    # Campos de entrada para datos del usuario
    cedula_label = tk.Label(usuarios_window, text="Cédula:",
                            bg='#0066CC', fg='white', font=('Arial', 12))
    cedula_label.pack()
    cedula_entry = tk.Entry(usuarios_window, width=30)
    cedula_entry.pack()

    nombre_label = tk.Label(usuarios_window, text="Nombre:",
                            bg='#0066CC', fg='white', font=('Arial', 12))
    nombre_label.pack()
    nombre_entry = tk.Entry(usuarios_window, width=30)
    nombre_entry.pack()

    contrasenia_label = tk.Label(
        usuarios_window, text="Contraseña:", bg='#0066CC', fg='white', font=('Arial', 12))
    contrasenia_label.pack()
    contrasenia_entry = tk.Entry(usuarios_window, width=30, show="*")
    contrasenia_entry.pack()

    nivel_label = tk.Label(usuarios_window, text="Nivel:",
                           bg='#0066CC', fg='white', font=('Arial', 12))
    nivel_label.pack()
    nivel_entry = tk.Entry(usuarios_window, width=30)
    nivel_entry.pack()

    # Función para guardar un nuevo usuario
    def guardarNuevoUsuario():
        cedula = int(cedula_entry.get())
        nombre = nombre_entry.get()
        contrasenia = contrasenia_entry.get()
        nivel = int(nivel_entry.get())
        guardarUsuario(cedula, nombre, contrasenia, nivel)

    # Función para consultar y mostrar un usuario
    def consultarMostrarUsuario():
        cedula = int(cedula_entry.get())
        usuario = consultarUsuario(cedula)
        if usuario:
            nombre_entry.delete(0, tk.END)
            contrasenia_entry.delete(0, tk.END)
            nivel_entry.delete(0, tk.END)
            # Índice 1 es el campo de nombre en la consulta
            nombre_entry.insert(0, usuario[1])
            # Índice 2 es el campo de contraseña
            contrasenia_entry.insert(0, usuario[2])
            nivel_entry.insert(0, usuario[3])  # Índice 3 es el campo de nivel
        else:
            tk.messagebox.showinfo("Error", "Usuario no encontrado")

    # Función para actualizar un usuario existente
    def actualizarUsuarioExistente():
        cedula = int(cedula_entry.get())
        nombre = nombre_entry.get()
        contrasenia = contrasenia_entry.get()
        nivel = int(nivel_entry.get())
        actualizarUsuario(cedula, nombre, contrasenia, nivel)
        tk.messagebox.showinfo("Éxito", "Usuario actualizado correctamente")

    # Botones de acciones
    save_button = tk.Button(usuarios_window, text="Guardar Nuevo", bg='gray', fg='white', font=(
        'Arial', 12), command=guardarNuevoUsuario)
    save_button.pack(pady=10)

    consult_button = tk.Button(usuarios_window, text="Consultar Usuario",
                               bg='gray', fg='white', font=('Arial', 12), command=consultarMostrarUsuario)
    consult_button.pack(pady=5)

    update_button = tk.Button(usuarios_window, text="Actualizar Usuario",
                              bg='gray', fg='white', font=('Arial', 12), command=actualizarUsuarioExistente)
    update_button.pack(pady=5)

    cancel_button = tk.Button(usuarios_window, text="Cancelar", bg='gray', fg='white', font=(
        'Arial', 12), command=usuarios_window.destroy)
    cancel_button.pack()

    usuarios_window.mainloop()
