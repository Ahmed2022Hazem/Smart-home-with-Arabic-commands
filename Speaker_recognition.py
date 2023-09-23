import keras
import librosa
import numpy as np
import sys
import time

#Used for detecting user

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
# Load the trained model from the .h5 file
model = keras.models.load_model('path to saved model/model.h5')

# Load the audio data of interest
audio_data, sr = librosa.load('path to saved audio file/s1.wav')

# Preprocess the audio data to make it compatible with the input shape required by the model
n_mels = 128
n_fft = 2048
hop_length = 512
mel_spec = librosa.feature.melspectrogram(audio_data, sr=sr, n_mels=n_mels, n_fft=n_fft, hop_length=hop_length)
mel_spec = librosa.power_to_db(mel_spec, ref=np.max)

# Pad or truncate the Mel spectrogram to the desired length
max_frames = 500 # Replace with your desired number of frames
if mel_spec.shape[1] < max_frames:
    mel_spec = np.pad(mel_spec, ((0, 0), (0, max_frames - mel_spec.shape[1])), mode='constant')
else:
    mel_spec = mel_spec[:, :max_frames]
 
mel_spec = np.expand_dims(mel_spec, axis=-1)
mel_spec = np.expand_dims(mel_spec, axis=0)

# Use the loaded model to predict the speaker in the preprocessed audio data
predicted_speaker = model.predict(mel_spec)

# Output the predicted speaker
labels = ['label1', 'label2', 'label3', 'label4', 'label5'] # Replace with your own labels
predicted_label = labels[np.argmax(predicted_speaker)]
print('Predicted speaker:', predicted_label)
x=0
Name = None

if(predicted_label=='label1'):
   x=1 
   print("مرحبا أول مستخدم")
   Name="User 1"
   import controlling_devices
if(predicted_label=='label2'):
   x=2
   print("مرحبا ثانى مستخدم")
   Name="User 2"
   import controlling_devices
if(predicted_label=='label3'):
   x=3 
   print("مرحبا ثالث مستخدم")
   Name="User 3"
   import controlling_devices
if(predicted_label=='label4'):
   x=4 
   print("مرحبا رابع مستخدم")   
   Name="User 4"
   import controlling_devices
if(predicted_label=='label5'):
   x=5 
   print("مرحبا خامس مستخدم ") 
   Name="User 5"
   import controlling_devices        
    

