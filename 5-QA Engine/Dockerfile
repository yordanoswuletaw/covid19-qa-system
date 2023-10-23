FROM python:3.8-slim
EXPOSE 8080
WORKDIR /qaapi
COPY . .
RUN pip3 install -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0  --port 8080