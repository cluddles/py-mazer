from window import Window

from geom import Point, Line, Box

def main():
    win = Window(800, 600)
    win.draw_line(Line.of(10, 10, 500, 500))
    win.draw_box(Box(Point(30, 30), Point(50, 50)), fill_colour="red")
    win.draw_box(Box(Point(130, 130), Point(160, 180), e = False, w = False), fill_colour="red")
    win.wait_for_close()

if __name__ == '__main__':
    main()
