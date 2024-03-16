from game_logging import logger
from headers import EvolutionStrategy
from random import choice


def single_round(self, opponent, game_settings):
    for _ in range(game_settings.times):
        a_put = self.next_choice()
        b_put = opponent.next_choice()

        logger.trace(
            f"A is a {self.__class__.__name__} and B is a {opponent.__class__.__name__}."
        )
        logger.trace(f"{a_put} {b_put}.", end=" ")
        if a_put and b_put:
            logger.trace("Both won.")
            self.points += game_settings.reward_matrix.win_win
            opponent.points += game_settings.reward_matrix.win_win
        elif not a_put and not b_put:
            logger.trace("Both cheated.")
            self.points += game_settings.reward_matrix.lose_lose
            opponent.points += game_settings.reward_matrix.lose_lose
        elif a_put:
            logger.trace("opponent won.")
            opponent.points += game_settings.reward_matrix.opponent_win
            self.points += game_settings.reward_matrix.self_lose
        elif b_put:
            logger.trace("self won.")
            self.points += game_settings.reward_matrix.self_win
            opponent.points += game_settings.reward_matrix.opponent_lose

        self.update_status(not b_put)
        opponent.update_status(not a_put)
        logger.trace(f"{self.points} {opponent.points}.\n")


class Game:
    def __init__(self, players, game_settings):
        self.players = players
        self.player_sum = len(players)
        self.game_settings = game_settings

    def count_players(self):
        types = set(p.__class__.__name__ for p in self.players)
        player_counts = {t: 0 for t in types}
        for player in self.players:
            player_counts[player.__class__.__name__] += 1
        return player_counts

    def show_players_numbers(self):
        player_counts = self.count_players()
        for type, num in player_counts.items():
            logger.info(f"{player_counts[type]} {type}")

    def show_points(self):
        for player in self.players:
            logger.info(f"{player.__class__.__name__} has {player.points} points.")

    def play_all(self):
        for p1_i in range(len(self.players)):
            for p2_i in range(p1_i + 1, len(self.players)):
                single_round(self.players[p1_i], self.players[p2_i], self.game_settings)
            # reset information about cheating
            for player in self.players:
                player.was_cheated = False
        self.sort()

    def __next__(self):
        self.play_and_evolve()

    def __iter__(self):
        self.round = 1
        return self

    def play_and_evolve(self):
        self.play_all()
        self.round += 1

        self.evolve()
        self.breed()

        if self.game_settings.reset_points:
            for player in self.players:
                player.points = 0

    def evolve(self):
        """Eliminate last players."""
        if self.game_settings.evolution_strategy == EvolutionStrategy.KEEP_BEST:
            return self.keep_best_evolve()
        elif self.game_settings.evolution_strategy == EvolutionStrategy.OBSOLETE_LAST:
            return self.obsolete_last_evolve()
        elif (
            self.game_settings.evolution_strategy == EvolutionStrategy.OBSOLETE_LAST_ALL
        ):
            return self.obsolete_last_all_evolve()
        else:
            raise ValueError(
                f"Unknown evolution strategy: {self.game_settings.evolution_strategy}"
            )

    def obsolete_last_all_evolve(self):
        last_point = self.players[-1].points
        highest_point = self.players[0].points
        # self.show_points()
        if last_point == highest_point:
            return False
        for player_i in range(len(self.players)):
            if self.players[player_i].points == last_point:
                self.players = self.players[:player_i]
                break
        return True

    def keep_best_evolve(self):
        """Keep best players and eliminate last players."""
        self.players = self.players[: self.game_settings.evolution_num]
        return True

    def obsolete_last_evolve(self):
        """Obsolete last players and eliminate last players."""
        self.players = self.players[: -self.game_settings.evolution_num]
        return True

    def breed(self):
        """Breed best players."""
        num = self.player_sum - len(self.players)

        highest_point = self.players[0].points
        best_players = set()
        for player in self.players:
            if player.points == highest_point:
                best_players.add(player.__class__)

        new_players = []
        each_num = num // len(best_players)
        for player_class in best_players:
            new_players.extend([player_class() for _ in range(each_num)])
        if num % len(best_players) != 0:
            new_players.extend(
                [choice(list(best_players))() for _ in range(num % len(best_players))]
            )

        self.players.extend(new_players)

    def sort(self):
        """Sort by points in descending order."""
        self.players.sort(key=lambda p: p.points, reverse=True)
