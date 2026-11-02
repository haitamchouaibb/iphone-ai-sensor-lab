# iphone-ai-sensor-lab
An AI-powered iPhone sensor analysis and activity recognition project

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

### 2