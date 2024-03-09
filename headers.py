from enum import Enum, auto


# game settings
class GameSettings:
    def __init__(
        self, cost, win_win, one_win, one_loss, both_loss, times, reset_points
    ):
        self.cost = cost
        self.win_win = win_win
        self.one_win = one_win
        self.one_loss = one_loss
        self.both_loss = both_loss
        self.times = times
        self.reset_points = reset_points


# evolutioin settings
class EvolutionStrategy(Enum):
    KEEP_BEST = auto()
    OBSOLETE_LAST = auto()
    OBSOLETE_LAST_ALL = auto()
