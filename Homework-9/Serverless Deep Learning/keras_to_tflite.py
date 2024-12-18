1. Writing the Code
(a) Convert Keras to TF-Lite
File: keras_to_tflite.py
import tensorflow as tf

# Load the Keras model
model = tf.keras.models.load_model("model_2024_hairstyle.keras")

# Convert to TF-Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TF-Lite model
with open("model_2024_hairstyle.tflite", "wb") as f:
    f.write(tflite_model)

print(f"TF-Lite model size: {len(tflite_model) / (1024 * 1024):.2f} MB")
