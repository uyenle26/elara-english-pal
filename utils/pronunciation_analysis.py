import speech_recognition as sr

def analyze_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        transcript = recognizer.recognize_google(audio)
        return {"transcript": transcript.lower()}
    except:
        return {"transcript": ""}
