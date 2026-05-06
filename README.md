# Data Cleaning and Visualization using Python

![Data Analysis Banner](https://img.shields.io/badge/Data%20Analysis-Project-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%23ffffff.svg?style=for-the-badge&logo=Seaborn&logoColor=black)

## 📌 Project Overview
This repository contains a complete, end-to-end data analysis project focusing on **Data Cleaning** and **Exploratory Data Analysis (EDA)**. The project analyzes a dirty real-world **Supermarket Sales Dataset** to uncover hidden trends, business insights, and handle common data issues like missing values, duplicates, and outliers.

This project is perfectly tailored for showcasing data analysis skills, suitable for internship submissions, college presentations (viva), and portfolio building.

## 🚀 Features
- **Data Collection & Generation**: Utilizes a raw retail dataset with injected real-world issues.
- **Data Preprocessing & Cleaning**: 
  - Identification and imputation of missing values
  - Removal of exact duplicate rows
  - Fixing wrong data types and inconsistent strings
- **Outlier Detection**: Using IQR and Boxplots to handle massive transaction anomalies.
- **Exploratory Data Analysis (EDA)**: Over 15 professional visualizations.
- **Business Insights & Conclusion**: Extracting KPIs, storytelling, and giving recommendations.

## 🛠️ Technologies Used
- **Language**: Python 3
- **Libraries**:
  - `pandas`: Data manipulation and cleaning
  - `numpy`: Numerical calculations
  - `matplotlib` & `seaborn`: Professional data visualization
  - `scipy` & `missingno`: Statistical testing and missing data visualization (Optional)
- **Environment**: Jupyter Notebook

## 📊 Dataset Information
- **Domain**: Retail / Supermarket Sales
- **Rows**: 1500+ records
- **Description**: Features include Branch, City, Customer type, Gender, Product line, Unit price, Total, Date, Time, and Customer Rating.
- **Issues Handled**: Missing values in Rating and Gender, Outliers in Total spending, String inconsistencies in City and Gender, Data type issues, Negative Quantities, and Duplicates.

## ⚙️ Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Data-Cleaning-Visualization.git
   cd Data-Cleaning-Visualization
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 How to Run the Project
1. Open up your terminal and run Jupyter Server:
   ```bash
   jupyter notebook
   ```
2. Open the main file: **`notebook.ipynb`**.
3. (Optional) Run the script **`generate_dataset.py`** to recreate the dirty dataset.
4. (Optional) You can also run the Python script version:
   ```bash
   python data_cleaning_eda.py
   ```

## 📈 Results & Visualizations
<p align="center">
  <i>(Include Screenshots from Notebook hereafter publishing to Github)</i><br>
  [Placeholder Snapshot 1: Missing Data Heatmap]<br>
  [Placeholder Snapshot 2: Correlation Heatmap]<br>
  [Placeholder Snapshot 3: Sales Distribution Dashboard]
</p>

## 🔮 Future Scope
- Build a Machine Learning model to predict customer ratings.
- Create an interactive Dashboard using Streamlit or PowerBI.
- Automate the ETL (Extract, Transform, Load) pipeline using Apache Airflow.

---
**Author:** *[Your Name]*  
*Data Science Intern | Aspiring Data Analyst*
