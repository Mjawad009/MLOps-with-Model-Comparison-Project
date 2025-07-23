# 🧠 Model Comparison Web App — House Price Prediction

This is a web-based machine learning app built with **Flask** and **Docker**, allowing users to input housing features and compare predictions from four trained ML models:

- **Linear Regression**
- **Decision Tree**
- **Random Forest**
- **XGBoost**

The app visualizes and compares results in real-time to help understand model performance differences.
![App Screenshot](result/main-page) .
![App Screenshot](result/result-page)

---

## 🚀 Features

- 📈 Model comparison on user-defined input.
- 🏡 Predict house prices using:
  - `HouseAge`
  - `AveRooms`
  - `AveBedrms`
- 💻 Built with Flask (Python web framework)
- 📦 Containerized with Docker
- ⚙️ Models trained in Jupyter/Google Colab, serialized with `pickle`.

---

## 🧰 Tech Stack

| Component         | Tool/Library           |
|------------------|------------------------|
| Backend          | Python, Flask          |
| ML Models        | scikit-learn, XGBoost  |
| Serialization    | Pickle                 |
| Frontend (basic) | HTML/CSS, Jinja2       |
| Containerization | Docker                 |

---

