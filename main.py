from players import Repeater, Fox, Acceptor, Cheater, PlayerGroup
from config import EvolutionStrategy


def generate_players(repeater_num, fox_num, acceptor_num, cheater_num):
    return PlayerGroup(
        [Repeater()] * repeater_num
        + [Fox()] * fox_num
        + [Acceptor()] * acceptor_num
        + [Cheater()] * cheater_num
    )


def main():
    players = generate_players(5, 5, 5, 5)
    players.play_and_evolve(10, EvolutionStrategy.OBSOLETE_LAST_ALL)


if __name__ == "__main__":
    main()
