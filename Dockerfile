FROM python:3

COPY ./MainScores.py .
COPY ./Utils.py .
COPY ./Scores.txt .
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP="MainScores.py"

EXPOSE 5000

CMD ["python", "flask", "run", "--host=0.0.0.0"]