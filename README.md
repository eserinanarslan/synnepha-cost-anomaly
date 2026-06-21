# Synnepha Cost Anomaly Detection & Forecasting

## Overview

This project was developed as part of a technical assessment focused on AWS cost monitoring, anomaly detection, forecasting, and production-ready deployment practices.

The solution combines:

* AWS Cost and Usage Report (CUR) analysis
* Kubernetes workload metrics analysis
* Machine Learning based anomaly detection
* Time-series forecasting
* Root cause investigation
* REST API serving layer
* Dockerized deployment
* Postman-based API testing

The objective is to identify unusual AWS cost behavior, forecast future costs, and expose results through a lightweight production-oriented API.

---

# Project Architecture

The solution consists of three main layers:

## 1. Analytics Layer (Notebooks)

Located under:

```text
notebooks/
```

### Cost Anomaly Detection

Notebook:

```text
01_cost_anomaly_detection.ipynb
```

Responsibilities:

* AWS CUR ingestion
* Kubernetes metrics ingestion
* Data validation
* Feature engineering
* Daily AWS cost aggregation
* Pod-day Kubernetes aggregation
* Rolling statistics generation
* Consensus Isolation Forest anomaly detection
* Root cause analysis
* Candidate anomaly selection

Output:

```text
question_1_candidate_cost_anomalies.csv
```

---

### Cost Forecasting

Notebook:

```text
02_cost_forecasting.ipynb
```

Responsibilities:

* Daily cost aggregation
* Trend analysis
* Time-series decomposition
* Forecast generation using Holt-Winters Exponential Smoothing
* Forecast evaluation

Output:

```text
question_2_daily_cost_forecast.csv
```

---

## 2. Service Layer

Located under:

```text
app/
```

The service layer exposes notebook outputs through a REST API.

Architecture:

```text
app/
├── api/
│   └── routes.py
│
├── config/
│   └── settings.py
│
├── models/
│   ├── anomaly_model.py
│   └── forecast_model.py
│
├── services/
│   ├── anomaly_service.py
│   └── forecast_service.py
│
└── utils/
    └── file_loader.py
```

Responsibilities:

* Configuration management
* CSV loading
* Service abstraction
* API routing
* Response serialization

---

## 3. Deployment Layer

The application is fully containerized using Docker.

Deployment components:

* FastAPI
* Uvicorn
* Docker
* Postman

This allows the solution to be deployed consistently across environments.

---

# Solution Workflow

```text
AWS CUR Export
       +
Kubernetes Metrics
       │
       ▼
Data Validation
       │
       ▼
Feature Engineering
       │
       ▼
Isolation Forest
Anomaly Detection
       │
       ▼
Root Cause Analysis
       │
       ▼
Anomaly Output CSV
       │
       ▼
REST API
```

```text
AWS CUR Export
       │
       ▼
Daily Cost Aggregation
       │
       ▼
Holt-Winters Forecasting
       │
       ▼
Forecast Output CSV
       │
       ▼
REST API
```

---

# Machine Learning Approach

## Anomaly Detection

Model:

```text
Consensus Isolation Forest
```

Features include:

* Daily AWS cost
* Daily usage quantity
* Cost deltas
* Rolling cost statistics
* Kubernetes CPU utilization
* Kubernetes memory utilization
* Pod-level workload variability

Hyperparameter stability analysis is performed across multiple Isolation Forest configurations.

Final anomalies are selected based on:

* Detection stability
* Cost impact
* Cost relevance

---

## Forecasting

Model:

```text
Holt-Winters Exponential Smoothing
```

Reasons for selection:

* Small dataset (~90 days)
* Clear trend structure
* Lightweight production deployment
* Interpretable results
* Fast retraining

Forecast horizon:

```text
14 Days
```

---

# API Endpoints

Swagger UI:

```text
http://localhost:8000/docs
```

Available endpoints:

## Health Check

```http
GET /health
```

Example:

```text
http://localhost:8000/health
```

---

## Get All Anomalies

```http
GET /anomalies
```

Example:

```text
http://localhost:8000/anomalies
```

---

## Get Anomaly By Rank

```http
GET /anomalies/{rank}
```

Example:

```text
http://localhost:8000/anomalies/1
```

---

## Get Forecast

```http
GET /forecast
```

Example:

```text
http://localhost:8000/forecast
```

---

# Configuration

Configuration is managed through:

```text
config.yaml
```

Example:

```yaml
server:
  host: 0.0.0.0
  port: 8000

files:
  anomaly_file: "./synnepha_exercise_90d/results/question_1_candidate_cost_anomalies.csv"
  forecast_file: "./synnepha_exercise_90d/results/question_2_daily_cost_forecast.csv"
```

---

# Running Locally

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Mac/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI service:

```bash
uvicorn main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

# Docker Deployment

Build image:

```bash
docker build -t synnepha-cost-anomaly-api .
```

Run container:

```bash
docker run -p 8000:8000 synnepha-cost-anomaly-api
```

Application becomes available at:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# Postman Testing

A Postman collection is included in the repository.

Import:

```text
collection/
└── synnepha_cost_anomaly_api.postman_collection.json
```

Available requests:

* Health Check
* Get All Anomalies
* Get Anomaly By Rank
* Get Forecast

Default base URL:

```text
http://localhost:8000
```

---

# Repository Structure

```text
SynnephaCostAnomaly/
│
├── app/
│
├── notebooks/
│   ├── 01_cost_anomaly_detection.ipynb
│   └── 02_cost_forecasting.ipynb
│
├── architecture/
│
├── collection/
│
├── synnepha_exercise_90d/
│
├── Dockerfile
├── requirements.txt
├── config.yaml
├── main.py
└── README.md
```

---

# Future Improvements

Potential production enhancements:

* Model registry integration
* Automated retraining pipelines
* CI/CD deployment
* Drift monitoring
* CloudWatch integration
* Slack/Teams notifications
* Real-time anomaly detection
* Infrastructure as Code (Terraform)

---

# Author

Eser İnan Arslan

Senior Data Scientist | Machine Learning Engineer | MLOps Engineer

Stockholm, Sweden
