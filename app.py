# Author: Manish Sharma
import os
import pickle
import numpy as np
import warnings
from flask import Flask, request, jsonify
from google import genai
from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=UserWarning)
load_dotenv()

app = Flask(__name__)

with open('nids_model.pkl', 'rb') as file:
    model = pickle.load(file)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
                model='gemini-2.5-flash',
                contents=prompt,
            )
            response['ai_explanation'] = ai_response.text
            
        return jsonify(response)

    except Exception as e:
        print(f"\n🔥 BACKEND CRASH ERROR: {str(e)}\n") 
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)