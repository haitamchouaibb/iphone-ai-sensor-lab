import pandas as pd
import matplotlib.pyplot as plt

# Load real iPhone sensor data
data = pd.read_csv("data/iphone_sensor_data.csv")

# Plot accelerometer
plt.figure(figsize=(12, 5))

plt.plot(data["timestamp"], data["acc_x"], label="X")
plt.plot(data["timestamp"], data["acc_y"], label="Y")
plt.plot(data["timestamp"], data["acc_z"], label="Z")

plt.title("iPhone Accelerometer")
plt.xlabel("Time (seconds)")
plt.ylabel("Acceleration (m/s²)")
plt.legend()
plt.grid()

plt.show()


# Plot gyroscope
plt.figure(figsize=(12, 5))

plt.plot(data["timestamp"], data["gyro_alpha"], label="Alpha")
plt.plot(data["timestamp"], data["gyro_beta"], label="Beta")
plt.plot(data["timestamp"], data["gyro_gamma"], label="Gamma")

plt.title("iPhone Gyroscope")
plt.xlabel("Time (seconds)")
plt.ylabel("Rotation rate (degrees/second)")
plt.legend()
plt.grid()

plt.show()