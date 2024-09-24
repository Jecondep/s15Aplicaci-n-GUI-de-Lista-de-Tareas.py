
#1import tkinter as tk
2
3class AplicaciónDeListaDeTareas:
4    def __init__(self, root):
5        self.root = root
6        self.root.title("Lista de Tareas")
7        self.tareas = []
8
9        # Crear campo de entrada para nuevas tareas
10        self.marco_de_entrada = tk.Frame(self.root)
11        self.etiqueta_de_entrada = tk.Label(self.marco_de_entrada, text="Nueva Tarea:")
12        self.etiqueta_de_entrada.pack(side="left")
13        self.entrada = tk.Entry(self.marco_de_entrada, width=30)
14        self.entrada.pack(side="left")
15        self.marco_de_entrada.pack(fill="x", padx=10, pady=10)
16
17        # Crear botones
18        self.marco_de_botones = tk.Frame(self.root)
19        self.boton_de_añadir = tk.Button(self.marco_de_botones, text="Añadir Tarea", command=self.añadir_tarea)
20        self.boton_de_añadir.pack(side="left")
21        self.boton_de_completar = tk.Button(self.marco_de_botones, text="Marcar como Completada", command=self.completar_tarea)
22        self.boton_de_completar.pack(side="left")
23        self.boton_de_eliminar = tk.Button(self.marco_de_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
24        self.boton_de_eliminar.pack(side="left")
25        self.marco_de_botones.pack(fill="x", padx=10, pady=10)
26
27        # Crear lista de tareas
28        self.marco_de_lista_de_tareas = tk.Frame(self.root)
29        self.etiqueta_de_lista_de_tareas = tk.Label(self.marco_de_lista_de_tareas, text="Lista de Tareas:")
30        self.etiqueta_de_lista_de_tareas.pack(side="top")
31        self.lista_de_tareas = tk.Listbox(self.marco_de_lista_de_tareas, width=40)
32        self.lista_de_tareas.pack(side="left", fill="both", expand=True)
33        self.marco_de_lista_de_tareas.pack(fill="both", expand=True, padx=10, pady=10)
34
35        # Asignar manejadores de eventos
36        self.entrada.bind("<Return>", self.añadir_tarea)
37        self.lista_de_tareas.bind("<Double-1>", self.completar_tarea)
38
39    def añadir_tarea(self, event=None):
40        tarea = self.entrada.get()
41        if tarea:
42            self.tareas.append(tarea)
43            self.lista_de_tareas.insert(tk.END, tarea)
44            self.entrada.delete(0, tk.END)
45
46    def completar_tarea(self, event=None):
47        selección = self.lista_de_tareas.curselection()
48        if selección:
49            tarea = self.tareas[selección[0]]
50            self.tareas[selección[0]] = f"[X] {tarea}"
51            self.lista_de_tareas.delete(selección[0])
52            self.lista_de_tareas.insert(selección[0], self.tareas[selección[0]])
53
54    def eliminar_tarea(self):
55        selección = self.lista_de_tareas.curselection()
56        if selección:
57            self.tareas.pop(selección[0])
58            self.lista_de_tareas.delete(selección[0])
59
60if __name__ == "__main__":
61    root = tk.Tk()
62    app = AplicaciónDeListaDeTareas(root)
63    root.mainloop()
