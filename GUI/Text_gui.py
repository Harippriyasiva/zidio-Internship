import tkinter as tk
from textblob import TextBlob

def analyze_emotion():
    user_text = entry.get()
    blob = TextBlob(user_text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        result.set("Emotion: Happy 😊")
    elif polarity < 0:
        result.set("Emotion: Sad 😢")
    else:
        result.set("Emotion: Neutral 😐")

app = tk.Tk()
app.title("Text Emotion Analyzer")
app.geometry("400x200")

tk.Label(app, text="Enter your text:").pack(pady=10)
entry = tk.Entry(app, width=40)
entry.pack()

tk.Button(app, text="Analyze", command=analyze_emotion).pack(pady=10)

result = tk.StringVar()
tk.Label(app, textvariable=result, font=('Arial', 14)).pack(pady=10)

app.mainloop()

