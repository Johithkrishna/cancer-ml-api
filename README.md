# 🚀 Cancer ML API with CI/CD (MLOps Project)

An end-to-end **Machine Learning + MLOps project** where a cancer prediction model is trained, served via an API, and deployed automatically using **GitHub Actions + Google Cloud Run**.

---

## 📌 Project Overview

This project demonstrates how to move from:

👉 **Model Training → API Development → Deployment → Automation**

It follows real-world **MLOps practices**.

---

## 🧠 Problem Statement

Build a Machine Learning model to predict cancer outcomes and make it production-ready through an API.

---

## 🏗️ Project Structure

```bash
.
├── api/                     # FastAPI app (serving layer)
│   └── main.py
│
├── src/                     # Core ML code (data processing, utilities)
│
├── trainer/                 # Model training scripts
│
├── models/                  # Saved trained model (.pkl)
│
├── data/                    # Dataset
│
├── .github/workflows/       # CI/CD pipeline
│   └── deploy.yml
│
├── Dockerfile               # Containerization
├── requirements.txt         # Dependencies
├── .gitignore
├── .dockerignore
└── README.md
```

---

## ⚙️ Tech Stack

* **ML**: Scikit-learn
* **API**: FastAPI
* **Containerization**: Docker
* **Cloud**: Google Cloud Run
* **CI/CD**: GitHub Actions
* **Auth**: Workload Identity Federation (WIF)

---

## 🔄 ML Pipeline

1. Data ingestion (`data/`)
2. Data preprocessing (`src/`)
3. Model training (`trainer/`)
4. Model saved in (`models/`)
5. API loads model (`api/`)
6. Prediction endpoint exposed

---

## 🚀 API Endpoint

### POST `/predict`

#### Request:

```json
{
  "features": [value1, value2, ..., value30]
}
```

#### Response:

```json
{
  "prediction": 0
}
```

---

## 🐳 Run Locally

```bash
git clone <your-repo-url>
cd cancer-ml-api
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8080
```

---

## 🐳 Docker

```bash
docker build -t ml-api .
docker run -p 8080:8080 ml-api
```

---

## ☁️ Deployment (Cloud Run)

```bash
gcloud run deploy ml-api \
  --image gcr.io/<PROJECT_ID>/ml-api \
  --region asia-south1 \
  --platform managed \
  --allow-unauthenticated
```

---

## ⚙️ CI/CD Pipeline

Automated using **GitHub Actions**

### Workflow:

1. Push to `main`
2. Authenticate to GCP using WIF
3. Build Docker image
4. Push to Container Registry
5. Deploy to Cloud Run

---

## 🔐 Security

* No service account keys used
* Secure authentication via **Workload Identity Federation**

---

## 📊 Architecture

```
GitHub
   ↓
GitHub Actions (CI/CD)
   ↓
Workload Identity Federation (Auth)
   ↓
Cloud Build
   ↓
Container Registry
   ↓
Cloud Run (Live API)
```

---

## 📸 Screenshots (Add in repo)

* ✅ GitHub Actions success
* ✅ Cloud Run deployed service
* ✅ Swagger UI (`/docs`)
* ✅ API response

---

## 🎯 Key Learnings

* End-to-end ML pipeline design
* API deployment using FastAPI
* Docker containerization
* CI/CD automation
* Debugging real-world IAM & permission issues

---

## 🚀 Future Improvements

* Add model monitoring
* Add logging & alerts
* Add unit tests
* Add staging environment

---

## 🌐 Live API

👉 https://<your-cloud-run-url>

---

## 🤝 Contributing

Feel free to fork and improve.

---

## ⭐ If you like this project, give it a star!
 
