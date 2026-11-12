"""Punto de entrada: ``python -m vepo`` abre la ventana principal."""

import tkinter as tk
from tkinter import ttk


def main() -> None:
    """Abre una ventana mínima para comprobar que el entorno funciona."""
    root = tk.Tk()
    root.title("VEPO")
    ttk.Label(root, text="VEPO · entorno listo", padding=40).pack()
    root.mainloop()


if __name__ == "__main__":
    main()
