import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cells_x = 12
        num_cells_y = 10
        m1 = Maze(num_cells_x, num_cells_y)
        self.assertEqual(len(m1._cells), num_cells_x * num_cells_y)

    # Could write more tests but, y'know...

if __name__ == "__main__":
    unittest.main()
