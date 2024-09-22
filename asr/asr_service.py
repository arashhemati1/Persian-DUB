# Mock ASR service code
from flask import Flask, request

app = Flask(__name__)

@app.route('/asr', methods=['POST'])
def asr():
    video = request.files['file']
    # ASR logic here
    return "ASR text output"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
