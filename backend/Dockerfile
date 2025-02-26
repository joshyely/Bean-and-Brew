FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /beanandbrew/
COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH=/beanandbrew

EXPOSE 8000
EXPOSE 5000
CMD ["fastapi", "run", "--workers", "4", "--port", "8000" "beanandbrew/main.py"]