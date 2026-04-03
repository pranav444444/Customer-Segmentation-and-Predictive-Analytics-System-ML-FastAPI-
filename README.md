

# 🧠 Customer Segmentation and Predictive Analytics System

## 📌 Problem Statement

This project analyzes customer data and segments customers into different groups based on their demographics and purchasing behavior. Businesses such as retail stores and e-commerce platforms can use this segmentation to better understand customer patterns and improve marketing strategies.

---

## 💡 Solution Overview

The system uses a **two-step machine learning approach**:

1. **Unsupervised Learning (Clustering)**
   Customers are grouped into clusters using K-Means clustering based on their behavior and spending patterns.

2. **Supervised Learning (Classification)**
   A trained **XGBoost Classifier** predicts the cluster of new customers based on input features.

### 🎯 Output Includes
- Customer Category (e.g., Low Value, High Value)
- Cluster ID
- Business Recommendation (e.g., Discounts, Engagement Strategies)

---

## 📊 Dataset

- **Marketing Campaign Dataset** (Customer Personality Analysis)
- Contains customer demographics, spending behavior, and campaign responses

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|-------------|
| Backend | Python, Flask |
| Machine Learning | Scikit-learn, XGBoost |
| Database | MongoDB Atlas |
| Frontend | HTML, CSS, Bootstrap |

---

## ⚙️ Machine Learning Workflow

1. Data Ingestion from MongoDB
2. Data Validation and Cleaning
3. Feature Engineering & Transformation
4. PCA for Dimensionality Reduction
5. K-Means Clustering (for creating labels)
6. XGBoost Classifier (for prediction)
7. Model Deployment using Flask

---

## 🚀 How to Run the Project

### 🔹 Step 1: Clone Repository

```bash
git clone <your-repo-link>
cd <project-folder>
```

### 🔹 Step 2: Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Step 4: Set Environment Variables

Create a `.env` file in the root directory and add:

```env
MONGO_DB_URL=your_mongodb_connection_string
```

### 🔹 Step 5: Run Application

```bash
python app.py
```

### 🔹 Step 6: Train the Model

Open in browser:

```
http://localhost:5000/train
```
Or

Open swagger by visiting the below link and click on **train** api to train the model

'''
http://localhost:5000/docs
'''

### 🔹 Step 7: Predict Customer Segment

Open:

```
http://localhost:5000/
```

Fill in the form to get:
- ✅ Cluster ID
- ✅ Customer Category
- ✅ Business Recommendation

---

## 📌 Key Features

- 🔢 Automatic Total Spending Calculation in UI
- ✅ Input Validation (Children logic handling)
- ⚡ Real-time Prediction via Web Interface
- 🔄 End-to-End ML Pipeline (Training + Prediction)

---

## 🤖 Models Used

| Model | Purpose |
|-------|---------|
| K-Means Clustering | Customer segmentation |
| XGBoost Classifier | Cluster prediction |
| GridSearchCV | Hyperparameter tuning |

---

## 📂 Project Structure

```
src/
│
├── components/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   ├── data_clustering.py
│   └── model_trainer.py
│
├── configuration/
├── entity/
└── utils/
```

---

## 📈 Results

- ✅ Achieved **~96% accuracy** using XGBoost Classifier
- ✅ Effective clustering of customers into meaningful segments
- ✅ Improved interpretability using category labels

---

## 📌 Conclusion

This system helps businesses:
- 🎯 Identify customer segments
- 📣 Target customers effectively
- 📈 Improve marketing strategies

---

## 🔮 Future Improvements

- [ ] Docker Deployment
- [ ] AWS Deployment (S3 + EC2)
- [ ] Real-time data pipeline
- [ ] Model monitoring
```

---


