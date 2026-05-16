# 🚨 Credit Card Fraud Detection System

### *Advanced Anomaly Detection Using Machine Learning, Statistical Analysis, MLflow, and Streamlit*

---

# 🌐 Live Web Application

## 🔗 Public Deployment

🚀 **Try the Live Fraud Detection App Here:**

[Credit Card Fraud Detection Web App](https://anomalydetection-qxwfshrb2rrqsygnv84njz.streamlit.app/)

The application is publicly deployed using Streamlit Community Cloud and supports real-time fraud prediction.

---

# 📌 Project Overview

This project presents a complete **Credit Card Fraud Detection System** designed to identify fraudulent transactions using:

* 📊 Statistical Analysis Techniques
* 🤖 Machine Learning Algorithms
* 🧪 MLflow Experiment Tracking
* 🌐 Streamlit Web Application
* 📈 Performance Evaluation & Visualization

The system compares multiple machine learning and anomaly detection algorithms to identify the most effective approach for fraud detection.

The final trained model is integrated into an interactive web application that enables users to perform real-time fraud prediction.

---

# 🎯 Project Objectives

✔ Detect fraudulent credit card transactions
✔ Compare multiple machine learning algorithms
✔ Apply statistical outlier detection techniques
✔ Evaluate model performance using multiple metrics
✔ Track experiments using MLflow
✔ Select the best-performing model
✔ Build and deploy an interactive fraud prediction web application

---

# 🛠️ Tech Stack

| Technology           | Purpose                   |
| -------------------- | ------------------------- |
| Python               | Core Programming Language |
| Jupyter Notebook     | Model Development         |
| VS Code              | Development Environment   |
| Anaconda             | Environment Management    |
| MLflow               | Experiment Tracking       |
| Streamlit            | Web Application Framework |
| Scikit-learn         | Machine Learning          |
| Matplotlib & Seaborn | Data Visualization        |

---

# 📚 Libraries Used

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
mlflow
streamlit
joblib
```

---

# 📂 Dataset Information

### Dataset Used

**Credit Card Fraud Detection Dataset**

The dataset contains anonymized credit card transaction records collected from European cardholders.
dataset is from kaggle. You can download it from here:"https://www.kaggle.com/code/annastasy/anomaly-detection-credit-card-fraud/input"

---


## 📊 Dataset Statistics

| Feature                 | Value             |
| ----------------------- | ----------------- |
| Total Transactions      | 284,807           |
| Total Features          | 31                |
| Fraudulent Transactions | Highly Imbalanced |
| Target Column           | `Class`           |

---
more dataset information in Dataset_Document.pdf

## 🎯 Target Labels

| Label | Description            |
| ----- | ---------------------- |
| `0`   | Normal Transaction     |
| `1`   | Fraudulent Transaction |

---

# 🧹 Data Preprocessing

The dataset underwent several preprocessing stages before training:

* ✔ Missing value handling
* ✔ Data cleaning
* ✔ Feature-target separation
* ✔ Numerical feature extraction
* ✔ Feature scaling using StandardScaler

---

# 📈 Statistical Analysis Techniques

To strengthen anomaly detection capability, statistical outlier detection methods were implemented.

---

## 🔹 Z-Score Analysis

Used to detect extreme deviations from the mean.

Formula:

$$ z = \frac{x - \mu}{\sigma} $$

### Purpose

* Detect statistical anomalies
* Identify unusually distributed transaction patterns

---

## 🔹 IQR (Interquartile Range) Method

Used for identifying outliers using quartile boundaries.

Formula:

IQR = Q_3 - Q_1

### Purpose

* Robust outlier detection
* Detection of abnormal transaction distributions

---

# 🤖 Machine Learning Algorithms Implemented

Multiple algorithms were trained and compared to identify the best-performing fraud detection model.

| Algorithm                  | Category                       |
| -------------------------- | ------------------------------ |
| Logistic Regression        | Supervised Learning            |
| Random Forest              | Ensemble Learning              |
| Isolation Forest           | Unsupervised Anomaly Detection |
| Local Outlier Factor (LOF) | Density-Based Detection        |
| One-Class SVM              | Boundary-Based Detection       |
| DBSCAN                     | Clustering-Based Detection     |

---

# 🧠 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Statistical Analysis
(Z-Score + IQR)
   ↓
Feature Scaling
   ↓
Train Multiple Models
   ↓
MLflow Experiment Tracking
   ↓
Performance Evaluation
   ↓
Algorithm Comparison
   ↓
Best Model Selection
   ↓
Save Trained Model
   ↓
Streamlit Web Application
   ↓
Real-Time Fraud Prediction
```

---

# 📊 Model Evaluation Metrics

The algorithms were evaluated using multiple performance metrics:

| Metric           | Purpose                            |
| ---------------- | ---------------------------------- |
| Accuracy         | Overall prediction correctness     |
| Precision        | Fraud prediction quality           |
| Recall           | Ability to detect fraud            |
| F1 Score         | Balance between precision & recall |
| ROC-AUC Score    | Classification performance         |
| Confusion Matrix | Detailed prediction analysis       |

---

# 📉 Data Visualization

The project includes several visualizations for analytical understanding:

* 📌 Scatter Plot Visualization
* 📌 Algorithm Comparison Graphs
* 📌 Confusion Matrix
* 📌 ROC Curve Analysis
* 📌 Anomaly Distribution Analysis

---

# 🧪 MLflow Integration

MLflow was integrated to create a professional experiment tracking environment.

---

## 🔍 MLflow Features Used

✔ Experiment Tracking
✔ Metric Logging
✔ Model Comparison
✔ Run Management
✔ Performance Monitoring

Each algorithm was logged as a separate experiment run for efficient comparison and reproducibility.

---

# 🌐 Streamlit Web Application

The project includes an interactive web application built using Streamlit.

---

## 🚀 Web App Features

✔ Real-Time Fraud Prediction
✔ User-Friendly Interface
✔ Interactive Input System
✔ Fraud Detection Alerts
✔ Trained ML Model Integration
✔ Public Cloud Deployment

---

# 💾 Model Saving & Deployment

The final trained model and scaler were saved using `joblib`.

### Saved Files

```text
best_model.pkl
scaler.pkl
```

The application was deployed publicly using Streamlit Community Cloud.

---

# 📁 Project Structure

```text
anomaly_detection/
│
├── app.py
├── best_model.pkl
├── scaler.pkl
├── creditcard.csv
├── requirements.txt
├── README.md
├── notebooks/
├── mlruns/
└── results/
```

---

# ▶️ Running the Project Locally

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 2: Run the Streamlit Application

```bash
streamlit run app.py
```

---

## Step 3: Open in Browser

```text
http://localhost:8501
```

---

# 🏆 Best Model Selection

After evaluating all models, the best-performing algorithm was selected based on:

* F1 Score
* Recall
* Precision
* Overall Fraud Detection Capability

The selected model was then used for final fraud prediction.

---

# 🔮 Future Enhancements

Potential future improvements include:

* ☁ Cloud Deployment
* 📡 Real-Time Transaction Monitoring
* 🧠 Deep Learning Models
* 🔌 API Integration
* 📱 Mobile Application Support
* ⚡ Advanced Hyperparameter Optimization

---

# 📌 Conclusion

This project successfully developed a comprehensive anomaly detection framework for credit card fraud detection using statistical methods and multiple machine learning algorithms.

The integration of MLflow enhanced experiment tracking, model comparison, and reproducibility, while Streamlit transformed the machine learning pipeline into an interactive real-time web application.

The final system demonstrates how machine learning can be effectively used to improve fraud detection accuracy and support intelligent financial security systems.

---


