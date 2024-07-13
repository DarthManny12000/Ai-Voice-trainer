from flask import Flask, request, jsonify, send_from_directory
import os
import librosa
import noisereduce as nr
import soundfile as sf

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Perform noise reduction
    y, sr = librosa.load(file_path, sr=None)
    reduced_noise = nr.reduce_noise(y=y, sr=sr)
    output_path = os.path.join(UPLOAD_FOLDER, 'cleaned_' + file.filename)
    sf.write(output_path, reduced_noise, sr)

    return jsonify({'success': 'File uploaded and noise reduced successfully', 'filename': 'cleaned_' + file.filename})


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True)
