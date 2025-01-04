from window import Window

from maze import Maze

def main():
    win = Window(800, 600)
    win.draw_line(10, 10, 500, 500)
    win.draw_box(30, 30, 50, 50, fill_colour="red")
    win.draw_box(130, 130, 160, 180, e = False, w = False, fill_colour="red")

    maze = Maze(20, 20, 50, 50, 20, 20, win)
    maze.cell_at(1, 1).e = False
    maze.draw()

    win.wait_for_close()

if __name__ == '__main__':
    main()
