from enum import Enum, auto


# game settings
class RewardMatrix:
    def __init__(
        self, self_win, self_lose, opponent_win, opponent_lose, win_win, lose_lose,title
    ):
        self.self_win = self_win
        self.self_lose = self_lose
        self.opponent_win = opponent_win
        self.opponent_lose = opponent_lose
        self.win_win = win_win
        self.lose_lose = lose_lose
        self.title = title


class GameSettings:
    def __init__(
        self, reward_matrix, times, reset_points, evolution_strategy, evolution_num
    ):
        self.reward_matrix = reward_matrix
        self.times = times
        self.reset_points = reset_points
        self.evolution_strategy = evolution_strategy
        self.evolution_num = evolution_num


# evolutioin settings
class EvolutionStrategy(Enum):
    KEEP_BEST = auto()
    OBSOLETE_LAST = auto()
    OBSOLETE_LAST_ALL = auto()
