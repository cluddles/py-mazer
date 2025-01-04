from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Mazer"
        self.__canvas = Canvas(self.__root, bg="white", height = height, width = width)
        self.__canvas.pack()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, x1, y1, x2, y2, fill_colour="black"):
        self.__canvas.create_line(x1, y1, x2, y2, fill = fill_colour, width = 2)

    def draw_box(self, x1, y1, x2, y2, n=True, e=True, s=True, w=True, fill_colour="black"):
        if n:
            self.draw_line(x1, y1, x2, y1, fill_colour)
        if e:
            self.draw_line(x2, y1, x2, y2, fill_colour)
        if s:
            self.draw_line(x1, y2, x2, y2, fill_colour)
        if w:
            self.draw_line(x1, y1, x1, y2, fill_colour)
