import Game
import MachineLearning
import concurrent.futures
import pickle


def main():
    generation = MachineLearning.Generation()
    generation_number = 0
    while True:
        number_of_generations = int(input("Input the number of generations you want: "))
        if number_of_generations == 0:
            break
        for _ in range(number_of_generations):
            generation_number += 1
            print()
            print("Current generation:", generation_number)
            print()

            with concurrent.futures.ProcessPoolExecutor() as executor:
                scores = list(executor.map(Game.start_game, generation.players))
                generation.next_generation(scores)
                with open("Training/best_player{}".format(generation_number), "wb") as file:
                    pickle.dump(generation.players[15], file)


if __name__ == "__main__":
    main()
