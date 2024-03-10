from players import Repeater, Fox, Acceptor, Cheater, PlayerGroup
from headers import EvolutionStrategy, GameSettings


def generate_players(repeater_num, fox_num, acceptor_num, cheater_num, game_settings):
    return PlayerGroup(
        [Repeater()] * repeater_num
        + [Fox()] * fox_num
        + [Acceptor()] * acceptor_num
        + [Cheater()] * cheater_num,
        game_settings,
    )


def main():
    common_settings = GameSettings(
        cost=0,
        win_win=5,
        one_loss=0,
        one_win=3,
        both_loss=0,
        times=5,
        reset_points=True,
    )
    players = generate_players(
        repeater_num=5,
        fox_num=5,
        acceptor_num=5,
        cheater_num=20,
        game_settings=common_settings,
    )
    players.play_and_evolve(10, EvolutionStrategy.OBSOLETE_LAST_ALL)


if __name__ == "__main__":
    main()
