import tkinter as tk
import json

# Dimensiones de la cuadrícula
ancho, alto = 10, 10
tamano_pixel = 20
coordenadas = []

# Crear la ventana de tkinter
root = tk.Tk()
root.title("Pixel Art")

# Crear un lienzo de tkinter
canvas = tk.Canvas(root, width=ancho * tamano_pixel, height=alto * tamano_pixel, bg="white")
canvas.pack()

# Función para dibujar un pixel
def dibujar_pixel(event):
    x, y = event.x // tamano_pixel, event.y // tamano_pixel
    if 0 <= x < ancho and 0 <= y < alto:
        color_actual = color.get()
        canvas.create_rectangle(x * tamano_pixel, y * tamano_pixel,
                                 (x + 1) * tamano_pixel, (y + 1) * tamano_pixel,
                                 fill=color_actual, outline="black")
        coordenadas.append({'x': x, 'y': y, 'color': color_actual})

# Configurar el evento de clic para dibujar
canvas.bind("<Button-1>", dibujar_pixel)

# Selección de color
color = tk.StringVar(value="black")
tk.Entry(root, textvariable=color).pack()

# Función para guardar las coordenadas
def guardar_coordenadas():
    with open("coordenadas.txt", "w") as f:
        json.dump(coordenadas, f)
    print("Coordenadas guardadas.")

# Función para cargar las coordenadas
def cargar_coordenadas():
    global coordenadas
    try:
        with open("coordenadas.txt", "r") as f:
            coordenadas = json.load(f)
        for pixel in coordenadas:
            canvas.create_rectangle(pixel['x'] * tamano_pixel, pixel['y'] * tamano_pixel,
                                    (pixel['x'] + 1) * tamano_pixel, (pixel['y'] + 1) * tamano_pixel,
                                    fill=pixel['color'], outline="black")
        print("Coordenadas cargadas.")
    except FileNotFoundError:
        print("No se encontró el archivo de coordenadas.")

# Botones para guardar y cargar
tk.Button(root, text="Guardar", command=guardar_coordenadas).pack()
tk.Button(root, text="Cargar", command=cargar_coordenadas).pack()

# Mostrar la ventana
root.mainloop()
