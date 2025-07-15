# 💧 Water Potability Prediction Web App

A beginner-friendly MLOps project that predicts whether water is **potable** (safe to drink) using a trained machine learning model.  
It includes a full stack:
- 📊 ML model built with `scikit-learn`
- ⚡ Backend using `FastAPI`
- 🖥️ Web UI built with `HTML + CSS + JavaScript`
- 🐳 Docker for containerization
- 🚀 Deployed on Render
- 📦 DVC (optional) for data/model versioning

---

## 🔥 Preview

> 🎯 Web UI for water quality prediction

![Landing Page](web/static/preview/landing-page.png)

---

## ✅ Features

- ✔️ Water quality prediction via 9 input parameters
- ✔️ Clean responsive UI
- ✔️ REST API `/api/predict`
- ✔️ Model served using `joblib`
- ✔️ Docker support
- ✔️ Deployed to Render (free tier)
- ✔️ CI/CD ready (GitHub Actions + DVC optional)

---

## 🧠 Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Frontend    | HTML, CSS, JS     |
| Backend     | FastAPI           |
| ML Model    | scikit-learn      |
| Packaging   | Docker            |
| Deployment  | Render            |
| CI/CD       | GitHub Actions ⚙️ |
| Versioning  | DVC (optional)    |

---

## 🏗️ Architecture
+-------------+ +--------------+ +-----------------+
| | POST | | Loads | |
| HTML/JS UI +--------->+ FastAPI API +--------->+ joblib Model |
| | | | | |
+-------------+ +--------------+ +-----------------+
  ^                        |
  |                        | Serves
  |                        v
+----------------+ +-----------------+
| styles.css | | app.js (logic) |
+----------------+ +-----------------+

---

## 🚀 Live Demo

> [🌐 Visit App on Render]((https://water-potability-cicd-pipeline.onrender.com/))  ![Uploading Screenshot 2025-07-15 230945.png…]()
![Uploading Screenshot 2025-07-15 230945.png…]()


---

## 💻 Run Locally

Follow these steps to clone and run locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/water-potability-mlops.git
cd water-potability-mlops
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the app with Uvicorn
``` bash
uvicorn web.main:app --reload --host 0.0.0.0 --port 8000
```
### Open browser at:
👉 http://localhost:8000

### 🐳 Run with Docker
```bash
docker build -t water-api .
docker run -p 8000:8000 water-api
```
---

## 📁 Project Structure
water-potability-app/
├── web/                        # Web-related files
│   ├── main.py                 # FastAPI app with API routes
│   ├── templates/
│   │   └── index.html          # Frontend HTML page
│   └── static/                 # Static frontend files
│       ├── css/                # Stylesheets
│       ├── js/                 # JavaScript logic
│       └── preview/            # UI screenshot(s) (optional)
│
├── models/
│   └── model.pkl               # Trained ML model (joblib or pickle)
│
├── src/                        # ML pipeline components
│   ├── data_collection.py      # Script to collect or load data
│   ├── data_prep.py            # Script to clean/preprocess data
│   ├── datamodel.py            # Pydantic BaseModel for request validation
│   ├── model_building.py       # Training script
│   ├── model_eval.py           # Model evaluation script
│   └── model_reg.py            # Optional: MLflow model registration
│
├── dvc.yaml                    # DVC pipeline configuration
├── params.yaml                 # Parameters used across pipeline
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker setup for deployment
└── README.md                   # Project documentation



---

## 🙌 Acknowledgements

This project was built purely for **learning MLOps and CI/CD fundamentals**.

Special thanks to:
- The open-source community
- [FastAPI](https://fastapi.tiangolo.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [Render](https://render.com/)
- [Docker](https://www.docker.com/)
- [DVC](https://dvc.org/)
- [MLflow](https://mlflow.org/) *(if used)*

---

## 📬 Contact

Made with ❤️ by **[Irfan Shaikh](https://www.linkedin.com/in/irfan-shaikh911/)**

Feel free to connect or suggest improvements.  
🔗 GitHub: [@your-github](https://github.com/irfanshaikh911)

---




