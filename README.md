# 🛡️ AI-Powered Network Intrusion Analyzer (AI-NIDS) v1.0.1

An advanced, enterprise-grade Network Intrusion Detection System (NIDS) powered by Machine Learning and Generative AI. This project analyzes network packets in real-time to identify malicious traffic (such as DrDoS/DDoS attacks) and utilizes the Google Gemini API to provide instant, human-readable explanations and mitigation strategies for system administrators.

**Developed by:** Manish Sharma | B.Tech CSE (2023-2027)

---

## ✨ Key Features

*   **⚡ Real-Time Packet Analysis:** Instantly scans 15+ raw network features to classify traffic as 'Safe' or 'Malicious'.
*   **🤖 AI-Driven Incident Response:** Integrates Google Gemini AI to generate 3-line incident reports and immediate action plans for detected anomalies.
*   **📊 Live Dashboard & Analytics:** Features a dark-themed, responsive UI with real-time stats and dynamic Doughnut charts powered by `Chart.js`.
*   **📜 SIEM-Style Threat Log:** Maintains a live, scrollable history table of all scanned packets, status, and system actions (Blocked/Allowed).
*   **📄 Downloadable Incident Reports:** Allows network admins to download detailed `.txt` logs of malicious packets along with the AI mitigation strategy.
*   **📡 Live Traffic Interception:** Simulates real-time network interception by pulling live data streams from pre-processed CSV datasets (e.g., CIC-DDoS2019).
*   **🛠️ Interactive UX/UI:** Includes hover tooltips, a single-click dashboard reset, and responsive design elements.

---

## 🛠️ Technology Stack

*   **Backend Engine:** Python, Flask
*   **Machine Learning:** Scikit-Learn, NumPy, Pandas, Pickle
*   **Artificial Intelligence:** Google Gemini API (`google-genai`)
*   **Frontend UI:** HTML5, CSS3, Vanilla JavaScript, Chart.js

---

## ⚙️ Installation & Setup

Follow these steps to run the NIDS Analyzer locally on your machine.

### 1. Clone the Repository
    git clone https://github.com/your-username/AI-NIDS-Analyzer.git
    cd AI-NIDS-Analyzer

### 2. Set Up Virtual Environment (Recommended)
    python -m venv venv
    
    # On Windows:
    venv\Scripts\activate
    
    # On Mac/Linux:
    source venv/bin/activate

### 3. Install Dependencies
    pip install flask numpy google-genai python-dotenv requests

### 4. Configure Environment Variables
    Create a .env file in the root directory of the project and add your Google Gemini API Key:
    
    GEMINI_API_KEY=your_google_gemini_api_key_here

### 5. Run the Application
    python app.py
    
    (The NIDS Dashboard will start locally on http://127.0.0.1:5000/)

---

## 📂 Project Architecture

    AI-NIDS-Analyzer/
    │
    ├── dataset/                    # Raw and processed network datasets
    ├── templates/                  
    │   └── index.html              # Frontend dashboard UI (Charts, Logs, AI UI)
    ├── app.py                      # Core Flask backend and API routing
    ├── nids_model.pkl              # Pre-trained Random Forest ML model
    ├── test_api.py                 # Script for terminal-based API testing
    ├── find_model.py               # Script to fetch active Gemini models
    ├── .env                        # Environment variables (Hidden)
    ├── .gitignore                  # Git ignore rules
    └── README.md                   # Project documentation

---

## 🎯 How to Use the Dashboard

1.  **Load Attack:** Auto-fills the system with known malicious packet features for testing.
2.  **Load Safe:** Auto-fills the system with normal, benign network traffic data.
3.  **⚡ Live Intercept:** Fetches a random real-world network packet from the backend dataset.
4.  **Scan Traffic:** Submits the data to the ML model. If a threat is detected, it triggers the Gemini AI, updates the Live Stats chart, and logs the event in the Threat History table.
5.  **📄 Download Report:** Generate and download a detailed log file of any detected intrusion.
6.  **🗑️ Clear:** Resets the input fields and AI analysis without deleting your session's threat history.

---

## 📜 License & Disclaimer
This project is developed as an academic engineering project. It is intended for educational purposes, demonstrating the integration of Machine Learning and LLMs in cybersecurity.