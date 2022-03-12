import numpy as np


def remove_row(state, row):
    state = np.delete(state, row, axis=0)
    state = np.append(state, np.zeros((1, 10)), axis=0)
    return state


def remove_rows(state):
    to_remove = []
    for y in reversed(range(20)):
        full = True
        for x in range(10):
            if state[y, x] == 0:
                full = False
        if full:
            to_remove.append(y)
    for row in to_remove:
        state = remove_row(state, row)
    return state, len(to_remove)


class Piece:
    @staticmethod
    def rotate(positions):
        rotated_positions = positions.copy()
        for i in range(4):
            rotated_positions[i] = (rotated_positions[i][1], rotated_positions[i][0] * -1)
        return rotated_positions

    def __init__(self, rotations):
        self.rotations = rotations

    @staticmethod
    def generate_rotations(positions, number_of_rotations):
        rotations = []
        for i in range(number_of_rotations):
            rotations.append(positions)
            positions = Piece.rotate(positions)
        return Piece(rotations)

    def drop_piece(self, x, max_height, rotation, state):
        new_state = np.copy(state)
        y = min(max_height + 3, 19)
        positions = self.rotations[rotation]

        dropped = False
        while not dropped:
            y -= 1
            for position in positions:
                x_pos = position[0] + x
                y_pos = position[1] + y
                if x_pos < 0 or x_pos > 9 or y_pos > 19:
                    return None
                if y_pos == 0 or state[y_pos - 1, x_pos] == 1:
                    dropped = True
        for position in positions:
            x_pos = position[0] + x
            y_pos = position[1] + y
            new_state[y_pos, x_pos] = 1
        return new_state


green = Piece.generate_rotations([(0, 0), (-1, 0), (0, 1), (1, 1)], 2)
red = Piece.generate_rotations([(0, 0), (1, 0), (0, 1), (-1, 1)], 2)
orange = Piece.generate_rotations([(0, 0), (-1, 0), (1, 0), (1, 1)], 4)
dark_blue = Piece.generate_rotations([(0, 0), (1, 0), (-1, 0), (-1, 1)], 4)
yellow = Piece.generate_rotations([(0, 0), (1, 0), (0, 1), (1, 1)], 1)
magenta = Piece.generate_rotations([(0, 0), (-1, 0), (1, 0), (0, 1)], 4)
light_blue = Piece([[(0, 0), (-1, 0), (-2, 0), (1, 0)],
                    [(0, 0), (0, 1), (0, 2), (0, -1)]])
blocks = [green, red, orange, dark_blue, yellow, magenta, light_blue]
