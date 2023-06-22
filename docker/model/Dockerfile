FROM python:3

WORKDIR /model_v

COPY ./src/model/requirements.txt /model_v/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/model/ /model_v/

CMD [ "python", "model.py", "--host=0.0.0.0"]