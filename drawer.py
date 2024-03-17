import matplotlib.pyplot as plt
import numpy as np
import inspect


def draw_reward_matrix_impact(reward_configs, final_results, max_cols=3):
    total_plots = len(reward_configs)
    cols = min(total_plots, max_cols)
    rows = total_plots // cols + (total_plots % cols > 0)
    
    fig, axs = plt.subplots(rows, cols, figsize=(cols*5, rows*5), squeeze=False)
    
    for i, (config, result) in enumerate(zip(reward_configs, final_results)):
        ax = axs[i // cols, i % cols]
        ax.imshow(np.array(result).reshape(1, 5), cmap="hot")
        ax.set_xticks(np.arange(5))
        ax.set_xticklabels(["Repeater", "Fox", "Acceptor", "Cheater", "Detector"])
        ax.set_title(f"{config.title}")
        ax.set_yticks([])
        for j in range(0,5):
            ax.text(j,0,final_results[i][j],ha="center",va="center",color="green",size=14)
    
    for j in range(i + 1, rows * cols):
        fig.delaxes(axs[j // cols, j % cols])
    
    plt.tight_layout()
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


def draw_rounds_impact(rounds, evolution_data, max_cols=3):
    total_plots = len(rounds)
    cols = min(total_plots, max_cols)
    rows = total_plots // cols + (total_plots % cols > 0)
    
    fig, axs = plt.subplots(rows, cols, figsize=(cols*5, rows*5), squeeze=False)
    
    for i, (round, data) in enumerate(zip(rounds, evolution_data)):
        ax = axs[i // cols, i % cols]
        for j in range(5):
            ax.plot(range(10), [row[j] for row in data], label=["Repeater", "Fox", "Acceptor", "Cheater", "Detector"][j])
        ax.set_title(f"Rounds: {round}")
        ax.set_xlabel("Generation")
        ax.set_ylabel("Number of Players")
        ax.legend()
    
    for j in range(i + 1, rows * cols):
        fig.delaxes(axs[j // cols, j % cols])
    
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
