# Heart_Disease_Prediction
# ❤️ Heart Disease Prediction using Machine Learning

A machine learning-powered web application that predicts the likelihood of heart disease based on patient health parameters. The application is built using **Python**, **Scikit-Learn**, and **Streamlit** for an interactive user experience.

## 🚀 Features

* Predicts heart disease risk using a trained KNN model.
* Interactive web interface built with Streamlit.
* Real-time predictions based on patient health data.
* Data preprocessing using StandardScaler.
* User-friendly form for entering medical information.

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* Scikit-Learn
* Pickle

## 📂 Project Structure

```text
Heart_Disease_Prediction/
│
├── app.py                    # Streamlit application
├── heart_disease_model.pkl   # Trained KNN model
├── scaler.pkl                # Feature scaler
├── disease_prediction.csv    # Dataset
├── KNN.ipynb                 # Model training notebook
└── README.md
```

## 📊 Input Features

The model uses the following features:

* Patient ID
* Age
* Gender
* Glucose Level
* Cholesterol Level
* Systolic Blood Pressure
* Diastolic Blood Pressure
* BMI
* Heart Rate
* Smoking Status
* Alcohol Consumption
* Family History
* Physical Activity Level

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kuldeepin3/Heart_Disease_Prediction.git
cd Heart_Disease_Prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

## 🎯 How It Works

1. User enters patient health information.
2. Data is preprocessed using the saved scaler.
3. The trained KNN model predicts the outcome.
4. The application displays whether heart disease is likely to be detected.

## 📸 Application Preview

Add screenshots of your application here.

## 🔮 Future Improvements

* Deploy on Streamlit Cloud.
* Add model performance metrics.
* Support multiple ML algorithms.
* Improve UI/UX design.
* Add patient report generation.

## 👨‍💻 Author

**Kuldeep Kirit Prajapati**

* GitHub: https://github.com/kuldeepin3
* LinkedIn: https://www.linkedin.com/in/kuldeep-prajapati-a929a32ab

## 📄 License

This project is open-source and available under the MIT License.
