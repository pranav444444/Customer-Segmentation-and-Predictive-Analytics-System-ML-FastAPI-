

# 🧠 Customer Segmentation and Predictive Analytics System

## 📌 Problem Statement

This project analyzes customer data and segments customers into different groups based on their demographics and purchasing behavior. Businesses such as retail stores and e-commerce platforms can use this segmentation to better understand customer patterns and improve marketing strategies.

---

## 💡 Solution Overview

The system uses a **two-step machine learning approach**:

1. **Unsupervised Learning (Clustering)**
   Customers are grouped into clusters using **K-Means clustering** based on their behavior and spending patterns.

2. **Supervised Learning (Classification)**
   A trained **XGBoost Classifier** predicts the cluster of new customers based on input features.

### 🎯 Output Includes
- Customer Category (e.g., Low Value, High Value)
- Cluster ID
- Business Recommendation (e.g., Discounts, Engagement Strategies)

--- 

### 🎯 Output Screenshots:

<img width="1005" height="799" alt="image" src="https://github.com/user-attachments/assets/6e262c35-46d3-4036-bb0c-59f5ecf2477d" />

<img width="1016" height="139" alt="image" src="https://github.com/user-attachments/assets/b7b44a84-09ab-401e-a060-a8e160567702" />

<img width="1443" height="676" alt="image" src="https://github.com/user-attachments/assets/d8a4d7f0-5276-4fcb-8a5a-a9e3fd2b8912" />

<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/a5f96ef6-6b81-4802-a1b7-5c824235673c" />

<img width="762" height="250" alt="image" src="https://github.com/user-attachments/assets/fa47e4db-7e20-4eb5-a1ea-fa06eea31a87" />

<img width="507" height="432" alt="image" src="https://github.com/user-attachments/assets/d31434ff-45e6-4cda-a9bc-4eeba4d3fc02" />

<img width="1274" height="447" alt="image" src="https://github.com/user-attachments/assets/8a3c99fe-6527-4725-899e-8840ea48b910" />

<img width="1623" height="669" alt="image" src="https://github.com/user-attachments/assets/7d156df7-ae98-43b7-aed9-c3f671ce61e6" />

<img width="1274" height="411" alt="image" src="https://github.com/user-attachments/assets/84c6eaf9-e3fb-43f8-ac1b-6f68c55149ef" />

<img width="1600" height="195" alt="image" src="https://github.com/user-attachments/assets/476f7345-718b-4862-a447-0244a837d662" />






---

## 📊 Dataset

- **Marketing Campaign Dataset** (Customer Personality Analysis)
- Contains customer demographics, spending behavior, and campaign responses
- https://drive.google.com/file/d/1zZgfcdlOpmqQHwaJHfs4V_sZq2-rvafT/view?usp=sharing

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|-------------|
| Backend | Python, Flask |
| Machine Learning | Scikit-learn, Pandas, Matplotlib, Seaborn |
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

```
http://localhost:5000/docs
```
<img width="1274" height="459" alt="image" src="https://github.com/user-attachments/assets/fb3aca12-2919-4721-968b-3eb22111328f" />

You must see **Training Successful !!** message displayed in output:
<img width="1274" height="593" alt="image" src="https://github.com/user-attachments/assets/781fe15c-c96e-40e5-92fe-e5facc3d0444" />



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


