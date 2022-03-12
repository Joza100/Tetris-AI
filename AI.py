import Blocks
import random


class Play:
    def __init__(self, position, rotation, score):
        self.position = position
        self.rotation = rotation
        self.score = score


def rows_removed_score(rows_removed):
    return 1 if rows_removed == 4 else -1


def buried_holes(max_height, new_state):
    holes = 0
    for y in range(0, max_height):
        for x in range(10):
            if new_state[y, x] == 0:
                for height in range(y, max_height):
                    if new_state[height, x] == 1:
                        holes += 1
    return holes


def count_holes(max_height, new_state):
    holes = 0
    for y in range(0, max_height):
        for x in range(10):
            if new_state[y, x] == 0:
                for height in range(y, max_height):
                    if new_state[height, x] == 1:
                        holes += 1
                        break
    return holes


def height_difference(new_state):
    heights = []
    for x in range(10):
        height = 0
        for y in range(20):
            if new_state[y, x] == 1:
                height = y
        heights.append(height)
    difference = 0
    for i in range(9):
        difference += abs(heights[i] - heights[i + 1])
    return difference


def find_best_play(max_height, current_piece, state, multipliers):
    # print("Current piece: ", current_piece)
    current_piece = Blocks.blocks[current_piece]
    plays = []

    for x in range(10):
        for rotation in range(len(current_piece.rotations)):
            new_state = current_piece.drop_piece(x, max_height, rotation, state)
            if new_state is None:
                # print("Broken play: ", x, " ", rotation)
                continue
            remove_rows = Blocks.remove_rows(new_state)
            new_state = remove_rows[0]
            rows_removed = remove_rows[1]
            holes = count_holes(min(max_height + 3, 19), new_state)
            buried = buried_holes(min(max_height + 3, 19), new_state)
            height_diff = height_difference(new_state)
            score = rows_removed_score(rows_removed) * multipliers[0] + holes * multipliers[1] * -1 +\
                buried * multipliers[2] * -1 + height_diff * multipliers[3] * -1
            plays.append(Play(x, rotation, score))

    best_play = plays[0]
    # print("All possible plays: ")
    # print("Score Position Rotation")
    for play in plays:
        # print(play.score, " ", play.position, " ", play.rotation)
        if play.score > best_play.score:
            best_play = play
        elif play.score == best_play.score:
            best_play = random.choice([play, best_play])
    # print("Best play: ")
    # print(best_play.score)
    # print(best_play.position)
    # print(best_play.rotation)
    return best_play
