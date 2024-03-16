from game_logging import logger


class Player:
    def __init__(self):
        self.points = 0
        self.was_cheated = False

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

    def next_choice(self):
        if self.was_cheated:
            return False
        else:
            return True

    def update_status(self, was_cheated):
        if was_cheated:
            self.was_cheated = True
