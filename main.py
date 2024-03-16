from players import Repeater, Fox, Acceptor, Cheater, Detector
from headers import EvolutionStrategy, GameSettings, RewardMatrix
from game import Game
from drawer import show_game_results


def generate_players(repeater_num, fox_num, acceptor_num, cheater_num, detector_num):
    players = []

    for i in range(repeater_num):
        players.append(Repeater())
    for i in range(fox_num):
        players.append(Fox())
    for i in range(acceptor_num):
        players.append(Acceptor())
    for i in range(cheater_num):
        players.append(Cheater())
    for i in range(detector_num):
        players.append(Detector())

    return players


def count_players(players):
    players_count = [0, 0, 0, 0, 0]
    for player in players:
        if isinstance(player, Repeater):
            players_count[0] += 1
        elif isinstance(player, Fox):
            players_count[1] += 1
        elif isinstance(player, Acceptor):
            players_count[2] += 1
        elif isinstance(player, Cheater):
            players_count[3] += 1
        elif isinstance(player, Detector):
            players_count[4] += 1
    return players_count


def main():
    common_reward = RewardMatrix(
        self_win=3,
        self_lose=-1,
        opponent_win=3,
        opponent_lose=-1,
        win_win=2,
        lose_lose=0,
    )
    settings = GameSettings(
        reward_matrix=common_reward,
        times=10,
        reset_points=True,
        evolution_strategy=EvolutionStrategy.OBSOLETE_LAST,
        evolution_num=5,
    )
    game = iter(
        Game(
            generate_players(
                repeater_num=6, fox_num=5, acceptor_num=5, cheater_num=6, detector_num=3
            ),
            game_settings=settings,
        )
    )
    results = {}
    for _ in range(10):
        results[f"Round {_+1}"] = count_players(game.players)
        next(game)
    show_game_results(results)


if __name__ == "__main__":
    main()
