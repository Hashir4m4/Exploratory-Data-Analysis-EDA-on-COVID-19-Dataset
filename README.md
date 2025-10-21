# 🧠 Exploratory Data Analysis (EDA) on COVID-19 Dataset

This project performs **Exploratory Data Analysis (EDA)** on a sample COVID-19 dataset using Python.  
It demonstrates how to analyze, summarize, and visualize real-world data using **Pandas**, **Matplotlib**, and **Seaborn**.

---

## 📊 Project Overview
The script performs the following steps:
1. Loads COVID-19 sample data from a CSV file.
2. Converts the date column to datetime format.
3. Displays summary statistics and dataset information.
4. Calculates total confirmed cases per country.
5. Visualizes:
   - Total confirmed cases by country (bar chart)
   - Correlation heatmap for `Confirmed`, `Deaths`, `Recovered`, and `Active` cases.

---

## 🧰 Technologies Used
- **Python 3.x**
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## 📦 Installation & Setup

1. Clone this repository:
   ```bash
   git clone(https://github.com/Hashir4m4/Exploratory-Data-Analysis-EDA-on-COVID-19-Dataset.git)
   ```

2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn
   ```

3. Ensure your dataset is available at:
   ```
   data/covid_sample.csv
   ```

4. Run the analysis:
   ```bash
   python eda_analysis.py
   ```

---

## 📈 Output
The script generates:
- **Bar Chart** → Total confirmed cases by country  
- **Heatmap** → Correlation matrix between numerical features  

---

## 📁 Project Structure
```
├── eda_analysis.py         # Main analysis script
├── data/
│   └── covid_sample.csv    # Input dataset
└── README.md               # Project documentation
```

---

## ✨ Future Improvements
- Add more visualizations (trend over time, case distribution, etc.)
- Automate missing data handling and outlier detection
- Integrate interactive dashboards (e.g., Plotly, Dash)
