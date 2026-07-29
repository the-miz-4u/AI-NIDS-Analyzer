# Author: Manish Sharma
import os
import pickle
import numpy as np
import warnings
from flask import Flask, request, jsonify
from google import genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

warnings.filterwarnings("ignore", category=UserWarning)
load_dotenv()

app = Flask(__name__)

with open('nids_model.pkl', 'rb') as file:
    model = pickle.load(file)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_live_traffic', methods=['GET'])
def get_live_traffic():
    # Humne yahan CSV se nikal kar kuch real attack aur normal traffic ke packets daale hain
    live_packets = [
        # 🔴 DrDoS DNS Attack packet 1
        [17, 49830, 4, 0, 2048, 0, 512.0, 0.0, 80.2, 0.0, 16610.0, 0.0, 16610.0, 80.2, 41062.4],
        # 🟢 Normal/Safe Traffic packet 1
        [6, 80, 2, 0, 1024, 0, 256.0, 0.0, 40.0, 0.0, 8000.0, 0.0, 8000.0, 40.0, 20000.0],
        # 🔴 DrDoS Variation packet 2
        [17, 53, 10, 0, 4096, 0, 1024.0, 0.0, 120.5, 0.0, 30000.0, 0.0, 30000.0, 120.5, 80000.0],
        # 🟢 Normal/Safe Traffic packet 2
        [6, 443, 3, 1, 1500, 200, 500.0, 66.6, 50.0, 10.0, 5000.0, 1000.0, 6000.0, 45.0, 15000.0]
    ]
    
    # Randomly inme se koi ek packet select karega
    import random
    selected_packet = random.choice(live_packets)
    
    # List ko string (comma separated) banakar bhej rahe hain taaki textarea mein fit ho jaye
    packet_string = ", ".join(map(str, selected_packet))
    return jsonify({'raw_data': packet_string})

@app.route('/predict', methods=['POST'])
def predict_traffic():
    try:
        data = request.json
        features = data.get('features')
        
        if not features:
            return jsonify({'error': 'No features provided'}), 400
            
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        is_attack = int(prediction) == 1
        
        response = {
            'status': 'Malicious' if is_attack else 'Safe',
            'prediction_code': int(prediction)
        }
        
        if is_attack:
            prompt = f"""
            You are a Network Security Expert. We just detected an anomaly in the network traffic.
            Here is the raw feature data of the packet (numeric format): {features}
            Explain in a short, 3-line warning (in Hinglish) what kind of attack this might be 
            based on DrDoS/DDoS characteristics, and what immediate action the sysadmin should take.
            """
            
            # Sahi aur active model use kar rahe hain
            ai_response = client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt,
            )
            response['ai_explanation'] = ai_response.text
            
        return jsonify(response)

    except Exception as e:
        print(f"\n🔥 BACKEND CRASH ERROR: {str(e)}\n") 
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)