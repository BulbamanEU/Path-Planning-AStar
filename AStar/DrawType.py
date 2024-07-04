from tkinter import *

class SelectDrawType():
    def __init__(self, master, stats):
        self.stats = stats
        self.master = master
        self.index = IntVar()
        self.draw_buttons()

    def add_stats(self, stat_add):
        self.stats.append(stat_add)

    def draw_buttons(self):
        for index in range(len(self.stats)):
            radiobutton = Radiobutton(self.master,
                                      text=self.stats[index],
                                      variable=self.index,
                                      value=index,
                                      command=self.get_type)
            radiobutton.pack()

    def get_type(self):
        selected_index = self.index.get()
        if selected_index == 0:
            pass
        elif selected_index == 1:
            pass
        elif selected_index == 2:
            pass
        else:
            pass

        return selected_index

stats = ["start", "end", "obstacles"]
color = ["green", "red", "grey"]
