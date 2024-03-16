import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl


def draw_reward_matrix(reward_matrix):
    # Define the choices and the result matrix
    self_choice = ["cooperate", "cheat"]
    opponent_choice = self_choice

    result = np.array(
        [[f"win-win ({reward_matrix[0, 0]})", "self-win"], ["self-lose", "both-lose"]]
    )

    # Create the plot
    fig, ax = plt.subplots()
    im = ax.imshow(reward_matrix)

    # Set axis labels
    ax.set_xlabel("Self's choice")
    ax.set_ylabel("Opponent's choice")

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(opponent_choice)), labels=opponent_choice)
    ax.set_yticks(np.arange(len(self_choice)), labels=self_choice)

    # Loop over data dimensions and create text annotations.
    for i in range(len(self_choice)):
        for j in range(len(opponent_choice)):
            text = ax.text(j, i, result[i, j], ha="center", va="center", color="w")

    ax.set_title("Game Result Matrix")
    fig.tight_layout()
    plt.show()


def show_game_results(results):
    player_kinds = ["Repeater", "Fox", "Acceptor", "Cheater", "Detector"]

    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps["RdYlGn"](np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(player_kinds, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(
            labels, widths, left=starts, height=0.5, label=colname, color=color
        )

        r, g, b, _ = color
        text_color = "white" if r * g * b < 0.5 else "darkgrey"
        ax.bar_label(rects, label_type="center", color=text_color)
    ax.legend(
        ncol=len(player_kinds),
        bbox_to_anchor=(0, 1),
        loc="lower left",
        fontsize="small",
    )

    plt.show()


# draw_reward_matrix(np.array([[3, 0], [5, 1]]))
