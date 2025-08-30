# 🚕 Trip Fare Prediction Project

## 📌 Project Overview
This project is focused on predicting taxi trip fares using machine learning models.  
The dataset includes trip details such as distance, pickup/drop locations, and other features, which are used to train regression models.  

The final model is a *Random Forest Regressor*, which was selected after testing multiple algorithms.
---

## 📂 Project Structure

Tripfare_project/ │ ├── data/                  # Datasets (not uploaded due to size restrictions) │   └── trip_fare.csv │ ├── models/                # Saved ML models │   └── best_rf_model_compressed.pkl   # Compressed model (7.4 MB) │ ├── notebooks/             # Jupyter/Colab notebooks │   └── EDA_and_Model.ipynb │ ├── compress_model.py      # Script to compress the trained model ├── requirements.txt       # Python dependencies ├── app.py                 # Streamlit app for demo └── README.md              # Project documentation

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Nandhini10102/DS_TripFare.git
cd <repo-name>

2. Install Dependencies

pip install -r requirements.txt
3. Run the Streamlit App

streamlit run app.py


---
📊 Dataset

File: trip_fare.csv

Size: ~170 MB (not uploaded due to GitHub restrictions)

Contains trip-level information such as:

Pickup & Drop locations

Distance traveled

Passenger count

Trip duration

Fare amount



👉 Dataset can be provided on request or stored externally.


--

🤖 Machine Learning Models

Several models were trained & compared:

Linear Regression

Decision Tree Regressor

Random Forest Regressor ✅ (Best performer)

XGBoost Regressor (tested but higher complexity)


The Random Forest Regressor gave the best performance with the lowest RMSE.


---
📦 Model File

The final trained model is saved as:

best_rf_model_compressed.pkl (7.44 MB)


Due to GitHub web upload issues, the model file is hosted externally:

👉 Download Model File :https://1drv.ms/u/c/f8551963b5fb9305/EXyRtZ2UjS5IrWas7uPACDoBiQCEVfZnjGT4sJk7bMfrcQ?e=D5skp9

📈 Results

Best Model: Random Forest Regressor

Accuracy (R² Score): ~0.92

RMSE: ~2.1


The model accurately predicts fares with minimal error.


---

🎯 Key Features of the Project

Full EDA (Exploratory Data Analysis) performed on dataset

Feature engineering for improved accuracy

Trained multiple regression models & compared metrics

Final model compressed from 170 MB → 7.4 MB for easy storage

Streamlit dashboard for user-friendly visualization



---

🚀 How to Use

1. Download the dataset (trip_fare.csv) and place inside data/ folder.


2. Download the compressed model from the above link.


3. Run streamlit run app.py to launch the dashboard.




---

🙌 Acknowledgements

Dataset inspired from NYC Taxi Fare Prediction Dataset

Tools: Python, Pandas, Scikit-learn, Streamlit, Matplotlib



---

📝 Notes

Large files (trip_fare.csv and full models) are not uploaded due to GitHub restrictions.

They can be shared via Google Drive/OneDrive upon request.



---
