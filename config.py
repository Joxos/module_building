from enum import Enum, auto

# game settings
COST = 0
WIN_WIN = 2
ONE_WIN = 2
BOTH_LOSS = 0

# player number settings
REPEATER_NUM = 5
FOX_NUM = 5
CHEATER_NUM = 5
ACCEPTOR_NUM = 5


# evolutioin settings
class EvolutionStrategy(Enum):
    KEEP_BEST = auto()
    OBSOLETE_LAST = auto()
    OBSOLETE_LAST_ALL = auto()
