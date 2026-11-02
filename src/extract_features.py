import numpy as np
import pandas as pd

data = pd.read_csv("data/activity_data.csv")

WINDOW_SIZE = 100
STEP_SIZE = 50

features = []

for recording_id, recording in data.groupby("recording_id"):

    recording = recording.reset_index(drop=True)

    for start in range(
        0,
        len(recording) - WINDOW_SIZE + 1,
        STEP_SIZE
    ):

        window = recording.iloc[start:start + WINDOW_SIZE]

        row = {}

        for axis in ["acc_x", "acc_y", "acc_z"]:

            values = window[axis].to_numpy()

            row[f"{axis}_mean"] = np.mean(values)
            row[f"{axis}_std"] = np.std(values)
            row[f"{axis}_min"] = np.min(values)
            row[f"{axis}_max"] = np.max(values)
            row[f"{axis}_rms"] = np.sqrt(np.mean(values ** 2))

        # Magnitude of acceleration
        magnitude = np.sqrt(
            window["acc_x"] ** 2 +
            window["acc_y"] ** 2 +
            window["acc_z"] ** 2
        )

        row["magnitude_mean"] = magnitude.mean()
        row["magnitude_std"] = magnitude.std()

        row["activity"] = window["activity"].iloc[0]
        row["recording_id"] = recording_id

        features.append(row)

feature_data = pd.DataFrame(features)

feature_data.to_csv(
    "data/features.csv",
    index=False
)

print("Feature extraction completed!")
print("Number of windows:", len(feature_data))
print(feature_data.head())