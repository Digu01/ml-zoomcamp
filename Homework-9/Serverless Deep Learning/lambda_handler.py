(c) Lambda Function
File: lambda_handler.py
import tflite_runtime.interpreter as tflite
import numpy as np
from image_preprocessing import download_image, prepare_image

# Load the TFLite model
interpreter = tflite.Interpreter(model_path="model_2024_hairstyle_v2.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def lambda_handler(event, context):
    image_url = event["image_url"]
    img = download_image(image_url)
    prepared_img = prepare_image(img, (150, 150))  # Replace with actual target size

    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], prepared_img)

    # Run inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return {"prediction": float(output_data[0])}
