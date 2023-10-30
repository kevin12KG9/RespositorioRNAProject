import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

window = tk.Tk()
window.title("Resultados")

bar_graph_frame = tk.Frame(window)
bar_graph_frame.pack(side="top")

x = np.arange(5)
y = np.random.randint(10, 100, 5)

fig = plt.figure(figsize=(5, 4))
plt.bar(x, y)
plt.xlabel("Tempo en semanas")
plt.ylabel("Ventas")
plt.title("Bar Graph")

canvas = FigureCanvasTkAgg(fig, master=bar_graph_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

table_frame = tk.Frame(window)
table_frame.pack(side="top")

table = tk.LabelFrame(table_frame, text="Table", padx=10, pady=10)
table.pack(side="top")

table.grid(row=0, column=0, padx=10, pady=10)

tk.Label(table, text="Tiempo").grid(row=0, column=0)
tk.Label(table, text="Ventas").grid(row=0, column=1)

table_values = [("1", "25"), ("2", "30"), ("2", "35")]

for i, (name, age) in enumerate(table_values, start=1):
    tk.Label(table, text=name).grid(row=i, column=0)
    tk.Label(table, text=age).grid(row=i, column=1)

button1 = tk.Button(window, text="Consulta")
button1.pack(side="left")

button2 = tk.Button(window, text="Guardar")
button2.pack(side="left")

button3 = tk.Button(window, text="Mostrar grafica")
button3.pack(side="left")

button4 = tk.Button(window, text="Mostrar tabla")
button4.pack(side="left")

window.mainloop()
