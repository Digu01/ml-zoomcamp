(d) Dockerfile
File: Dockerfile

FROM public.ecr.aws/lambda/python:3.10

# Copy model and code
COPY model_2024_hairstyle_v2.tflite .
COPY lambda_handler.py .
COPY image_preprocessing.py .

# Install dependencies
RUN pip install numpy==1.23.1 \
    https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

# Command for Lambda
CMD ["lambda_handler.lambda_handler"]
