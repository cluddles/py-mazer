import time

class Cell:
    def __init__(self):
        self.e = True
        self.s = True

class Maze:
    def __init__(self, num_cells_x, num_cells_y, x1, y1, cell_width, cell_height, win = None):
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.x1 = x1
        self.y1 = y1
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for _ in range(0, self.num_cells_y * self.num_cells_x):
            self._cells.append(Cell())

    def cell_at(self, cx, cy):
        return self._cells[cy * self.num_cells_x + cx]

    def cell_window_pos(self, cx, cy):
        return (self.x1 + cx * self.cell_width, self.y1 + cy * self.cell_height)

    def draw_cell(self, cx, cy):
        cell = self.cell_at(cx, cy)
        n = (cy == 0)
        w = (cx == 0)
        (x1, y1) = self.cell_window_pos(cx, cy)
        (x2, y2) = self.cell_window_pos(cx+1, cy+1)
        self.win.draw_box(x1, y1, x2, y2, n, cell.e, cell.s, w)

    def draw_move(self, cx1, cy1, cx2, cy2, undo=False):
        (x1, y1) = self.cell_window_pos(cx1, cy1)
        (x2, y2) = self.cell_window_pos(cx2, cy2)
        self.win.draw_line(
            x1 + self.cell_width/2, y1 + self.cell_height/2,
            x2 + self.cell_width/2, y2 + self.cell_height/2,
            fill_colour = "gray" if undo else "red")

    def draw(self):
        for cy in range(0, self.num_cells_y):
            for cx in range(0, self.num_cells_x):
                self.draw_cell(cx, cy)

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)
