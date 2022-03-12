import numpy as np
import Blocks
import random
from time import time
import AI


score_per_rows_cleared = [0, 40, 100, 300, 1200]
full_piece_pool = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]


class Game:
    def __init__(self):
        self.state = np.empty(shape=(20, 10))
        self.state.fill(0)
        self.current_piece_pool = full_piece_pool.copy()
        self.current_piece = 0
        self.score = 0
        self.start_time = time()
        self.pieces_placed = 0
    def max_height(self):
        max_height = 0
        for x in range(10):
            for y in range(20):
                if self.state[y, x] == 1:
                    max_height = max(max_height, y)
        return max_height + 1

    def next_piece(self):
        if len(self.current_piece_pool) == 0:
            self.current_piece_pool = full_piece_pool.copy()
        random_piece = random.randint(0, len(self.current_piece_pool) - 1)
        self.current_piece = self.current_piece_pool[random_piece]
        del self.current_piece_pool[random_piece]
    def play(self, position, rotation):
        self.pieces_placed += 1
        self.state = Blocks.blocks[self.current_piece].drop_piece(position, self.max_height(), rotation, self.state)
        self.state, cleared_rows = Blocks.remove_rows(self.state)
        self.score += score_per_rows_cleared[cleared_rows]

    def is_lost(self):
        for x in range(10):
            if self.state[19, x] == 1:
                return True
        return False


def start_game(multipliers):
    game = Game()
    while True:
        game.next_piece()
        play = AI.find_best_play(game.max_height(), game.current_piece, game.state, multipliers)
        game.play(play.position, play.rotation)
        if game.is_lost():
            break
        # sleep(0.5)
    print()
    print("Game score:", game.score)
    print("Game length:", time() - game.start_time)
    print("Pieces placed:", game.pieces_placed)
    print("Pieces per second:", game.pieces_placed / (time() - game.start_time))
    return game.score
