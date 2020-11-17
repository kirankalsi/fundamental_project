FROM python:3.7

WORKDIR /fundamental_project

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

#ENV DB_URI=${DB_URI}
ENV SECRET_KEY=${SECRET_KEY}

ENTRYPOINT ["python", "app.py"]
