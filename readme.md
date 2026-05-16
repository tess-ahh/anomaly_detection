# 🚨 Credit Card Fraud Detection System

### *Advanced Anomaly Detection Using Machine Learning, Statistical Analysis, and MLflow*

---

## 📌 Project Overview

Financial fraud detection is one of the most critical applications of Machine Learning in the banking and cybersecurity industries.
This project presents a complete **Credit Card Fraud Detection System** designed to identify fraudulent transactions using a combination of:

* 📊 Statistical Outlier Detection
* 🤖 Machine Learning Algorithms
* 🧪 Experiment Tracking with MLflow
* 📈 Performance Evaluation & Visualization

The system compares multiple supervised and unsupervised learning algorithms to determine the most effective approach for anomaly detection.

---

# 🎯 Project Objectives

✔ Detect fraudulent credit card transactions
✔ Compare multiple anomaly detection algorithms
✔ Apply statistical analysis techniques for outlier detection
✔ Evaluate model performance using industry-standard metrics
✔ Track experiments and results using MLflow
✔ Select and deploy the best-performing model for prediction

---

# 🛠️ Tech Stack

| Technology           | Purpose                   |
| -------------------- | ------------------------- |
| Python               | Core Programming Language |
| Jupyter Notebook     | Model Development         |
| VS Code              | Development Environment   |
| Anaconda             | Environment Management    |
| MLflow               | Experiment Tracking       |
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
joblib
```

---

# 📂 Dataset Information

### Dataset Used

**Credit Card Fraud Detection Dataset**

The dataset contains anonymized credit card transaction records collected from European cardholders.

---

## 📊 Dataset Statistics

| Feature                 | Value             |
| ----------------------- | ----------------- |
| Total Transactions      | 284,807           |
| Total Features          | 31                |
| Fraudulent Transactions | Highly Imbalanced |
| Target Column           | `Class`           |

---

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
$z = \frac{x - \mu}{\sigma}$ 



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

# 🧠 Model Training Pipeline

The system follows a complete machine learning workflow:

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
Predict New Transactions


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

The project includes several visualizations for better analytical understanding:

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

# 🏆 Best Model Selection

After evaluating all models, the best-performing algorithm was selected based on:

* F1 Score
* Recall
* Precision
* Overall Fraud Detection Capability

The selected model was then used for final fraud prediction.

---

# 💾 Model Saving & Deployment Preparation

The final trained model and scaler were saved using `joblib`.

### Saved Files


best_model.pkl
scaler.pkl


These files enable:

* future predictions
* deployment in web applications
* real-time fraud detection systems

---

# 🔮 Future Enhancements

Potential future improvements include:

* 🌐 Streamlit/Flask Web Application
* ⚡ Real-Time Fraud Detection
* 🧠 Deep Learning Models
* ☁ Cloud Deployment
* 🔌 API Integration
* 📡 Live Transaction Monitoring
* 🎯 Hyperparameter Optimization

---

# 📌 Conclusion

This project successfully developed a comprehensive anomaly detection framework for credit card fraud detection using statistical methods and multiple machine learning algorithms.

The integration of MLflow enhanced experiment tracking, model comparison, and reproducibility, making the system scalable, professional, and aligned with real-world machine learning workflows.

The final system demonstrates how data science and machine learning can be effectively used to improve fraud detection accuracy and support intelligent financial security systems.

