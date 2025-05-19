import tkinter as tk
import sounddevice as sd
import numpy as np
import librosa
import joblib
from scipy.io.wavfile import write
import os
import tempfile

# Load pre-trained voice emotion model
model = joblib.load("voice_emotion_model.pkl")  # Make sure this exists in your folder

# Feature extraction
def extract_features(audio_path):
    y, sr = librosa.load(audio_path, duration=3, offset=0.5)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

# Recording function
def record_audio():
    duration = 3  # seconds
    fs = 44100
    result.set("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    
    temp_path = os.path.join(tempfile.gettempdir(), "recording.wav")
    write(temp_path, fs, audio)
    
    features = extract_features(temp_path).reshape(1, -1)
    prediction = model.predict(features)[0]
    result.set(f"Detected Emotion: {prediction}")

# GUI
app = tk.Tk()
app.title("Voice Emotion Analyzer")
app.geometry("400x200")

tk.Label(app, text="Click to Record Voice").pack(pady=10)
tk.Button(app, text="Record and Analyze", command=record_audio).pack(pady=10)

result = tk.StringVar()
tk.Label(app, textvariable=result, font=('Arial', 14)).pack(pady=20)

app.mainloop()
