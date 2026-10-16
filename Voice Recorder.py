import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# Settings
seconds = 5  # Kitne seconds tak record karna hai
fs = 44100   # Sample rate

print("Recording shuru ho chuki hai... Kuch boliye!")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int16')
sd.wait()  # Recording khatam hone ka wait karein
print("Recording khatam! File save ho rahi hai...")

# File save karein
write('my_audio_recording.wav', fs, audio)
print("Successfully 'my_audio_recording.wav' ke naam se save ho gayi hai!")