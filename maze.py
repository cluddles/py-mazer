import time

class Cell:
    def __init__(self):
        self._e = True
        self._s = True

class Maze:
    def __init__(self, num_cells_x, num_cells_y, x1 = 0, y1 = 0, cell_width = 16, cell_height = 16, win = None):
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

    def cell_draw_pos(self, cx, cy):
        return (self.x1 + cx * self.cell_width, self.y1 + cy * self.cell_height)

    def draw_cell(self, cx, cy):
        cell = self.cell_at(cx, cy)
        # draw N/W edges only for top/left cells
        n = (cy == 0)
        w = (cx == 0)
        e = cell._e
        s = cell._s
        (x1, y1) = self.cell_draw_pos(cx, cy)
        (x2, y2) = self.cell_draw_pos(cx + 1, cy + 1)
        if n:
            self.win.draw_line(x1, y1, x2, y1)
        if e:
            self.win.draw_line(x2, y1, x2, y2)
        if s:
            self.win.draw_line(x1, y2, x2, y2)
        if w:
            self.win.draw_line(x1, y1, x1, y2)

    def draw_move(self, cx1, cy1, cx2, cy2, undo=False):
        (x1, y1) = self.cell_draw_pos(cx1, cy1)
        (x2, y2) = self.cell_draw_pos(cx2, cy2)
        hcw = self.cell_width / 2
        hch = self.cell_height / 2
        self.win.draw_line(x1 + hcw, y1 + hch, x2 + hcw, y2 + hch, fill_colour = "gray" if undo else "red")

    def draw_all_cells(self):
        for cy in range(0, self.num_cells_y):
            for cx in range(0, self.num_cells_x):
                self.draw_cell(cx, cy)

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)
