homework questions


## Steps to Reproduce

1. **Convert Keras to TF-Lite:**
   ```bash
   python keras_to_tflite.py


2. Test Image Preprocessing:
python image_preprocessing.py


3. Build and Run Docker Container:
docker build -t hairstyle-model .
docker run -p 8080:8080 hairstyle-model


4. Test Lambda Function:
curl -X POST -H "Content-Type: application/json" \
-d '{"image_url": "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"}' \
http://localhost:8080/2015-03-31/functions/function/invocations


5. Deploy to AWS (optional):

