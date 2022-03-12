import random


class Generation:
    def __init__(self):
        self.players = []
        for _ in range(16):
            self.players.append(Generation.random_player())

    def next_generation(self, scores):
        players_with_scores = []
        for i in range(16):
            players_with_scores.append((self.players[i], scores[i]))
        players_with_scores.sort(key=lambda player_with_score: player_with_score[1], reverse=True)
        new_players = []
        for i in range(10):
            new_players.append(players_with_scores[i][0])
        best_player = new_players[0].copy()
        for new_player in new_players:
            new_player[random.randint(0, 3)] += random.uniform(-0.2, 0.2)
        for _ in range(5):
            new_players.append(Generation.random_player())
        new_players.append(best_player)
        self.players = new_players


    @staticmethod
    def random_player():
        parameters = []
        for _ in range(4):
            parameters.append(random.uniform(-1, 1))
        return parameters
