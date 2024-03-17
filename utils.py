from players import Repeater, Fox, Acceptor, Cheater, Detector


def generate_players(repeater_num, fox_num, acceptor_num, cheater_num, detector_num):
    players = []
    for i in range(repeater_num):
        players.append(Repeater())
    for i in range(fox_num):
        players.append(Fox())
    for i in range(acceptor_num):
        players.append(Acceptor())
    for i in range(cheater_num):
        players.append(Cheater())
    for i in range(detector_num):
        players.append(Detector())
    return players


def count_players(players):
    players_count = [0, 0, 0, 0, 0]
    for player in players:
        if isinstance(player, Repeater):
            players_count[0] += 1
        elif isinstance(player, Fox):
            players_count[1] += 1
        elif isinstance(player, Acceptor):
            players_count[2] += 1
        elif isinstance(player, Cheater):
            players_count[3] += 1
        elif isinstance(player, Detector):
            players_count[4] += 1
    return players_count
