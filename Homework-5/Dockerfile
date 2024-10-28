FROM svizor/zoomcamp-model:3.11.5-slim
RUN pip install pipenv
COPY ["Pipfile","Pipfile.lock","./"]
RUN pipenv install --system --deploy
COPY ["predict_flask_service.py","./"]
CMD [ "gunicorn", "--bind", "0.0.0.0:9696", "predict_flask_service:app" ]
EXPOSE 9696
