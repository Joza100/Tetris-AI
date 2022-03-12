from GameInteraction import GameInteraction
import AI
from time import sleep
import pickle


def main():
    with open( "Training/best_player9", "rb") as file:
        parameters = pickle.load(file)
    game_interaction = GameInteraction()
    game_interaction.find_next_piece()
    next_piece = game_interaction.next_piece
    started = False
    while True:
        game_interaction.find_next_piece()
        if next_piece != game_interaction.next_piece or started:
            started = True
            print("Playing.")
            current_piece = next_piece
            next_piece = game_interaction.next_piece
            game_interaction.find_game_state()
            best_play = AI.find_best_play(game_interaction.max_height, current_piece, game_interaction.state, parameters)
            if current_piece == 6:
                game_interaction.play(best_play.position - 1, best_play.rotation)
            else:
                game_interaction.play(best_play.position, best_play.rotation)
            print()
            sleep(0.02)


if __name__ == '__main__':
    main()
