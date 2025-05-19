import tkinter as tk
from tkinter import messagebox
import cv2
from keras.models import load_model
import numpy as np

# Load emotion detection model
emotion_model = load_model('emotion_model.h5', compile=False)

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def start_emotion_detection():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = np.expand_dims(roi, axis=0)
                roi = np.expand_dims(roi, axis=-1)
                prediction = emotion_model.predict(roi)[0]
                label = emotion_labels[np.argmax(prediction)]

                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

        cv2.imshow("Face Emotion Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# GUI using Tkinter
root = tk.Tk()
root.title("AI Emotion Detection")
root.geometry("400x300")
root.configure(bg="#ddeeff")

title = tk.Label(root, text="Emotion Detection System", font=("Arial", 18, "bold"), bg="#ddeeff")
title.pack(pady=20)

btn = tk.Button(root, text="Start Detection", command=start_emotion_detection, font=("Arial", 14), bg="#3399ff", fg="white")
btn.pack(pady=20)

note = tk.Label(root, text="Press 'q' to quit webcam", bg="#ddeeff", font=("Arial", 10))
note.pack(pady=10)

root.mainloop()
