import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/activity_data.csv")

activities = ["stationary", "walking", "running"]

fig, axes = plt.subplots(3, 1, figsize=(12, 10))

for ax, activity in zip(axes, activities):

    subset = data[data["activity"] == activity]

    ax.plot(subset["timestamp"], subset["acc_x"], label="X")
    ax.plot(subset["timestamp"], subset["acc_y"], label="Y")
    ax.plot(subset["timestamp"], subset["acc_z"], label="Z")

    ax.set_title(activity.capitalize())
    ax.set_ylabel("Acceleration (m/s²)")
    ax.legend()
    ax.grid()

axes[-1].set_xlabel("Time (seconds)")

plt.tight_layout()
plt.show()