from players import Repeater, Fox, Acceptor, Cheater, PlayerGroup
from game_logging import logger
from config import REPEATER_NUM, FOX_NUM, ACCEPTOR_NUM, CHEATER_NUM, EvolutionStrategy


def main():
    players = PlayerGroup(
        [Repeater()] * REPEATER_NUM
        + [Fox()] * FOX_NUM
        + [Acceptor()] * ACCEPTOR_NUM
        + [Cheater()] * CHEATER_NUM
    )
    players.play_and_evolve(10, EvolutionStrategy.OBSOLETE_LAST_ALL)


if __name__ == "__main__":
    main()
