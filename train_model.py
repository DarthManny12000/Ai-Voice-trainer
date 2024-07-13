# backend/train_model.py

import tensorflow as tf


def train_model(audio_file):
    # Load and preprocess the audio file
    # Define your model architecture
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(None, 1)),
        tf.keras.layers.LSTM(128, return_sequences=True),
        tf.keras.layers.LSTM(128),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    # Assuming `train_data` and `train_labels` are preprocessed and available
    model.fit(train_data, train_labels, epochs=10)

    # Save the trained model
    model.save('trained_model.h5')
