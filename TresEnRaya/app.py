import customtkinter as ctk
from tkinter import messagebox

# Configurar tema oscuro
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Tres en Raya")
ventana.geometry("500x600")

# Configurar las columnas para centrar el contenido
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)

lbl_title = ctk.CTkLabel(ventana, text="Juego Tres en Raya", font=("Arial", 24, "bold"))
lbl_title.grid(row=0, column=0, columnspan=3, pady=(10, 0))

casillas = [" " for _ in range(9)]
botones = []
turno = "X"

label_turno = ctk.CTkLabel(ventana, text=f"Turno: {turno}", font=("Arial", 16))
label_turno.grid(row=1, column=0, columnspan=3, pady=(10, 0))


def crear_tablero():
    for i in range(9):
        boton = ctk.CTkButton(
            ventana,
            text=" ",
            width=120,
            height=120,
            font=("Arial", 32, "bold"),
            command=lambda i=i: jugada(i),
            fg_color="#2b2b2b",
            hover_color="#3b3b3b",
        )
        botones.append(boton)
        boton.grid(row=2 + i // 3, column=i % 3, padx=0, pady=2)


def actualizar_turno():
    label_turno.configure(text=f"Turno: {turno}")


def deshabilitar_todo():
    for b in botones:
        b.configure(state="disabled")


def reiniciar():
    global casillas, turno
    casillas = [" " for _ in range(9)]
    turno = "X"
    for b in botones:
        b.configure(text=" ", state="normal")
    actualizar_turno()


def jugada(indice):
    global turno
    if casillas[indice] != " ":
        return
    casillas[indice] = turno
    botones[indice].configure(text=turno, state="disabled")
    if verificar_ganador(turno):
        messagebox.showinfo("Fin del juego", f"¡El jugador {turno} ha ganado!")
        reiniciar()

    else:
        if " " not in casillas:
            messagebox.showinfo("Fin del juego", "Empate")
            deshabilitar_todo()
            reiniciar()
            return
        turno = "O" if turno == "X" else "X"
        actualizar_turno()


def verificar_ganador(jugador):
    # Filas
    for fila in range(3):
        if (
            casillas[fila * 3]
            == casillas[fila * 3 + 1]
            == casillas[fila * 3 + 2]
            == jugador
        ):
            return True
    # Columnas
    for col in range(3):
        if casillas[col] == casillas[col + 3] == casillas[col + 6] == jugador:
            return True
    # Diagonales
    if casillas[0] == casillas[4] == casillas[8] == jugador:
        return True
    if casillas[2] == casillas[4] == casillas[6] == jugador:
        return True
    return False


crear_tablero()

boton_reiniciar = ctk.CTkButton(
    ventana, text="Reiniciar", command=reiniciar, font=("Arial", 14), height=40
)
boton_reiniciar.grid(row=5, column=0, columnspan=3, pady=(10, 15))

ventana.mainloop()
