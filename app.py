from flask import Flask, render_template, request
from utils.pronunciation_analysis import analyze_audio
from utils.feedback_generator import generate_feedback

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    audio_file = request.files["audio"]
    result = analyze_audio(audio_file)
    feedback = generate_feedback(result)
    return feedback

if __name__ == "__main__":
    app.run(debug=True)
