from window import Window

from maze import Maze

def main():
    win = Window(800, 600)
    win.draw_line(10, 10, 500, 500)

    maze = Maze(20, 20, 50, 50, 20, 20, win)
    maze.cell_at(1, 1).e = False
    maze.draw_all()

    maze.break_walls(0, 0)

    win.wait_for_close()

if __name__ == '__main__':
    main()
