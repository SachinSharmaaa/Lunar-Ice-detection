# Lunar Ice Detection using Chandrayaan-2 DFSAR Radar Data

## Overview

Lunar polar regions are considered one of the most promising locations for the presence of subsurface water ice. This project focuses on the detection and characterization of potential ice-rich regions in the Lunar South Pole using Chandrayaan-2 Dual Frequency Synthetic Aperture Radar (DFSAR) observations.

The objective is to process radar signals, identify anomalous reflections associated with subsurface ice deposits, rank potential landing sites, and generate mission-planning insights for future lunar exploration missions.

---

## Problem Statement

Detection and Characterization of Subsurface Ice in Lunar South Polar Regions using Chandrayaan-2 DFSAR Radar and Imagery Data for Landing Site and Rover Traverse Planning.

---

## Key Features

### Radar Signal Processing
- DFSAR radar data loading and preprocessing
- Noise reduction and signal normalization
- Radar reflection analysis

### Ice Candidate Detection
- Statistical anomaly detection
- Strong reflection extraction
- Potential ice-rich region identification

### Landing Site Analysis
- Landing site suitability ranking
- Ice probability scoring
- Candidate region prioritization

### Machine Learning Integration
- Ice probability modeling
- Classification-based candidate assessment
- Automated ranking pipeline

### Mission Planning
- Rover traverse planning
- Mission dashboard generation
- Final landing site recommendation

### DFSAR Binary Data Parsing
- OBS metadata parsing
- PRD radar signal extraction
- Binary radar waveform analysis

---

## Project Architecture

```text
Lunar-Ice-detection/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── check_data.py
│   ├── preprocess.py
│   ├── signal_histogram.py
│   ├── ice_candidates.py
│   ├── ice_probability.py
│   └── ice_probability_plot.py
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 01_radar_analysis.ipynb
│   ├── 02_landing_site_ranking.ipynb
│   ├── 03_ice_probability_model.ipynb
│   ├── 04_ml_based_ice_classifier.ipynb
│   ├── 05_final_landing_site_selection.ipynb
│   ├── 06_rover_traverse_planning.ipynb
│   ├── 07_results_dashboard.ipynb
│   ├── 08_project_summary.ipynb
│   ├── 09_dfsar_obs_parser.ipynb
│   ├── 10_dfsar_prd_parser.ipynb
│   ├── 11_lunar_ice_probability_map.ipynb
│   └── 12_mission_report_generator.ipynb
│
├── docs/
├── output/
├── README.md
└── requirements.txt
```

---

## Workflow

1. Data Acquisition
2. DFSAR Radar Processing
3. Signal Analysis
4. Ice Candidate Extraction
5. Landing Site Ranking
6. Ice Probability Modeling
7. Machine Learning Classification
8. Rover Traverse Planning
9. Probability Map Generation
10. Mission Report Generation

---

## Technologies Used

### Programming Languages
- Python

### Libraries
- NumPy
- Pandas
- Matplotlib
- Scikit-Learn

### Development Environment
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## Dataset

This project utilizes Chandrayaan-2 DFSAR radar observations.

### Data Types
- Calibrated Radar CSV Files
- OBS Metadata Files
- PRD Radar Signal Files

Due to size limitations, large radar files are excluded from this repository.

---

## Results

The system successfully:

- Processed DFSAR radar observations
- Extracted radar reflection signatures
- Identified potential ice candidate regions
- Generated landing site suitability rankings
- Produced lunar ice probability estimates
- Created mission planning outputs

---

## Future Improvements

- Deep Learning based ice detection
- Terrain hazard mapping
- Crater and slope analysis
- Lunar GIS visualization
- Chandrayaan-2 imagery integration
- Interactive web dashboard
- Real-time rover path optimization

---

## Applications

- Lunar Exploration Missions
- ISRO Mission Planning
- Landing Site Assessment
- Rover Navigation
- Resource Prospecting
- In-Situ Resource Utilization (ISRU)

---

## Author

**Sachin Sharma**

B.Tech Information Technology  
Artificial Intelligence & Machine Learning Enthusiast  
Computer Vision | Deep Learning | Space Technology

---

## License

This project is developed for research, educational, and academic purposes.

<img width="1920" height="1200" alt="vadim-sadovski-e9" src="https://github.com/user-attachments/assets/7cd11373-9fc3-474e-b814-a4ce86b381f8" />

