import tkinter as tk
import consultas_Materias


# funcion para llamar siguiente ventana de consultas

def Sig_ventana(nombre, cedula):
    consultas_Materias.ventana_consulta_materias(nombre, cedula)

# funcion para consultar notas


def crear_ventanaE(nombre, cedula):
    # Crear la ventana principal

    root = tk.Tk()

    root.configure(bg='#0066CC')

    frame = tk.Frame(root, bg='white',
                     highlightbackground='#0066CC', highlightthickness=5)
    frame.pack(padx=5, pady=5)


# Crear las etiquetas de bienvenida y las opciones
    welcome_label = tk.Label(frame, text=f"¡Bienvenido!, {nombre} ", bg='white',
                             font=('Arial', 26), fg='black')
    welcome_label.pack()

    consult_button = tk.Button(frame, text="Consultar",
                               bg='gray', font=('Arial', 15), fg='white', command=lambda: Sig_ventana(nombre, cedula))
    consult_button.pack(padx=40)


# Ejecutar la aplicación
    root.mainloop()
