# 🧠 SegmentIQ — Customer Segmentation & Predictive Analytics System

An end-to-end Machine Learning application for **customer segmentation and customer segment prediction**, built using clustering and classification techniques and deployed as a containerized web application.

The system analyzes customer demographics and purchasing behavior, discovers meaningful customer groups using unsupervised learning, and predicts the segment of new customers using a trained classification model.

---

## 🌐 Live Application

🚀 **SegmentIQ is deployed and publicly accessible on Render:**

👉 https://segmentiq-qyte.onrender.com

> **Note:** The application is hosted on a Render free instance. If the service has been inactive, the first request may take some time while the instance starts.

---

## 📌 Problem Statement

Businesses such as retail stores and e-commerce platforms interact with customers having different purchasing behaviors, spending capacities, demographics, and engagement patterns.

Treating every customer in the same way can lead to ineffective marketing strategies.

**SegmentIQ** addresses this problem by:

1. Discovering meaningful customer groups using **unsupervised machine learning**.
2. Training a **supervised classification model** to predict the segment of new customers.
3. Providing predictions through an interactive web interface.

This can help businesses better understand their customers and design more targeted marketing and engagement strategies.

---

## 💡 Solution Overview

The project follows a two-stage Machine Learning approach:

### 1️⃣ Customer Segmentation — Unsupervised Learning

Multiple clustering algorithms were explored and evaluated:

- K-Means Clustering
- Agglomerative Clustering
- Gaussian Mixture Model (GMM)
- DBSCAN

The clustering performance was analyzed using techniques such as the **Elbow Method** and **Silhouette Score**.

For K-Means, the following silhouette scores were obtained:

| Number of Clusters | Silhouette Score |
| ------------------ | ---------------- |
| 3 | **0.5105** |
| 4 | 0.4575 |
| 5 | 0.4336 |
| 6 | 0.3910 |

Based on the clustering experiments and evaluation, **K-Means with 3 clusters** was selected for the final segmentation pipeline.

PCA was also used to reduce dimensionality for visualization of the customer clusters.

---

### 2️⃣ Customer Segment Prediction — Supervised Learning

After generating customer cluster labels, multiple classification algorithms were trained and compared to predict the segment of new customers.

### Classification Model Comparison — Before Hyperparameter Tuning

| Model | Accuracy |
| ----- | -------: |
| K-Nearest Neighbors | 81.25% |
| Logistic Regression | 87.72% |
| AdaBoost Classifier | 90.18% |
| Decision Tree | 94.42% |
| Random Forest | 95.98% |
| Gradient Boosting | 96.21% |
| **XGBoost Classifier** | **96.43%** |

**XGBoost achieved the highest accuracy (~96.43%)** among the evaluated classification models and was selected for further optimization.

---

## ⚙️ XGBoost Hyperparameter Tuning

After selecting XGBoost, **GridSearchCV with 5-fold cross-validation** was used to search for the best combination of hyperparameters.

The following parameter grid was evaluated:

```python
params = {
    "n_estimators": [100, 200, 300],
    "max_depth": [3, 5, 7],
    "learning_rate": [0.01, 0.05, 0.1],
    "subsample": [0.8, 1],
    "colsample_bytree": [0.8, 1]
}
```

The best parameters identified by GridSearchCV were then used to train the final XGBoost model.

---

## 📊 Model Evaluation

Before hyperparameter tuning, the selected XGBoost classifier achieved approximately:

- **Accuracy:** 96.43%
- **Macro Precision:** 0.96
- **Macro Recall:** 0.96
- **Macro F1-Score:** 0.96
- **Weighted Precision:** 0.96
- **Weighted Recall:** 0.96
- **Weighted F1-Score:** 0.96

The model was also evaluated using a **classification report and confusion matrix** to analyze prediction performance across all three customer segments.

> **Note:** The 96.43% model comparison result corresponds to the XGBoost model evaluated before GridSearchCV hyperparameter tuning.

---

## 🎯 Output Includes

For a new customer profile, the application provides:

- Customer Segment / Category
- Cluster ID
- Business Recommendation
- Real-time prediction through the web interface

---

## 📸 Output Screenshots

<!-- Keep your existing screenshot/image links below this section -->

### Customer Segmentation Visualization

<img width="1005" height="799" alt="image" src="https://github.com/user-attachments/assets/b70f745b-5bea-42c2-8cc5-2a3e88ed205b" />

<img width="1026" height="558" alt="image" src="https://github.com/user-attachments/assets/362fab4f-d2ff-4fb8-b09c-cc4ddcda2871" />

<img width="1033" height="164" alt="image" src="https://github.com/user-attachments/assets/48f842c9-99ed-4882-9282-669b3de56e24" />

<img width="1443" height="676" alt="image" src="https://github.com/user-attachments/assets/2c942075-66be-4342-9ff0-8bff42b5cfed" />

### Model Comparison

<img width="462" height="392" alt="image" src="https://github.com/user-attachments/assets/6601e8a6-d3e0-4e5a-a3d9-4ee22096726b" />

Final model selected after hyperparameter tuning using GridSearchCV

<img width="849" height="415" alt="image" src="https://github.com/user-attachments/assets/be173202-cfcc-48ba-b747-3209ee2c809c" />


### Confusion Matrix

<img width="507" height="432" alt="image" src="https://github.com/user-attachments/assets/2be7e7ae-37ef-4c1a-9821-cf58c4b6df2c" />


### SegmentIQ Web Application

<img width="1895" height="871" alt="image" src="https://github.com/user-attachments/assets/1e43b2c3-9d3f-4c15-b6b8-2b766f64bc3b" />

<img width="1889" height="877" alt="image" src="https://github.com/user-attachments/assets/360fa5db-a569-49ba-9a45-db2e2939b6f1" />

<img width="1894" height="880" alt="image" src="https://github.com/user-attachments/assets/c92e3244-ac3b-4b20-b99b-98c6258a8b34" />

<img width="1886" height="411" alt="image" src="https://github.com/user-attachments/assets/b4e36ee4-330e-4ee1-99e9-d36f1a13e940" />

---

## 📊 Dataset

- **Marketing Campaign Dataset — Customer Personality Analysis**
- Contains customer demographics, spending behavior, purchasing patterns, household information, campaign responses, and customer engagement information.

### Dataset Link

https://drive.google.com/file/d/1zZgfcdlOpmqQHwaJHfs4V_sZq2-rvafT/view?usp=sharing

---

## 🔄 End-to-End Machine Learning Workflow

```text
Customer Dataset
       │
       ▼
Data Ingestion
       │
       ▼
Data Validation & Cleaning
       │
       ▼
Exploratory Data Analysis
       │
       ▼
Feature Engineering
       │
       ▼
Data Transformation
       │
       ▼
Clustering Experiments
(K-Means / Agglomerative / GMM / DBSCAN)
       │
       ▼
Clustering Evaluation
(Elbow Method + Silhouette Score)
       │
       ▼
K-Means — 3 Customer Segments
       │
       ▼
Classification Model Comparison
       │
       ▼
XGBoost Classifier
       │
       ▼
GridSearchCV Hyperparameter Tuning
       │
       ▼
Prediction Pipeline
       │
       ▼
FastAPI Web Application
       │
       ▼
Docker Containerization
       │
       ▼
Render Deployment
```

---

## 🛠️ Tech Stack

| Category | Technologies |
| -------- | ------------ |
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost |
| Clustering | K-Means, Agglomerative Clustering, GMM, DBSCAN |
| Hyperparameter Tuning | GridSearchCV |
| Dimensionality Reduction | PCA |
| Visualization | Matplotlib, Seaborn |
| Backend / API | FastAPI, Uvicorn |
| Database | MongoDB Atlas |
| Frontend | HTML, CSS |
| Containerization | Docker |
| Deployment | Render |
| Version Control | Git, GitHub |

---

## ⚙️ Machine Learning Pipeline

The production-level Machine Learning workflow consists of:

1. **Data Ingestion**
   - Retrieves and prepares customer data for the pipeline.

2. **Data Validation**
   - Validates incoming data and checks data quality.

3. **Data Transformation**
   - Performs preprocessing and feature transformation.

4. **Data Clustering**
   - Creates customer segments using the selected clustering approach.

5. **Model Training**
   - Trains the classification model for customer segment prediction.

6. **Model Evaluation**
   - Evaluates the trained model using classification metrics.

7. **Prediction Pipeline**
   - Uses the trained model to predict the segment of new customers.

---

## 🏗️ Production-Level Implementation

After completing experimentation in Jupyter Notebooks, the project was converted into a modular Python application.

The production pipeline separates the major Machine Learning responsibilities into reusable components.

```text
src/
│
├── components/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   ├── data_clustering.py
│   └── model_trainer.py
│
├── pipeline/
│   └── prediction_pipeline.py
│
├── configuration/
├── cloud_storage/
├── entity/
├── exception/
├── logger/
├── ml/
└── utils/
```

This modular architecture separates data processing, model training, prediction, configuration, logging, and other application responsibilities instead of keeping the complete workflow inside Jupyter Notebooks.

---

# 🚀 How to Run the Project

The application can be run either:

1. **Locally using Python**
2. **Inside a Docker container**

---

## 🔹 Option 1 — Run Locally

### Step 1: Clone Repository

```bash
git clone <your-repository-url>
cd <project-folder>
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Environment Variables

Create a `.env` file in the root directory and add:

```env
MONGO_DB_URL=your_mongodb_connection_string
```

> ⚠️ Never commit database credentials or your `.env` file to GitHub.

### Step 5: Run Application

```bash
python app.py
```

Open the application:

```text
http://localhost:5000
```

---

## 🔹 Train the Model

Open:

```text
http://localhost:5000/train
```

Or use the FastAPI Swagger documentation:

```text
http://localhost:5000/docs
```

Use the **train API endpoint** to start the training pipeline.

A successful execution should return a training success response.

---

## 🔹 Predict Customer Segment

Open:

```text
http://localhost:5000/
```

Enter the required customer information in the web interface to generate the predicted customer segment.

---

# 🐳 Run Using Docker

The application has been containerized using **Docker** so that the code and its dependencies can run consistently across different environments.

## Step 1: Build Docker Image

```bash
docker build -t customer_categorizer .
```

## Step 2: Run Docker Container

```bash
docker run -d --name segmentiq-container -p 5000:5000 customer_categorizer
```

## Step 3: Open Application

```text
http://localhost:5000
```

To verify that the container is running:

```bash
docker ps
```

---

## ☁️ Deployment

The application has successfully progressed through the following stages:

```text
Jupyter Notebook Experimentation
          ↓
Modular Python ML Pipeline
          ↓
FastAPI Application
          ↓
Docker Image
          ↓
Docker Container
          ↓
Render Cloud Deployment
          ↓
Public SegmentIQ Web Application
```

### 🌐 Live Deployment

👉 https://segmentiq-qyte.onrender.com

The deployed application can be accessed from any device with an internet connection.

---

## 📌 Key Features

- 🔍 Exploratory analysis of customer behavior
- 👥 Customer segmentation using unsupervised learning
- 🧪 Comparison of multiple clustering algorithms
- 📊 Cluster evaluation using Silhouette Score
- 📉 PCA-based cluster visualization
- 🤖 Comparison of multiple classification algorithms
- ⚡ XGBoost-based customer segment prediction
- 🔧 Hyperparameter tuning using GridSearchCV
- 📋 Classification report and confusion matrix evaluation
- 🔢 Automatic spending-related calculations in the UI
- ✅ Input validation
- ⚡ Real-time prediction through the web interface
- 🔄 End-to-End Machine Learning pipeline
- 🧩 Modular production-level Python architecture
- 🌐 FastAPI-based application
- 🐳 Docker containerization
- ☁️ Public deployment using Render

---

## 📈 Key Results

- ✅ Experimented with **K-Means, Agglomerative Clustering, GMM, and DBSCAN**
- ✅ Selected **3 customer segments** for the final K-Means solution
- ✅ Achieved a **0.5105 Silhouette Score** with K-Means at `k = 3`
- ✅ Evaluated **7 classification algorithms**
- ✅ XGBoost achieved approximately **96.43% accuracy before hyperparameter tuning**
- ✅ Achieved approximately **0.96 macro and weighted F1-score**
- ✅ Performed **5-fold GridSearchCV** hyperparameter tuning on XGBoost
- ✅ Converted notebook experimentation into a modular ML application
- ✅ Containerized the complete application using **Docker**
- ✅ Successfully deployed the application publicly using **Render**

---

## 💼 Business Value

SegmentIQ can help businesses:

- 🎯 Identify distinct customer groups
- 🧠 Understand differences in customer purchasing behavior
- 📣 Design segment-specific marketing strategies
- 🎁 Provide targeted offers and promotions
- 🤝 Improve customer engagement
- 📈 Support data-driven customer relationship decisions

---

## 🔮 Future Improvements

- [ ] CI/CD pipeline using GitHub Actions
- [ ] AWS deployment
- [ ] Cloud-based model storage using Amazon S3
- [ ] Model monitoring and data drift detection
- [ ] Automated model retraining
- [ ] Real-time customer data pipeline

---

## 📌 Conclusion

**SegmentIQ** demonstrates an end-to-end Machine Learning workflow that goes beyond model experimentation.

The project covers **data preprocessing, exploratory analysis, clustering experimentation, cluster evaluation, supervised model comparison, hyperparameter tuning, production-level code organization, API development, Docker containerization, and cloud deployment**.

The final system uses **K-Means clustering with three customer segments** and an **XGBoost-based classification pipeline** to predict the segment of new customers through an interactive web application.

The application has been successfully containerized using **Docker** and deployed publicly on **Render**, demonstrating the complete transition from Machine Learning experimentation to a deployable application.
