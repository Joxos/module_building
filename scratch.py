import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 假设数据
initial_ratios = np.array(
    [[0.1, 0.2, 0.3, 0.2, 0.2], [0.2, 0.1, 0.4, 0.2, 0.1], [0.3, 0.1, 0.1, 0.4, 0.1]]
)
reward_configs = np.array(
    [[3, -1, 3, -1, 2, 0], [4, -2, 4, -2, 1, -1], [5, 0, 5, 0, 3, -2]]
)
final_results = np.array(
    [[10, 20, 30, 25, 15], [15, 25, 20, 30, 10], [20, 15, 25, 25, 15]]
)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

X, Y = np.meshgrid(initial_ratios[:, 0], reward_configs[:, 0])
Z = np.broadcast_to(final_results[:, 0].reshape(3, 1), X.shape)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="viridis")
ax.set_xlabel("Initial Ratio (Repeater)")
ax.set_ylabel("Reward Config (Self Win)")
ax.set_zlabel("Final Result (Repeater)")
plt.show()
