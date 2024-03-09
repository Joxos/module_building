from config import (
    COST,
    WIN_WIN,
    ONE_WIN,
    ONE_LOSS,
    BOTH_LOSS,
    RESET_POINTS,
    EvolutionStrategy,
)
from game_logging import logger


class Player:
    def __init__(self):
        self.points = 0

    def next_choice(self):
        return True

    def update_status(self, cheated):
        pass


class Repeater(Player):
    """
    A repeater is a man who always repeats other's last choice.
    """

    def __init__(self):
        super().__init__()
        self.was_cheated = False

    def next_choice(self):
        if self.was_cheated:
            return False
        else:
            return True

    def update_status(self, cheated):
        self.was_cheated = cheated


class Cheater(Player):
    """
    A cheater is a man who always cheats.
    """

    def __init__(self):
        super().__init__()

    def next_choice(self):
        return False


class Acceptor(Player):
    """
    An acceptor is a man who never cheats.
    """

    def __init__(self):
        super().__init__()

    def next_choice(self):
        return True


class Fox(Player):
    """
    A fox is a man who cheats if has been cheated before.
    """

    def __init__(self):
        super().__init__()
        self.was_cheated = False

    def next_choice(self):
        if self.was_cheated:
            return False
        else:
            return True

    def update_status(self, was_cheated):
        if was_cheated:
            self.was_cheated = True


def coin_test(a: Player, b: Player, times=5):
    for _ in range(times):
        a_put = a.next_choice()
        b_put = b.next_choice()

        logger.trace(
            f"A is a {a.__class__.__name__} and B is a {b.__class__.__name__}."
        )
        logger.trace(f"A put {a_put} and B put {b_put}.", end=" ")
        a.points -= COST
        b.points -= COST
        if a_put and b_put:
            logger.trace("Both won.")
            a.points += WIN_WIN
            b.points += WIN_WIN
        elif not a_put and not b_put:
            logger.trace("Both cheated.")
            a.points += BOTH_LOSS
            b.points += BOTH_LOSS
        elif not a_put:
            logger.trace("A won.")
            a.points += ONE_WIN
            b.points += ONE_LOSS
        elif not b_put:
            logger.trace("B won.")
            b.points += ONE_WIN
            a.points += ONE_LOSS

        a.update_status(not b_put)
        b.update_status(not a_put)
        logger.trace(
            f"{a.__class__.__name__} has {a.points} points and {b.__class__.__name__} has {b.points} points.\n"
        )


class PlayerGroup:
    def __init__(self, players):
        self.players = players

    def show_points(self):
        types = set(p.__class__.__name__ for p in self.players)
        player_counts = {t: 0 for t in types}
        for player in self.players:
            player_counts[player.__class__.__name__] += 1
        for type in types:
            logger.info(f"{player_counts[type]} {type}")

    def play_all(self):
        for p1_i in range(len(self.players)):
            for p2_i in range(p1_i + 1, len(self.players)):
                coin_test(self.players[p1_i], self.players[p2_i])
        self.sort()

    def play_and_evolve(self, times, strategy, num=0):
        logger.info(f"Playing {times} rounds with evolution strategy {strategy}.")
        logger.info(f"Initial players:")
        self.show_points()
        print()
        for time in range(times):
            logger.info(f"Round {time+1} after evolution:")
            self.play_all()
            go_on = self.evolve(strategy, num)
            self.show_points()
            if RESET_POINTS:
                for player in self.players:
                    player.points = 0
            if not go_on:
                break

    def evolve(self, strategy, num=0):
        """Eliminate last players."""
        # if len(self.players) <= num:
        #     return False
        if strategy == EvolutionStrategy.KEEP_BEST:
            return self.keep_best_evolve(num)
        elif strategy == EvolutionStrategy.OBSOLETE_LAST:
            return self.obsolete_last_evolve(num)
        elif strategy == EvolutionStrategy.OBSOLETE_LAST_ALL:
            return self.obsolete_last_all_evolve()
        else:
            raise ValueError(f"Unknown evolution strategy: {strategy}")

    def obsolete_last_all_evolve(self):
        last_point = self.players[-1].points
        for player_i in range(len(self.players)):
            if self.players[player_i].points == last_point:
                start_i = player_i
                if start_i == 0:
                    return False
                self.players = self.players[:start_i]
                break
        return True

    def keep_best_evolve(self, keep_num):
        """Keep best players and eliminate last players."""
        self.players = self.players[:keep_num]
        return True

    def obsolete_last_evolve(self, obsolete_num):
        """Obsolete last players and eliminate last players."""
        self.players = self.players[:-obsolete_num]
        return True

    def sort(self):
        """Sort by points in descending order."""
        self.players.sort(key=lambda p: p.points, reverse=True)

    def add(self, player):
        self.players.append(player)

    def remove(self, player):
        self.players.remove(player)

    def __len__(self):
        return len(self.players)

    def __getitem__(self, index):
        return self.players[index]

    def __setitem__(self, index, value):
        self.players[index] = value

    def __delitem__(self, index):
        del self.players[index]

    def __iter__(self):
        return iter(self.players)

    def __reversed__(self):
        return reversed(self.players)

    def __contains__(self, item):
        return item in self.players

    def __str__(self):
        return str(self.players)

    def __repr__(self):
        return f"PlayerGroup({self.players})"
