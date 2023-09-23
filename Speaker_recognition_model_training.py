import os
import numpy as np
import keras
import librosa

#Trainning and saving the model

# Define the parameters of the model and the preprocessing steps
n_mels = 128
n_fft = 2048
hop_length = 512
max_frames = 500

# Load the audio data and labels
data_dir = '[path to saved audio files to train the model with]'
labels = os.listdir(data_dir)
audio_data = []
speaker_ids = []
for i, label in enumerate(labels):
    speaker_dir = os.path.join(data_dir, label)
    for audio_file in os.listdir(speaker_dir):
        audio_path = os.path.join(speaker_dir, audio_file)
        audio, sr = librosa.load(audio_path)
        mel_spec = librosa.feature.melspectrogram(audio, sr=sr, n_mels=n_mels, n_fft=n_fft, hop_length=hop_length)
        mel_spec = librosa.power_to_db(mel_spec, ref=np.max)

        # Pad or truncate the Mel spectrogram to the desired length
        if mel_spec.shape[1] < max_frames:
            mel_spec = np.pad(mel_spec, ((0, 0), (0, max_frames - mel_spec.shape[1])), mode='constant')
        else:
            mel_spec = mel_spec[:, :max_frames]

        audio_data.append(mel_spec)
        speaker_ids.append(i)

# Convert the audio data and labels to numpy arrays
audio_data = np.array(audio_data)
speaker_ids = np.array(speaker_ids)

# Reshape the audio data to have the shape (num_samples, n_mels, max_frames, 1)
audio_data = np.expand_dims(audio_data, axis=-1)

# Define the model architecture
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(n_mels, max_frames, 1)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(len(labels), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(audio_data, speaker_ids, batch_size=32, epochs=10)

# Save the trained model as an .h5 file
model.save('path to saving model /model.h5')