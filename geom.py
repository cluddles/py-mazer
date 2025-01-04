import collections

class Point(collections.namedtuple('Point', ('x', 'y'))):
    pass

class Line(collections.namedtuple('Line', ('start', 'end'))):
    @classmethod
    def of(cls, x1, y1, x2, y2):
        obj = cls.__new__(cls, Point(x1, y1), Point(x2, y2))
        super(Line, obj).__init__()
        return obj

    def draw(self, canvas, fill_colour="black"):
        canvas.create_line(
            self.start.x, self.start.y,
            self.end.x, self.end.y,
            fill = fill_colour,
            width = 2
        )

class Box:
    def __init__(self, topLeft, bottomRight, n=True, e=True, s=True, w=True):
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.n = n
        self.e = e
        self.s = s
        self.w = w

    def draw(self, canvas, fill_colour="black"):
        (x1, y1) = self.topLeft
        (x2, y2) = self.bottomRight
        if self.n:
            Line.of(x1, y1, x2, y1).draw(canvas, fill_colour)
        if self.e:
            Line.of(x2, y1, x2, y2).draw(canvas, fill_colour)
        if self.s:
            Line.of(x1, y2, x2, y2).draw(canvas, fill_colour)
        if self.w:
            Line.of(x1, y1, x1, y2).draw(canvas, fill_colour)
