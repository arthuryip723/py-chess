from steppable import Steppable

class King(Steppable):
    def __init__(self, color, board, pos):
        super(King, self).__init__(color, board, pos)

    def symbol(self):
        return u'\u2654' if self.color == "white" else u'\u265a'

    def _move_diffs(self):
        return [[-1, -1],
         [-1, 0],
         [-1, 1],
         [0, -1],
         [0, 1],
         [1, -1],
         [1, 0],
         [1, 1]]
