from enum import Enum, auto

# game settings
COST = 0
WIN_WIN = 2
ONE_WIN = 2
ONE_LOSS = 0
BOTH_LOSS = 0
RESET_POINTS = True


# evolutioin settings
class EvolutionStrategy(Enum):
    KEEP_BEST = auto()
    OBSOLETE_LAST = auto()
    OBSOLETE_LAST_ALL = auto()
