import tkinter as tk
from DrawType import *


class ResizableGrid:
    def __init__(self, master, color, frame_width = 600, frame_height = 600):
        self.master = master
        self.rows = 20
        self.cols = 20

        self.slider_num = tk.Scale(master, from_=1, to=50, orient="horizontal", label="Rows", command=self.update_grid)
        self.slider_num.pack(fill="x")
        self.slider_num.set(self.rows)
        self.slider_num.set(self.cols)
        self.cell_size = frame_height/self.rows

        self.grid_frame = tk.Frame(master, width=frame_width, height=frame_height, bg="white")
        self.grid_frame.pack(pady=20)

        self.canvas = tk.Canvas(self.grid_frame, width=frame_width, height=frame_height, bg="black")
        self.canvas.pack(fill="both", expand=True)

        self.grid_frame.bind("<Configure>", self.on_resize)

        self.create_grid()
        self.canvas.bind("<Button-1>", lambda event: self.on_click(color, self.sel_type(), event))



    def create_grid(self):
        self.canvas.delete("all")
        rect = 0
        self.rectangles = {}

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        cell_width = width / self.cols
        cell_height = cell_width
        self.cell_size = cell_width

        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * cell_width
                y1 = row * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                self.rectangles[(row, col)] = rect #!?

    def update_grid(self, value):
        self.rows = self.slider_num.get()
        self.cols = self.slider_num.get()
        print(self.rectangles)
        self.create_grid()

    def on_resize(self, event):
        self.create_grid()

    def on_click(self, color, sel_type, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if (row, col) in self.rectangles:
            current_color = self.canvas.itemcget(self.rectangles[(row, col)], "fill")
            if current_color == "white":
                new_color = color[sel_type]

                #some sort of list of coordinates as to what is written here
                #reikia rasti koordinates
            else:
                new_color = "white"
            self.canvas.itemconfig(self.rectangles[(row, col)], fill=new_color)

    def sel_type(self):
        return chk.get_type()


if __name__ == "__main__":
    window = tk.Tk()
    chk = SelectDrawType(window, stats)
    app = ResizableGrid(window, color)
    window.mainloop()
