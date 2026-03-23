FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r src/requirements.txt

EXPOSE 5000

CMD ["python", "src/app.py"]