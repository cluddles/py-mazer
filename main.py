from window import Window

from maze import Maze

def main():
    win = Window(800, 600)

    w = 32
    h = 23
    maze = Maze(w, h, 16, 16, 24, 24, win)
    maze.draw_all()

    maze.break_walls(0, 0)

    maze.draw_move(0, -1, 0, 0)
    maze.solve_dfs(0, 0, w-1, h-1)
    maze.draw_move(w-1, h-1, w-1, h)
    maze.animate()

    win.wait_for_close()

if __name__ == '__main__':
    main()
