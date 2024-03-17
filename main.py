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
    title='common reward matrix'
)

# initial_ratios = [[round(random(), 2) for _ in range(5)] for _ in range(20)]
# initial_players = []
# final_results = []
# player_num = 30
# for ratio in initial_ratios:
#     repeater_num = int(player_num * ratio[0])
#     fox_num = int(player_num * ratio[1])
#     acceptor_num = int(player_num * ratio[2])
#     cheater_num = int(player_num * ratio[3])
#     detector_num = int(player_num * ratio[4])
#     initial_players.append([repeater_num, fox_num, acceptor_num, cheater_num, detector_num])

#     settings = GameSettings(
#         reward_matrix=common_reward_matrix,
#         times=10,
#         reset_points=True,
#         evolution_strategy=EvolutionStrategy.OBSOLETE_LAST,
#         evolution_num=5,
#     )

#     game = iter(
#         Game(
#             generate_players(
#                 repeater_num, fox_num, acceptor_num, cheater_num, detector_num
#             ),
#             game_settings=settings,
#         )
#     )

#     for _ in range(10):
#         next(game)

#     final_results.append(count_players(game.players))

# draw_initial_ratio_impact(initial_players, final_results, 5)

win_win_reward_matrix = RewardMatrix(
    self_win=3,
    self_lose=-1,
    opponent_win=3,
    opponent_lose=-1,   
    win_win=4,
    lose_lose=0,
    title='win-win encouraged'
)
lose_lose_reward_matrix = RewardMatrix(
    self_win=3,
    self_lose=-1,
    opponent_win=3,
    opponent_lose=-1,   
    win_win=2,
    lose_lose=-2,
    title='lose-lose punished'
)
reward_configs = [common_reward_matrix,win_win_reward_matrix,lose_lose_reward_matrix]
final_results = []
repeater_num, fox_num, acceptor_num, cheater_num, detector_num = 5, 5, 15, 20,5
for config in reward_configs:
    settings = GameSettings(
        reward_matrix=config,
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
    for _ in range(5):
        next(game)

    final_results.append(count_players(game.players))

draw_rounds_impact(reward_configs, final_results,1)

# rounds = list(range(1, 18, 2))
# evolution_data = []
# for round in rounds:
#     repeater_num, fox_num, acceptor_num, cheater_num, detector_num = 5, 5, 15, 5, 5

#     settings = GameSettings(
#         reward_matrix=common_reward_matrix,
#         times=round,
#         reset_points=True,
#         evolution_strategy=EvolutionStrategy.OBSOLETE_LAST,
#         evolution_num=5,
#     )

#     game = iter(
#         Game(
#             generate_players(
#                 repeater_num, fox_num, acceptor_num, cheater_num, detector_num
#             ),
#             game_settings=settings,
#         )
#     )

#     data = []
#     for _ in range(10):
#         data.append(count_players(game.players))
#         next(game)
#     evolution_data.append(data)

# draw_rounds_impact(rounds, evolution_data)

# # elimination_nums = [2, 5, 10]
# # final_results = []
# # for elim_num in elimination_nums:
# #     repeater_num, fox_num, acceptor_num, cheater_num, detector_num = 5, 5, 15, 5, 0

# #     settings = GameSettings(
# #         reward_matrix=RewardMatrix(
# #             self_win=3, self_lose=-1, opponent_win=3, opponent_lose=-1, win_win=2, lose_lose=0
# #         ),
# #         times=10,
# #         reset_points=True,
# #         evolution_strategy=EvolutionStrategy.OBSOLETE_LAST,
# #         evolution_num=elim_num,
# #     )

# #     game = iter(Game(
# #         generate_players(repeater_num, fox_num, acceptor_num, cheater_num, detector_num),
# #         game_settings=settings,
# #     ))

# #     for _ in range(6):
# #         next(game)

# #     final_results.append(count_players(game.players))

# # draw_elimination_impact(elimination_nums, final_results)
