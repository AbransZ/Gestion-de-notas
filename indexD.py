import tkinter as tk
import consultas_Materias
import Usuarios
import materia
import Carreras
import notas
import gestionProfesores
import gestionarMateriasEstudiantes
# Función para abrir la ventana de consultas de materias


# Función para abrir la ventana de CRUD de usuarios


def ventanaUsuarios():
    Usuarios.ventanaUsuarios()


# Función para abrir la ventana de CRUD de materias


def ventanaMaterias():
    materia.ventanaMate()


# Función para abrir la ventana de CRUD de carreras


def ventanaCarreras():
    Carreras.ventanaCarr()

# Función para abrir la ventana de CRUD de notas


def ventanaNotas():
    notas.ventanaNotas()


def ventanaProfesores():
    gestionProfesores.ventanaAcreditarMateria()


def ventanaInscripcion():
    gestionarMateriasEstudiantes.ventanaInscribirEstudiante()

# Función para abrir la ventana principal del director


def VentanaDirector(nombre, cedula):
    # Crear la ventana principal
    root = tk.Tk()
    root.configure(bg='#0066CC')
    frame = tk.Frame(root, bg='white',
                     highlightbackground='#0066CC', highlightthickness=5)
    frame.pack(padx=5, pady=5)

    # Etiqueta de bienvenida
    welcome_label = tk.Label(frame, text=f"¡Bienvenido Director!, {nombre} ", bg='white',
                             font=('Arial', 26), fg='black')
    welcome_label.pack()

    users_button = tk.Button(frame, text="Gestionar Usuarios",
                             bg='gray', font=('Arial', 15), fg='white', command=ventanaUsuarios)
    users_button.pack(padx=30)

    subjects_button = tk.Button(frame, text="Gestionar Materias",
                                bg='gray', font=('Arial', 15), fg='white', command=ventanaMaterias)
    subjects_button.pack(padx=30)

    careers_button = tk.Button(frame, text="Gestionar Carreras",
                               bg='gray', font=('Arial', 15), fg='white', command=ventanaCarreras)
    careers_button.pack(padx=30)

    grades_button = tk.Button(frame, text="Gestionar Notas",
                              bg='gray', font=('Arial', 15), fg='white', command=ventanaNotas)
    grades_button.pack(padx=30)

    Profesors_button = tk.Button(frame, text="Acreditar materia a profesores",
                                 bg='gray', font=('Arial', 15), fg='white', command=ventanaProfesores)
    Profesors_button.pack(padx=30)

    Profesors_button = tk.Button(frame, text="Acreditar materia a estudiantes",
                                 bg='gray', font=('Arial', 15), fg='white', command=ventanaInscripcion)
    Profesors_button.pack(padx=30)

    root.mainloop()
