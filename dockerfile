FROM tensorflow/tensorflow:2.12.0

WORKDIR /app

COPY ./final_cnn_model.h5 /app/final_cnn_model.h5
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
