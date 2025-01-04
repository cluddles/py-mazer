from window import Window

from geom import Point, Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(500, 500)), "black")
    win.wait_for_close()

if __name__ == '__main__':
    main()
