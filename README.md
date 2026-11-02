# iPhone AI Sensor Lab

**Human Activity Recognition using iPhone motion sensors and Machine Learning.**

An experimental AI project that explores how smartphone motion sensors can be used to recognize human activities through signal processing and machine learning.

## Project Overview

The goal of this project is to build a complete Human Activity Recognition (HAR) pipeline using real-world motion data collected from an iPhone.

The system uses:
- **Accelerometer:** measures acceleration along the X, Y and Z axes.
- **Gyroscope:** measures angular velocity around three axes.
- **Python:** processes and analyzes sensor data.
- **Machine Learning:** classifies physical activities based on extracted features.

## Architecture

```text
iPhone Motion Sensors
        |
        v
JavaScript Data Collection
        |
        v
      CSV Files
        |
        v
Signal Visualization
        |
        v
  Feature Extraction
        |
        v
  Machine Learning
        |
        v
Activity Classification
```

## Supported Activities

The initial classification targets are:

- Stationary
- Walking
- Running

## Technologies

| Technology | Purpose |
|---|---|
| Python | Data processing and ML |
| NumPy | Numerical computations |
| Pandas | Dataset manipulation |
| Matplotlib | Signal visualization |
| Scikit-learn | Machine learning |
| JavaScript | iPhone sensor acquisition |
| GitHub Pages | Hosting the data collector |

## Project Structure

```text
iphone-ai-sensor-lab/
│
├── data/
│   └── .gitkeep
│
├── docs/
│   └── index.html
│
├── notebooks/
│
├── src/
│   ├── generate_sensor_data.py
│   ├── extract_features.py
│   ├── train_model.py
│   └── visualize_sensor_data.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:haitamchouaibb/iphone-ai-sensor-lab.git
cd iphone-ai-sensor-lab
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate synthetic sensor data

```bash
python src/generate_sensor_data.py
```

### 5. Extract features

```bash
python src/extract_features.py
```

### 6. Train the baseline model

```bash
python src/train_model.py
```

## Current Progress

- [x] Synthetic motion dataset generation
- [x] Sensor signal feature extraction
- [x] Initial Random Forest classifier
- [x] Model evaluation
- [x] iPhone accelerometer data acquisition
- [x] iPhone gyroscope data acquisition
- [x] Sensor signal visualization
- [x] Activity-labelled CSV collector
- [ ] Real-world dataset collection
- [ ] Real-world model training and evaluation
- [ ] Model optimization
- [ ] Real-time activity recognition

## Current Limitations

The initial machine learning experiments use synthetic sensor data. The initial perfect classification results should not be interpreted as real-world performance.

Real-world data collection and model validation are still in progress.

The current browser-based sensor collector uses the DeviceMotion API and requires a compatible browser and sensor permissions.

## Future Goals

- Build a reliable real-world motion dataset.
- Investigate signal processing techniques.
- Compare different machine learning algorithms.
- Evaluate model generalization on unseen recordings.
- Explore real-time activity recognition.

## Author

**Haitam Chouaib**

Computer Engineering Student | Machine Learning & AI

GitHub: [@haitamchouaibb](https://github.com/haitamchouaibb)
