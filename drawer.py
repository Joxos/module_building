import matplotlib.pyplot as plt
from players import Repeater, Fox, Acceptor, Cheater, Detector
import numpy as np


def draw_reward_matrix(reward_matrix):
    # Define the choices and the result matrix
    self_choice = ["cooperate", "cheat"]
    opponent_choice = self_choice

    result = np.array(
        [
            [f"win-win ({reward_matrix[0, 0]})", f"self-win ({reward_matrix[0, 1]})"],
            [
                f"self-lose ({reward_matrix[1, 0]})",
                f"both-lose ({reward_matrix[1, 1]})",
            ],
        ]
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
            labels, widths, left=starts, height=0.8, label=colname, color=color
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


def draw_initial_ratio_impact(initial_ratios, final_results, max_cols=3):
    labels = ["Repeater", "Fox", "Acceptor", "Cheater", "Detector"]

    total_plots = len(final_results)
    cols = min(total_plots, max_cols)
    rows = total_plots // cols + (total_plots % cols > 0)

    fig, axs = plt.subplots(rows, cols, figsize=(cols * 5, rows * 4), squeeze=False)

    for i, (initial, final) in enumerate(zip(initial_ratios, final_results)):
        ax = axs[i // cols, i % cols]
        ax.bar(labels, final, color=["C0", "C1", "C2", "C3", "C4"])
        ax.set_title(f"{initial}")

    for j in range(i + 1, rows * cols):
        fig.delaxes(axs[j // cols, j % cols])

    plt.tight_layout()
    plt.show()


def draw_reward_matrix_impact(reward_configs, final_results):
    fig, axs = plt.subplots(1, len(reward_configs), figsize=(15, 5))
    for i, (config, result) in enumerate(zip(reward_configs, final_results)):
        axs[i].imshow(np.array(result).reshape(1, 5), cmap="hot")
        axs[i].set_xticks(np.arange(5))
        axs[i].set_xticklabels(["Repeater", "Fox", "Acceptor", "Cheater", "Detector"])
        axs[i].set_title(f"Reward Config: {config}")
    plt.tight_layout()
    plt.show()


def draw_rounds_impact(rounds, evolution_data):
    labels = ["Repeater", "Fox", "Acceptor", "Cheater", "Detector"]
    fig, axs = plt.subplots(1, len(rounds), figsize=(15, 5))
    for i, (round, data) in enumerate(zip(rounds, evolution_data)):
        for j in range(5):
            axs[i].plot(range(round + 1), [row[j] for row in data], label=labels[j])
        axs[i].set_title(f"Rounds: {round}")
        axs[i].set_xlabel("Generation")
        axs[i].set_ylabel("Number of Players")
        axs[i].legend()
    plt.tight_layout()
    plt.show()


def draw_elimination_impact(elimination_nums, final_results):
    labels = ["Repeater", "Fox", "Acceptor", "Cheater", "Detector"]
    num_strategies = len(labels)
    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.6 / len(elimination_nums)
    index = np.arange(num_strategies)

    for i, (elim_num, result) in enumerate(zip(elimination_nums, final_results)):
        ax.bar(
            index + i * bar_width,
            result,
            bar_width,
            label=f"Elimination Number: {elim_num}",
        )

    ax.set_xticks(index + bar_width * (len(elimination_nums) - 1) / 2)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_title("Final Results with Different Elimination Numbers")
    ax.set_xlabel("Strategies")
    ax.set_ylabel("Number of Players")

    plt.tight_layout()
    plt.show()
