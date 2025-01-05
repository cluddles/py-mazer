import time
import random

from geom import Point, Dir

class Cell:
    def __init__(self):
        self.e = True
        self.s = True

class Maze:
    def __init__(self, num_cells_x, num_cells_y, x1 = 0, y1 = 0, cell_width = 16, cell_height = 16, win = None, seed = 1):
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.x1 = x1
        self.y1 = y1
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        self._cells = []
        for _ in range(0, self.num_cells_y * self.num_cells_x):
            self._cells.append(Cell())

    def _cell_index(self, cx, cy):
        return cy * self.num_cells_x + cx

    def cell_at(self, cx, cy):
        return self._cells[self._cell_index(cx, cy)]

    def cell_draw_pos(self, cx, cy):
        return Point(self.x1 + cx * self.cell_width, self.y1 + cy * self.cell_height)

    def draw_cell(self, cx, cy):
        cell = self.cell_at(cx, cy)
        e = cell.e
        s = cell.s
        (x1, y1) = self.cell_draw_pos(cx, cy)
        (x2, y2) = self.cell_draw_pos(cx + 1, cy + 1)
        if e:
            self.win.draw_line(x2, y1, x2, y2)
        if s:
            self.win.draw_line(x1, y2, x2, y2)

    def redraw_cell(self, cx, cy):
        cell = self.cell_at(cx, cy)
        e = cell.e
        s = cell.s
        (x1, y1) = self.cell_draw_pos(cx, cy)
        (x2, y2) = self.cell_draw_pos(cx + 1, cy + 1)
        blank_col = "white"
        wall_col = "black"
        self.win.draw_line(x2, y1, x2, y2, fill_colour = wall_col if e else blank_col)
        self.win.draw_line(x1, y2, x2, y2, fill_colour = wall_col if s else blank_col)

    def draw_all(self):
        self.win.draw_line(self.x1, self.y1, self.x1 + self.num_cells_x * self.cell_width, self.y1)
        self.win.draw_line(self.x1, self.y1, self.x1, self.y1 + self.num_cells_y * self.cell_height)
        for cy in range(0, self.num_cells_y):
            for cx in range(0, self.num_cells_x):
                self.draw_cell(cx, cy)

    def draw_move(self, cx1, cy1, cx2, cy2, undo=False):
        (x1, y1) = self.cell_draw_pos(cx1, cy1)
        (x2, y2) = self.cell_draw_pos(cx2, cy2)
        hcw = self.cell_width / 2
        hch = self.cell_height / 2
        self.win.draw_line(x1 + hcw, y1 + hch, x2 + hcw, y2 + hch, fill_colour = "gray" if undo else "red")

    def animate(self, anim_delay = 0.005):
        self.win.redraw()
        time.sleep(anim_delay)

    def break_walls(self, cx, cy, visited = set(), anim_delay = 0.005):
        # Visit each point once
        visited.add(Point(cx, cy))
        # Determine valid neighbours that we can visit (don't check visited at this point)
        candidates = []
        if cx > 0:
            candidates.append(Dir.W)
        if cy > 0:
            candidates.append(Dir.N)
        if cx < self.num_cells_x - 1:
            candidates.append(Dir.E)
        if cy < self.num_cells_y - 1:
            candidates.append(Dir.S)
        # Randomly select a neighbour and, if unvisited, break wall between us and it
        # Then call this method for the neighbour
        while len(candidates) > 0:
            next_dir = random.choice(candidates)
            candidates.remove(next_dir)
            next = Point(cx + next_dir.value.x, cy + next_dir.value.y)
            if next not in visited:
                # Break walls in relevant cell (neighbour for N, W edges), and redraw
                if next_dir == Dir.E:
                    self.cell_at(cx, cy).e = False
                    self.redraw_cell(cx, cy)
                elif next_dir == Dir.S:
                    self.cell_at(cx, cy).s = False
                    self.redraw_cell(cx, cy)
                elif next_dir == Dir.W:
                    self.cell_at(cx-1, cy).e = False
                    self.redraw_cell(cx-1, cy)
                elif next_dir == Dir.N:
                    self.cell_at(cx, cy-1).s = False
                    self.redraw_cell(cx, cy-1)
                self.animate(anim_delay)
                (ncx, ncy) = next
                self.break_walls(ncx, ncy, visited, anim_delay)
