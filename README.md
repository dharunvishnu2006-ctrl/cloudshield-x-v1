# 🛡️ CloudShield X v1 — Server Log Security Analyzer

> The foundation of an enterprise-grade CSPM (Cloud Security Posture Management) platform — built from scratch in Python.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![pytest](https://img.shields.io/badge/pytest-Tested-yellow)

## 🚀 Live Demo
**[Try it live →](https://cloudshield-x-v1-4rdy68whxptnf6whzzrdrd.streamlit.app)**

## 📖 About

CloudShield X is an open-source CSPM platform that grows across 6 versions, each adding a new skill. **v1** is the foundation — a Python tool that reads server logs, detects brute-force attacks, raises alerts, and exports a security report.

Every fintech, e-commerce, and cloud platform generates millions of log lines daily — hidden in them are attackers probing for weaknesses. This tool catches them.

## ✨ Features

- **Log File Reader** — parses raw server logs (File I/O)
- **Suspicious IP Detector** — flags brute-force patterns via threshold-based counting
- **Alert System** — raises clear, testable warnings
- **CSV Report Generator** — exports professional security summaries (Pandas)
- **Interactive Dashboard** — live Streamlit web app with charts and downloads

## 🏗️ Architecture

Log File → Reader → IP Detector → Alert System → CSV Report
then connects down to → Streamlit Dashboard

## 🔧 Tech Stack

Python 3.11 · Pandas · NumPy · Streamlit · pytest · Git

## 💻 How to Run Locally

git clone https://github.com/dharunvishnu2006-ctrl/cloudshield-x-v1.git
cd cloudshield-x-v1
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

## 🧪 Testing

5 pytest tests cover data parsing, detection accuracy, report generation, and error handling:

python -m pytest -v

## 📚 What I Learned

- File I/O and error handling (try/except)
- Dictionary-based counting patterns for threat detection
- Building and testing with Pandas DataFrames
- Object-Oriented Programming (classes, `__init__`, `self`)
- Writing testable code with pytest
- Deploying Python apps to the cloud with Streamlit

## 🗺️ Roadmap

This is **v1 of 6**. Each future version adds a new layer of mastery toward a full enterprise CSPM platform:
- v2: Advanced Python & APIs
- v3: Cloud provider integrations (AWS/Azure)
- v4: Database & authentication
- v5: Real-time monitoring
- v6: Full enterprise dashboard

## 👤 Author

J. Dharun Vishnu — Future AI/ML + Cyber Security Engineer 🎯
