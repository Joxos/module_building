from headers import EvolutionStrategy, GameSettings, RewardMatrix
from game import Game
from random import random
from drawer import (
    draw_initial_ratio_impact,
    draw_reward_matrix_impact,
    draw_rounds_impact,
)
from utils import generate_players, count_players

common_reward_matrix = RewardMatrix(
    self_win=3,
    self_lose=-1,
    opponent_win=3,
    opponent_lose=-1,   
    win_win=2,
    lose_lose=0,
)

initial_ratios = [[round(random(), 2) for _ in range(5)] for _ in range(10)]
final_results = []
for ratio in initial_ratios:
    repeater_num = int(30 * ratio[0])
    fox_num = int(30 * ratio[1])
    acceptor_num = int(30 * ratio[2])
    cheater_num = int(30 * ratio[3])
    detector_num = int(30 * ratio[4])

    settings = GameSettings(
        reward_matrix=common_reward_matrix,
        times=10,
        reset_points=True,
        evolution_strategy=EvolutionStrategy.OBSOLETE_LAST,
        evolution_num=5,
    )

    game = iter(
        Game(
            generate_players(
                repeater_num, fox_num, acceptor_num, cheater_num, detector_num
            ),
            game_settings=settings,
        )
    )

    for _ in range(6):
        next(game)

    final_results.append(count_players(game.players))

draw_initial_ratio_impact(initial_ratios, final_results, 5)

reward_configs = [[3, -1, 3, -1, 2, 0], [4, -2, 4, -2, 1, -1], [5, 0, 5, 0, 3, -2]]
final_results = []
for config in reward_configs:
    repeater_num, fox_num, acceptor_num, cheater_num, detector_num = 5, 5, 15, 5, 0

    settings = GameSettings(
        reward_matrix=RewardMatrix(*config),
        times=10,
        reset_points=True,
        evolution_strategy=EvolutionStrategy.OBSOLETE_LAST,
        evolution_num=5,
    )

    game = iter(
        Game(
            generate_players(
                repeater_num, fox_num, acceptor_num, cheater_num, detector_num
            ),
            game_settings=settings,
        )
    )

    for _ in range(6):
        next(game)

    final_results.append(count_players(game.players))

draw_reward_matrix_impact(reward_configs, final_results)

rounds = [5, 10, 15]
evolution_data = []
for round in rounds:
    repeater_num, fox_num, acceptor_num, cheater_num, detector_num = 5, 5, 15, 5, 0

    settings = GameSettings(
        reward_matrix=common_reward_matrix,
        times=round,
        reset_points=True,
        evolution_strategy=EvolutionStrategy.OBSOLETE_LAST,
        evolution_num=5,
    )

    game = iter(
        Game(
            generate_players(
                repeater_num, fox_num, acceptor_num, cheater_num, detector_num
            ),
            game_settings=settings,
        )
    )

    data = []
    for _ in range(round + 1):
        data.append(count_players(game.players))
        next(game)
    evolution_data.append(data)

draw_rounds_impact(rounds, evolution_data)

# elimination_nums = [2, 5, 10]
# final_results = []
# for elim_num in elimination_nums:
#     repeater_num, fox_num, acceptor_num, cheater_num, detector_num = 5, 5, 15, 5, 0

#     settings = GameSettings(
#         reward_matrix=RewardMatrix(
#             self_win=3, self_lose=-1, opponent_win=3, opponent_lose=-1, win_win=2, lose_lose=0
#         ),
#         times=10,
#         reset_points=True,
#         evolution_strategy=EvolutionStrategy.OBSOLETE_LAST,
#         evolution_num=elim_num,
#     )

#     game = iter(Game(
#         generate_players(repeater_num, fox_num, acceptor_num, cheater_num, detector_num),
#         game_settings=settings,
#     ))

#     for _ in range(6):
#         next(game)

#     final_results.append(count_players(game.players))

# draw_elimination_impact(elimination_nums, final_results)
