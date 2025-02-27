from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Mazer")
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

