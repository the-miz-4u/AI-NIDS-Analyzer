import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: API Key nahi mili .env file mein!")
else:
    print("🔍 Google ke server se available models fetch kar rahe hain...\n")
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        models = response.json().get('models', [])
        print("✅ YAHAN HAIN TUMHARE VALID MODELS (Inme se koi ek use karo):")
        print("-" * 50)
        for m in models:
            # Sirf wahi models print karenge jo text generate kar sakte hain
            if 'generateContent' in m.get('supportedGenerationMethods', []):
                # 'models/' prefix hata kar print kar rahe hain
                clean_name = m['name'].replace('models/', '')
                print(f"👉 {clean_name}")
        print("-" * 50)
    else:
        print(f"Error fetching models: {response.text}")