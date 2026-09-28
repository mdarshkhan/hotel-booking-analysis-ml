# Hotel Booking Demand Analysis and Cancellation Study

A Python data-analysis project based on the Hotel Booking Demand dataset and the submitted SAC project report.

## Project overview

The project analyzes hotel booking behavior, cancellation patterns, guest/booking characteristics, and related trends. The report describes a dataset containing **119,390 bookings and 32 attributes**.

### Included analysis
- Data loading with Pandas
- Missing-value inspection and preprocessing
- Data-type conversion
- Hotel-type distribution
- Top-country booking analysis
- Lead-time distribution
- Cancellation-status analysis
- Numeric correlation analysis
- Hotel-wise stay-duration analysis
- Visualizations using Matplotlib and Seaborn

The academic report also describes cancellation prediction using Logistic Regression, Random Forest, and Gradient Boosting. The supplied PDF does not expose the complete model-training cells in readable form, so this repository does not fabricate those missing cells.

## Repository structure

```
hotel-booking-analysis-ml/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── hotel_booking_analysis.ipynb
├── src/
│   └── hotel_booking_analysis.py
├── data/
│   └── README.md
└── docs/
    └── Hotel_Booking_Project_Report.pdf
```

## Dataset

The code expects:

```
hotel_bookings.csv
```

Place the dataset in the project working directory or update the CSV path in the notebook/script. The raw dataset is not included in this repository.

## Installation

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
jupyter notebook
```

Open `notebooks/hotel_booking_analysis.ipynb`.

## Tech stack

Python • NumPy • Pandas • Matplotlib • Seaborn • PyCountry • Jupyter

## Academic project

**Title:** Hotel Booking (Data Set)  
**Program:** B.Tech – Information Technology  
**Institution:** CMR Engineering College  
**Project type:** SAC Project  
**Author:** Mohammed Arsh Khan  
**Guide:** Mrs. C. Madhuri

## Source note

This repository was prepared from the supplied 14-page academic project PDF. Selectable implementation code was preserved, while screenshot-only sections are documented rather than presented as reconstructed facts.
