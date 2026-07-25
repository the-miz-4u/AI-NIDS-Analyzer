import requests
import json

dummy_features = [17, 49830, 4, 0, 2048, 0, 512.0, 0.0, 80.2, 0.0, 16610.0, 0.0, 16610.0, 80.2, 41062.4]

url = 'http://127.0.0.1:5000/predict'
payload = {'features': dummy_features}
headers = {'Content-Type': 'application/json'}

print("🚀 Sending network packet data to Flask API...\n")

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    result = response.json()
    
    # Agar backend se error aaya hai, toh use clearly print karo
    if 'error' in result:
        print(f"❌ ASLI ERROR YAHAN HAI:\n{result['error']}")
    else:
        print("--- 🛡️ NIDS Analyzer Response ---")
        print(f"Traffic Status: {result.get('status')}")
        print(f"Prediction Code: {result.get('prediction_code')}")
        
        if 'ai_explanation' in result:
            print("\n--- 🤖 Gemini AI Explanation ---")
            print(result['ai_explanation'])
            
except Exception as e:
    print(f"Connection Error: {e}")