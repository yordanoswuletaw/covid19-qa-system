FROM python:3.8-slim
EXPOSE 8080
WORKDIR /SAM
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run streamlit_qa.py --server.port 8080