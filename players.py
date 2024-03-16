from game_logging import logger


class Player:
    def __init__(self):
        self.points = 0
        self.was_cheated = False

    def next_choice(self):
        pass

    def update_status(self, cheated):
        self.was_cheated = cheated

    def reset(self):
        self.was_cheated = False


class Repeater(Player):
    """
    A repeater is a man who always repeats other's last choice.
    """

    def __init__(self):
        super().__init__()

    def next_choice(self):
        return not self.was_cheated


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

    def next_choice(self):
        return not self.was_cheated

    def update_status(self, cheated):
        if cheated:
            self.was_cheated = True


class Detector(Player):
    """
    A detector is a man who detects if the other player cheats and cheats if he hasn't been cheated before.
    """

    def __init__(self):
        super().__init__()
        self.initial_choice = [True, False, True, True]
        self.ever_cheated = False

    def next_choice(self):
        if self.initial_choice:
            return self.initial_choice.pop(0)
        elif self.ever_cheated:
            return not self.was_cheated
        else:
            return False

    def update_status(self, cheated):
        super().update_status(cheated)
        if cheated:
            self.ever_cheated = True

    def reset(self):
        super().reset()
        self.initial_choice = [True, False, True, True]
        self.ever_cheated = False
