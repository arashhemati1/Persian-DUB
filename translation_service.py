from flask import Flask, request, jsonify
from google.cloud import translate_v2 as translate
import os

app = Flask(__name__)

# Initialize the Google Translate client
def translate_text(text, target_language='fa'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    text = data['text']
    translated_text = translate_text(text)
    
    return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    # Set the environment variable for authentication
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "path_to_your_google_cloud_credentials.json"
    app.run(host='0.0.0.0', port=5000)
