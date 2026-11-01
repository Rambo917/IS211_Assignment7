
import random
import argparse

random.seed(0)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points


class Die:
    def roll(self):
        return random.randint(1, 6)


class PigGame:
    def __init__(self, num_players=2):
        self.players = [
            Player("Player " + str(i + 1))
            for i in range(num_players)
        ]
        self.die = Die()
        self.current_player = 0

    def show_scores(self):
        print("\nCurrent Scores:")
        for player in self.players:
            print("{}: {}".format(player.name, player.score))

    def play_turn(self):
        player = self.players[self.current_player]
        turn_total = 0
        last_roll = None

        print("\n{}'s turn!".format(player.name))

        while True:
            print("\nLast roll: {}".format(
                last_roll if last_roll is not None else "None"
            ))
            print("Turn total:", turn_total)
            print("Total score:", player.score)

            choice = input("Roll (r) or Hold (h)? ").strip().lower()

            if choice == "r":
                last_roll = self.die.roll()
                print("{} rolled a {}".format(player.name, last_roll))

                if last_roll == 1:
                    print("Rolled a 1! No points earned this turn.")
                    print("Turn total: 0")
                    print("Total score:", player.score)
                    return

                turn_total += last_roll

                print("Turn total:", turn_total)
                print("Total score:", player.score)

            elif choice == "h":
                player.add_score(turn_total)
                print("{} holds and earns {} points.".format(
                    player.name, turn_total
                ))
                print("Turn total:", turn_total)
                print("Total score:", player.score)
                return

            else:
                print("Invalid choice. Please enter r or h.")

    def play(self):
        print("Welcome to Pig!")
        print("First player to reach 100 points wins!")

        while True:
            self.show_scores()
            self.play_turn()

            player = self.players[self.current_player]

            if player.score >= 100:
                self.show_scores()
                print("\n{} wins with {} points!".format(
                    player.name, player.score
                ))
                print("Game Over!")
                break

            self.current_player = (
                self.current_player + 1
            ) % len(self.players)


def main():
    parser = argparse.ArgumentParser(
        description="Play the Pig dice game."
    )

    parser.add_argument(
        "--numPlayers",
        type=int,
        default=2,
        help="Number of players (default: 2)"
    )

    args = parser.parse_args()

    if args.numPlayers < 2:
        parser.error("There must be at least 2 players.")

    game = PigGame(args.numPlayers)
    game.play()


if __name__ == "__main__":
    main()
