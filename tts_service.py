from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

def text_to_speech(text):
    # Generate speech using gTTS (Google Text-to-Speech)
    tts = gTTS(text, lang='fa')
    output_file = f"output_{text[:5]}.mp3"
    tts.save(output_file)
    return output_file

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    text = data['text']
    output_file = text_to_speech(text)
    
    return jsonify({"audio_file": output_file})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
