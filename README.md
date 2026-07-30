# 🛡️ AI-Powered Network Intrusion Analyzer (AI-NIDS)

An advanced, real-time Network Intrusion Detection System (NIDS) powered by Machine Learning and Generative AI. This project analyzes network packets to identify malicious traffic (such as DrDoS/DDoS attacks) and utilizes the Google Gemini API to provide instant, human-readable explanations and mitigation strategies for system administrators.

**Developed by:** Manish Sharma  

---

## ✨ Features

*   **⚡ Real-Time Packet Analysis:** Instantly scans raw network features to classify traffic as 'Safe' or 'Malicious'.
*   **🤖 AI-Driven Insights:** Integrates gemini-3.5-flash to generate 3-line incident reports and immediate action plans for detected anomalies.
*   **📡 Live Traffic Interception:** Simulates real-time network interception by pulling live data streams from pre-processed CSV datasets (e.g., CIC-DDoS2019).
*   **💻 Interactive Dashboard:** A sleek, responsive, dark-themed UI designed for security professionals and demonstrations.
*   **🚀 Lightweight Backend:** Powered by Flask for fast processing and seamless API communication.

---

## 🛠️ Technology Stack

*   **Backend:** Python, Flask
*   **Machine Learning:** Scikit-Learn, NumPy, Pickle
*   **Artificial Intelligence:** Google Gemini API (google-genai)
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally on your machine.

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
    (The server will start on http://127.0.0.1:5000/)

---

## 📂 Project Structure

    AI-NIDS-Analyzer/
    │
    ├── dataset/                    # Raw and processed datasets (e.g., DrDoS_DNS.csv)
    ├── templates/                  
    │   └── index.html              # Frontend dashboard UI
    ├── app.py                      # Core Flask backend and API routing
    ├── nids_model.pkl              # Pre-trained Machine Learning model
    ├── test_api.py                 # Script for terminal-based API testing
    ├── find_model.py               # Script to fetch active Gemini models
    ├── .env                        # Environment variables (Hidden)
    ├── .gitignore                  # Git ignore rules
    └── README.md                   # Project documentation

---

## 🎯 How to Use the Dashboard

1.  **Launch the App:** Open http://127.0.0.1:5000/ in your web browser.
2.  **Load Sample Attack:** Click this to auto-fill the system with known malicious packet features.
3.  **Load Safe Traffic:** Click this to test the system's response to normal, benign network traffic.
4.  **Intercept Live Traffic:** Simulates fetching a random real-world network packet from the dataset.
5.  **Scan Traffic:** Submits the data to the ML model and triggers the Gemini AI if a threat is detected.

---

## 📜 License
This project is for academic and educational purposes.