import os
from flask import Flask, render_template, request
from emotion_detector import detect_emotion
from music_suggester import load_spotify_credentials, get_spotify_token, search_spotify_song

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load Spotify credentials
def init_spotify():
    cid, cs = load_spotify_credentials()
    token = get_spotify_token(cid, cs)
    return token

token = init_spotify()

# Dummy tag extractor (replace this with actual image tag extractor like a Vision API or custom model)
def get_image_tags(image_path):
    # Example mocked tags based on filename or placeholder
    filename = os.path.basename(image_path).lower()
    tags = []

    if "traditional" in filename:
        tags.append("traditional")
    if "smile" in filename:
        tags.append("smile")
    if "pose" in filename:
        tags.append("pose")
    if "nature" in filename:
        tags.append("nature")
    if "dark" in filename:
        tags.append("dark lighting")
        tags.append("serious")
    return tags

@app.route('/', methods=['GET', 'POST'])
def index():
    songs = []
    mood = None
    photo_url = None

    if request.method == 'POST':
        lang = request.form['language']
        img = request.files['photo']
        if img:
            path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
            img.save(path)
            photo_url = path

            # Step 1: Get image tags (pose, smile, traditional etc.)
            tags = [tag.lower() for tag in get_image_tags(path)]

            # Step 2: Smart mood detection using tags
            if "traditional" in tags and "smile" in tags:
                mood = "festive"
            elif "fashion" in tags and "pose" in tags:
                mood = "boss vibe"
            elif "dark lighting" in tags and "serious" in tags:
                mood = "dramatic"
            elif "nature" in tags and "peaceful" in tags:
                mood = "chill"
            else:
                # Fallback to DeepFace emotion detection
                detected = detect_emotion(path)
                mood_map = {
                    'happy': 'happy',
                    'sad': 'sad',
                    'angry': 'energetic',
                    'surprise': 'energetic',
                    'neutral': 'chill',
                    'disgust': 'sad',
                    'fear': 'sad'
                }
                mood = mood_map.get(detected.lower(), 'chill')

            # Step 3: Get song suggestions
            songs = search_spotify_song(mood, lang, token)

    return render_template('index.html', photo=photo_url, mood=mood, songs=songs)

import os

@app.route('/')
def home():
    return "Hello from Railway!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT env var or 5000
    app.run(host="0.0.0.0", port=port)