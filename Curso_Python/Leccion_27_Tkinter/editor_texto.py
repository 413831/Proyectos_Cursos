import tkinter as tk


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor de Texto')
        # Configuración tamaño mínimo de la ventana
        self.rowconfigure(0,minsize=600, weight=1)
        # Configuración mínima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        # Atributo de campo de texto
        self.campo_texto = tk.Text(self,wrap=tk.WORD)
        # Atributo de archivo
        self.archivo = None
        # Atributo para validar si hay un archivo abierto
        self.archivo_abierto = False
        # Creacion de componentes
        self._crear_componentes()

    def _crear_componentes(self):
        frame_botones = tk.Frame(self,relief=tk.RAISED, bd=2)
        boton_abrir = tk.Button(frame_botones, text='Abrir')
        boton_guardar = tk.Button(frame_botones, text='Guardar')
        boton_guardar_como = tk.Button(frame_botones, text='Guardar como')
        # Los botones se expanden de forma horizontal
        boton_abrir.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        boton_guardar_como.grid(row=2, column=0, sticky='we', padx=5, pady=5)
        # Se coloca Frame de forma vertical
        frame_botones.grid(row=0, column=0, sticky='ns')
        # Se agrega campo de texto




if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()