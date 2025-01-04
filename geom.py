import collections

class Point(collections.namedtuple('Point', ('x', 'y'))):
    pass

class Line(collections.namedtuple('Line', ('start', 'end'))):
    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.start.x, self.start.y,
            self.end.x, self.end.y,
            fill = fill_colour,
            width = 2
        )
