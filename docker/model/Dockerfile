FROM python:3

WORKDIR /model_v

COPY ./src/model/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/model/ .

CMD [ "python", "model.py", "--host=0.0.0.0"]