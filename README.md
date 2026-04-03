

---

 **Customer Segmentation and Predictive Analytics System**

📌 **Problem Statement**

This project focuses on analyzing customer data and segmenting customers into different groups based on their demographics and purchasing behavior. Businesses such as retail stores and e-commerce platforms can use this segmentation to better understand customer patterns and improve marketing strategies.

---

## 💡 Solution Overview

The system uses a **two-step machine learning approach**:

1. **Unsupervised Learning (Clustering)**  
   Customers are grouped into clusters using K-Means clustering based on their behavior and spending patterns.

2. **Supervised Learning (Classification)**  
   A trained **XGBoost Classifier** is used to predict the cluster of new customers based on input features.

### 🎯 Output Includes:
- Customer Category (e.g., Low Value, High Value)
- Cluster ID
- Business Recommendation (e.g., Discounts, Engagement Strategies)

---

## 📊 Dataset

- Marketing Campaign Dataset (Customer Personality Analysis)  
- Contains customer demographics, spending behavior, and campaign responses  

---

## 🛠️ Tech Stack Used

- Python  
- Flask (Web Application)  
- Machine Learning (Scikit-learn, XGBoost)  
- MongoDB Atlas (Database)  
- HTML, CSS, Bootstrap (Frontend)  

---

## ⚙️ Machine Learning Workflow

1. Data Ingestion from MongoDB  
2. Data Validation and Cleaning  
3. Feature Engineering & Transformation  
4. PCA for dimensionality reduction  
5. K-Means Clustering (for creating labels)  
6. XGBoost Classifier (for prediction)  
7. Model Deployment using Flask  

---

## 🚀 How to Run the Project

### 🔹 Step 1: Clone Repository
```bash
git clone <your-repo-link>
cd <project-folder>

**###🔹Step 2: Create Virtual Environment**

python -m venv venv
venv\Scripts\activate   # Windows

###🔹 Step 3: Install Dependencies

pip install -r requirements.txt

###🔹 Step 4: Set Environment Variables

Create a .env file and add:

MONGO_DB_URL=your_mongodb_connection_string


---

🔹 Step 5: Run Application

python app.py


---

🔹 Step 6: Train Model

Open in browser:

http://localhost:5000/train


---

🔹 Step 7: Predict Customer Segment

Open:

http://localhost:5000/

Fill the form → Get:

Cluster ID

Customer Category

Recommendation



---

📌 Key Features

Automatic Total Spending Calculation in UI

Input Validation (Children logic handling)

Real-time Prediction via Web Interface

End-to-End ML Pipeline (Training + Prediction)



---

🤖 Models Used

K-Means Clustering (for segmentation)

XGBoost Classifier (for prediction)

GridSearchCV (for hyperparameter tuning)



---

📂 Project Structure

src/
│
├── components/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   ├── data_clustering.py
│   ├── model_trainer.py
│
├── configuration/
├── entity/
├── utils/


---

📈 Results

Achieved ~96% accuracy using XGBoost Classifier

Effective clustering of customers into meaningful segments

Improved interpretability using category labels



---

📌 Conclusion

This system helps businesses:

Identify customer segments

Target customers effectively

Improve marketing strategies



---

🔮 Future Improvements

Docker Deployment

AWS Deployment (S3 + EC2)

Real-time data pipeline

Model monitoring


