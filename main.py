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
    players = generate_players(
        repeater_num=1,
        fox_num=1,
        acceptor_num=1,
        cheater_num=2,
        game_settings=GameSettings(
            cost=1,
            win_win=3,
            one_loss=-3,
            one_win=5,
            both_loss=-2,
            times=5,
            reset_points=True,
        ),
    )
    players.play_and_evolve(10, EvolutionStrategy.OBSOLETE_LAST_ALL)


if __name__ == "__main__":
    main()
