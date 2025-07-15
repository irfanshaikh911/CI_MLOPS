# 💧 Water Potability Prediction Web App

A beginner-friendly end-to-end **MLOps** project that predicts whether water is **potable** (safe to drink) using a trained ML model.

---

## 🌟 What's Inside?

- 📊 ML model built with **scikit-learn**
- ⚡ Backend using **FastAPI**
- 🖥️ Frontend with **HTML + CSS + JavaScript**
- 🐳 Dockerized for portability
- 🚀 Deployed on **Render**
- 🔁 CI/CD using **GitHub Actions**
- 📦 Optional **DVC** for versioning

---

## 🔥 Preview

> 🎯 Web UI for water quality prediction

<p align="center">
  <img src="web/static/preview/landing-page.png" alt="Landing Page" width="600"/>
</p>

## ✅ Features

- ✔️ Predicts potability from 9 water quality parameters
- ✔️ Clean and responsive web UI
- ✔️ FastAPI-based `/api/predict` endpoint
- ✔️ ML model served using `joblib`
- ✔️ Fully Docker-compatible
- ✔️ Live on Render (free-tier deployment)
- ✔️ CI/CD setup using GitHub Actions
- ✔️ Optional versioning with DVC

---

## 🧠 Tech Stack

| Layer       | Technology         |
|-------------|--------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | FastAPI            |
| ML Model    | scikit-learn       |
| Container   | Docker             |
| Deployment  | Render             |
| CI/CD       | GitHub Actions ⚙️  |
| Versioning  | DVC (optional)     |

---

## 🏗️ Architecture

```text
+--------------+      POST      +-------------+      Load      +---------------+
|  HTML / JS   +------------->  | FastAPI API +------------->  |  joblib Model |
+--------------+               +-------------+                +---------------+
       ^                             |                               
       |        Serves HTML/CSS/JS   |                               
       |                             v                               
+----------------+        +-------------------+                    
|  styles.css    |        |  app.js (logic)   |                    
+----------------+        +-------------------+
```

## 🚀 Live Demo

> [🌐 Visit App on Render]((https://water-potability-cicd-pipeline.onrender.com/)) [Water Potability Detection]()


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
```bash
water-potability-app/
├── web/
│   ├── main.py                # FastAPI app with API routes
│   ├── templates/
│   │   └── index.html         # Frontend HTML page
│   └── static/
│       ├── css/               # Stylesheets
│       ├── js/                # JavaScript logic
│       └── preview/           # UI screenshots (optional)
├── models/
│   └── model.pkl              # Trained ML model
├── src/
│   ├── data_collection.py     # Data loading
│   ├── data_prep.py           # Data preprocessing
│   ├── datamodel.py           # Pydantic model for request validation
│   ├── model_building.py      # Training logic
│   ├── model_eval.py          # Evaluation metrics
│   └── model_reg.py           # Optional MLflow model registration
├── dvc.yaml                   # DVC pipeline configuration
├── params.yaml                # Parameters for the pipeline
├── requirements.txt           # Required Python packages
├── Dockerfile                 # Docker container setup
└── README.md                  # Project documentation
```

## 🙌 Acknowledgements

This project was built purely for **learning MLOps and CI/CD fundamentals**.

Special thanks to:
- The open-source community
- [FastAPI](https://fastapi.tiangolo.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [Render](https://render.com/)
- [Docker](https://www.docker.com/)
- [DVC](https://dvc.org/)
- [MLflow](https://mlflow.org/) 

---

## 📬 Contact

Made with ❤️ by **[Irfan Shaikh](https://www.linkedin.com/in/irfan-shaikh911/)**

Feel free to connect or suggest improvements.  
🔗 GitHub: [IrfanShaikh911](https://github.com/irfanshaikh911)

---


