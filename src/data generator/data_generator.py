import tkinter as tk
from tkinter import colorchooser
from openpyxl import Workbook
import random
import os

dot_radius = 5  # Radius of each dot
dot_colors = ["#FF0000", "#00FF00", "#0000FF", "#FFA500", "#800080", "#FFFF00", "#FFC0CB", "#00FFFF", "#FF00FF", "#A52A2A"]

class Dot:
    def __init__(self, x, y, color_class):
        self.x = x
        self.y = y
        self.color_class = color_class

class DotGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()
        self.dots = []

        color_frame = tk.Frame(self.root)
        color_frame.pack(side=tk.TOP, padx=10)

        self.selected_color = tk.Label(color_frame, width=5, height=1, bg=dot_colors[0])
        self.selected_color.pack(pady=10)

        self.color_buttons = []
        for color in dot_colors:
            button = tk.Button(color_frame, bg=color, width=5, height=1, command=lambda c=color: self.select_color(c))
            button.pack(side=tk.LEFT, padx=2)
            self.color_buttons.append(button)

        self.canvas.bind("<Button-1>", self.place_cluster)
        self.canvas.bind("<Button-3>", self.cycle_color)

        # Set the range of the dot coordinates to match make_circles
        self.x_range = (-1, 1)
        self.y_range = (-1, 1)

        self.dot_distance = 0.03  # Distance between dots

    def place_cluster(self, event):
        x = event.x
        y = event.y

        color_class = dot_colors.index(self.selected_color["bg"])

        # Scale the dot coordinates to match the desired range
        dot_x = self.scale_coordinate(x, self.x_range[0], self.x_range[1])
        dot_y = self.scale_coordinate(y, self.y_range[0], self.y_range[1])

        for _ in range(10):
            dot_x += random.uniform(-self.dot_distance, self.dot_distance)  # Add small noise to the x-coordinate
            dot_y += random.uniform(-self.dot_distance, self.dot_distance)  # Add small noise to the y-coordinate

            # Unscale the dot coordinates to the canvas range
            canvas_x = self.unscale_coordinate(dot_x, self.x_range[0], self.x_range[1])
            canvas_y = self.unscale_coordinate(dot_y, self.y_range[0], self.y_range[1])

            self.canvas.create_oval(canvas_x - dot_radius, canvas_y - dot_radius,
                                    canvas_x + dot_radius, canvas_y + dot_radius, fill=dot_colors[color_class])

            self.dots.append(Dot(dot_x, dot_y, color_class))

    def cycle_color(self, event):
        current_color = self.selected_color["bg"]
        current_index = dot_colors.index(current_color)
        next_index = (current_index + 1) % len(dot_colors)
        self.selected_color["bg"] = dot_colors[next_index]

    def select_color(self, color):
        self.selected_color["bg"] = color

    def scale_coordinate(self, value, min_val, max_val):
        canvas_width = self.canvas.winfo_width()  # Get the current width of the canvas
        return (value / canvas_width) * (max_val - min_val) + min_val

    def unscale_coordinate(self, value, min_val, max_val):
        canvas_width = self.canvas.winfo_width()  # Get the current width of the canvas
        return (value - min_val) / (max_val - min_val) * canvas_width

    def save_to_excel(self):
        i = 1
        while os.path.exists(f"data/custom_data_{i}.xlsx"):
            i += 1

        filename = f"data/custom_data_{i}.xlsx"

        wb = Workbook()
        ws = wb.active
        ws.append(["X", "Y", "Color Class"])

        for dot in self.dots:
            scaled_x = self.scale_coordinate(dot.x, self.x_range[0], self.x_range[1])
            scaled_y = self.scale_coordinate(dot.y, self.y_range[0], self.y_range[1])
            ws.append([scaled_x, scaled_y, dot.color_class])

        wb.save(filename)
        print(f"Data saved to {filename}")


root = tk.Tk()
app = DotGeneratorApp(root)

save_button = tk.Button(root, text="Save to Excel", command=app.save_to_excel)
save_button.pack(pady=10)

root.mainloop()
