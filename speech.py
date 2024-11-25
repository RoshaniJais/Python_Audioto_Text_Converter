import speech_recognition as sr
from pydub import AudioSegment

# Convert audio to WAV format in memory
audio = AudioSegment.from_file("aud.mp3")
audio.export("temp.wav", format="wav")

# Use SpeechRecognition to transcribe
recognizer = sr.Recognizer()
with sr.AudioFile("temp.wav") as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)
    print("Transcription:", text)
