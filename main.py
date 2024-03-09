from players import Repeater, Fox, Acceptor, Cheater, PlayerGroup
from game_logging import logger
from config import REPEATER_NUM, FOX_NUM, ACCEPTOR_NUM, CHEATER_NUM


def main():
    players = PlayerGroup(
        [Repeater()] * REPEATER_NUM
        + [Fox()] * FOX_NUM
        + [Acceptor()] * ACCEPTOR_NUM
        + [Cheater()] * CHEATER_NUM
    )
    players.play_and_evolve(1)


if __name__ == "__main__":
    main()
