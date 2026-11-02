import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

FREQUENCY = 50
DURATION = 10
N_RECORDINGS = 20

activities = {
    "stationary": (0.0, 0.05),
    "walking": (1.2, 1.8),
    "running": (2.0, 3.0)
}

all_data = []

for activity, parameters in activities.items():

    for recording in range(N_RECORDINGS):

        n_samples = FREQUENCY * DURATION
        time = np.arange(n_samples) / FREQUENCY

        if activity == "stationary":
            step_frequency = 0
            amplitude = rng.uniform(0.02, 0.08)
        else:
            step_frequency = rng.uniform(*parameters)
            amplitude = rng.uniform(
                0.6 if activity == "walking" else 1.2,
                1.0 if activity == "walking" else 1.8
            )

        phase = rng.uniform(0, 2 * np.pi)

        acc_x = amplitude * np.sin(
            2 * np.pi * step_frequency * time + phase
        )

        acc_y = amplitude * 0.5 * np.cos(
            2 * np.pi * step_frequency * time + phase
        )

        acc_z = 9.81 + amplitude * np.sin(
            2 * np.pi * step_frequency * time + phase
        )

        acc_x += rng.normal(0, 0.1, n_samples)
        acc_y += rng.normal(0, 0.1, n_samples)
        acc_z += rng.normal(0, 0.1, n_samples)

        data = pd.DataFrame({
            "timestamp": time,
            "acc_x": acc_x,
            "acc_y": acc_y,
            "acc_z": acc_z,
            "activity": activity,
            "recording_id": f"{activity}_{recording}"
        })

        all_data.append(data)

final_data = pd.concat(all_data, ignore_index=True)

final_data.to_csv("data/activity_data.csv", index=False)

print("Dataset generated!")
print(final_data.groupby("activity")["recording_id"].nunique())
print("Total measurements:", len(final_data))