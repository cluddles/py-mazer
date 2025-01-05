from window import Window

from maze import Maze

def main():
    win = Window(800, 600)

    maze = Maze(20, 20, 50, 50, 20, 20, win)
    maze.draw_all()
    maze.break_walls(0, 0)

    win.wait_for_close()

if __name__ == '__main__':
    main()
