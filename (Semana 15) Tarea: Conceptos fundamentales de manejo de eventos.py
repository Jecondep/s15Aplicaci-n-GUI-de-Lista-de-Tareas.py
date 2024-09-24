
#import tkinter as tk

class AplicaciónDeListaDeTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.tareas = []

        # Crear campo de entrada para nuevas tareas
        self.marco_de_entrada = tk.Frame(self.root)
        self.etiqueta_de_entrada = tk.Label(self.marco_de_entrada, text="Nueva Tarea:")
        self.etiqueta_de_entrada.pack(side="left")
        self.entrada = tk.Entry(self.marco_de_entrada, width=30)
        self.entrada.pack(side="left")
        self.marco_de_entrada.pack(fill="x", padx=10, pady=10)

        # Crear botones
        self.marco_de_botones = tk.Frame(self.root)
        self.boton_de_añadir = tk.Button(self.marco_de_botones, text="Añadir Tarea", command=self.añadir_tarea)
        self.boton_de_añadir.pack(side="left")
        self.boton_de_completar = tk.Button(self.marco_de_botones, text="Marcar como Completada", command=self.completar_tarea)
         self.boton_de_completar.pack(side="left")
        self.boton_de_eliminar = tk.Button(self.marco_de_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_de_eliminar.pack(side="left")
        self.marco_de_botones.pack(fill="x", padx=10, pady=10)

        # Crear lista de tareas
        self.marco_de_lista_de_tareas = tk.Frame(self.root)
        self.etiqueta_de_lista_de_tareas = tk.Label(self.marco_de_lista_de_tareas, text="Lista de Tareas:")
        self.etiqueta_de_lista_de_tareas.pack(side="top")
        self.lista_de_tareas = tk.Listbox(self.marco_de_lista_de_tareas, width=40)
        self.lista_de_tareas.pack(side="left", fill="both", expand=True)
        self.marco_de_lista_de_tareas.pack(fill="both", expand=True, padx=10, pady=10)

        # Asignar manejadores de eventos
        self.entrada.bind("<Return>", self.añadir_tarea)
        self.lista_de_tareas.bind("<Double-1>", self.completar_tarea)

    def añadir_tarea(self, event=None):
        tarea = self.entrada.get()
        if tarea:
            self.tareas.append(tarea)
            self.lista_de_tareas.insert(tk.END, tarea)
            self.entrada.delete(0, tk.END)

    def completar_tarea(self, event=None):
        selección = self.lista_de_tareas.curselection()
        if selección:
            tarea = self.tareas[selección[0]]
            self.tareas[selección[0]] = f"[X] {tarea}"
            self.lista_de_tareas.delete(selección[0])
            self.lista_de_tareas.insert(selección[0], self.tareas[selección[0]])

    def eliminar_tarea(self):
        selección = self.lista_de_tareas.curselection()
        if selección:
            self.tareas.pop(selección[0])
            self.lista_de_tareas.delete(selección[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicaciónDeListaDeTareas(root)
    root.mainloop()
